#
# Deep Q-Learning Agent for Jobshop Scheduling
#
# Author: Lisa Ong, NUS/ISS
#
# References:
# https://github.com/srnand/Reinforcement-Learning-using-OpenAI-Gym/blob/master/DQN/cartpole_dqn.py
# https://github.com/keras-rl/keras-rl/blob/master/examples/dqn_cartpole.py

import numpy as np
import random
from collections import deque, OrderedDict

import tensorflow as tf
if float(tf.__version__.split('.')[0]) < 2.0:
    raise(Exception(f'Tensorflow >= 2.0 required, current version: {tf.__version__}'))

from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

class EpsilonPolicy:
    """Implements the epsilon policy
    """
    def __init__(self, epsilon_decay=.995, epsilon_min=.01):
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.epsilon = 1.

    def get(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        return self.epsilon

class DQNAgent:
    """Deep Q-Learning Agent
    observation_space: the observation space
    action_space: the action space
    gamma: the discount factor in considering future rewards
    alpha: how much prior knowledge to include
    epsilon_policy: object instance that defines the epsilon policy
    """
    def __init__(self, observation_space, action_space,
        gamma=.8, alpha=.1, epsilon_policy=EpsilonPolicy(),
        verbose=False):

        self.gamma = gamma
        self.alpha = alpha
        self.verbose = verbose
        self.epsilon_policy = epsilon_policy

        # 1 neural network per task to predict the Q values of start time
        # given the input observation
        self.action_space = action_space
        input_size = observation_space.spaces['is_scheduled'].shape[0]
        n_models = action_space['task_id'].n
        output_size = action_space['start_time'].n

        # batch size is either the number of actions in each episode, or
        # 16, whichever is smaller
        n_actions_per_episode = action_space['task_id'].n
        self.batch_size = min(n_actions_per_episode, 16)

        self.models = []
        for i in range(n_models):
            model = Sequential([
                Dense(input_size*4, input_dim=input_size, activation='relu'),
                Dense(input_size*4, activation='relu'),
                Dense(output_size, activation='linear')
            ])

            # start with a slow learning rate as we are fitting in smaller
            # batches (which will be noiser)
            model.compile(loss='mse', optimizer=Adam(lr=1e-3), metrics=['mae'])
            self.models.append(model)

        # Experience replay (to improve convergence)
        self.replay_memory = deque(maxlen=2000)
        self.prev_observation = None
        self.prev_action = None

    def _not_restarted(self, observation):
        return any(observation['is_scheduled'])

    def _get_best_action(self, observation):
        # find the action with the highest Q value
        is_scheduled = observation['is_scheduled']
        X = np.array([is_scheduled])
        Q_values = np.array([model.predict(X)[0] for model in self.models])

        # apply a mask so that we only select unscheduled tasks
        Q_values[np.array(is_scheduled) != 0, :] = -float('inf')

        # find task, start_time with the highest Q-value
        ind = np.unravel_index(np.argmax(Q_values, axis=None), Q_values.shape)

        # shift start_times by 1 (non-zero)
        best_action = OrderedDict([('task_id', ind[0]), ('start_time', ind[1]+1)])
        return best_action

    def act(self, observation, reward, done):
        """Update the Q-values, then take an action
        observation: current state
        reward: reward from the previous action (unused)
        done: whether the episode is completed
        """
        if self._not_restarted(observation):
            # not the first action, remember it and update model
            self._remember(self.prev_action, reward, observation, done)
            if len(self.replay_memory) > self.batch_size:
                self._replay()

        # determine the next action if not yet done
        action = None

        if not done:
            # epsilon greedy
            if random.uniform(0, 1) < self.epsilon_policy.get():
                # exploration: random action
                action = self.action_space.sample()
                action['start_time'] += 1 # non-zero start times
            else:
                # exploitation
                action = self._get_best_action(observation)

            self.prev_observation = observation
            self.prev_action = action

        return action

    def _remember(self, action, reward, observation, done):
        # deque will pop old entries automatically if filled to capacity
        self.replay_memory.append((self.prev_observation, action, reward,
            observation, done))

    def _replay(self):
        minibatch = random.sample(self.replay_memory, self.batch_size)
        for obs, action, reward, next_obs, done in minibatch:
            X = np.array([obs['is_scheduled']])
            if done:
                target = reward
            else:
                # find the maximum Q-value for all future actions
                next_X = np.array([next_obs['is_scheduled']])
                max_future_reward = np.array([model.predict(next_X)[0]
                    for model in self.models]).max()

                # apply Temporal Difference
                task_id = action['task_id']
                old_value = self.models[task_id].predict(X)[0]
                target = old_value + \
                    self.alpha * (reward + self.gamma * max_future_reward - old_value)

            # update the model
            self.models[task_id].fit(X, [[target]], epochs=1, verbose=self.verbose)

        # save the model weights
        [model.save(f'dqn_{task_id}.h5')
            for model, task_id in zip(self.models, range(len(self.models)))]

    def get_best_schedule(self):
        """Returns the scheduling actions based on highest Q-values.
        This requires the model weights to be already saved.
        """
        # load the model weights
        self.models = [load_model(f'dqn_{task_id}.h5')
            for task_id in range(len(self.models))]

        actions = []
        is_scheduled = [0] * len(self.models)

        while (not all(is_scheduled)):
            observation = OrderedDict([('is_scheduled', is_scheduled)])
            best_action = self._get_best_action(observation)
            actions.append(best_action)
            is_scheduled[best_action['task_id']] = best_action['start_time']

        return actions