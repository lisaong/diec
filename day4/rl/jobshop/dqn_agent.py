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
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

if tf.__version__ < 2.0:
    raise(Exception(f'Tensorflow >= 2.0 required, current version: {tf.__version__}'))

class DQNAgent:
    """Deep Q-Learning Agent
    observation_space: the observation space
    action_space: the action space
    gamma: the discount factor in considering future rewards
    alpha: how much prior knowledge to include
    epsilon: how much exploration (vs greedy exploitation)
    """
    def __init__(self, observation_space, action_space,
        gamma=.8, alpha=.1, epsilon=0.2, verbose=False):

        self.gamma = gamma
        self.alpha = alpha
        self.verbose = verbose
        self.epsilon = epsilon
        self.action_space = action_space

        # 1 neural network per task to predict the Q values of start time
        # given the input observation
        input_size = observation_space.shape
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
            model.compile(loss='mse', optimizer=Adam(lr=1e-3))
            self.models.append(model)

        # Experience replay (to improve convergence)
        self.replay_memory = deque(maxlen=2000)
        self.prev_observation = None
        self.prev_action = None

    def _not_restarted(self, observation):
        return all(observation['is_scheduled'])

    def act(self, observation, reward, done):
        """Update the Q-values, then take an action
        observation: current state
        reward: reward from the previous action (unused)
        done: whether the episode is completed
        """
        if self._not_restarted(observation)
            # not the first action, remember it and update model
            self._remember(self.prev_action, reward, observation, done)
            if len(self.replay_memory) > self.batch_size:
                self._replay()

        # determine the next action if not yet done
        action = None

        if not done:
            # epsilon greedy
            if random.uniform(0, 1) < self.epsilon:
                # exploration
                action = self.action_space.sample()
            else:
                # exploitation, find the model with the highest Q value
                Q_values = np.array([model.predict(observation)[0]
                    for model in self.models])
                
                task_id = Q_values.argmax()
                start_time = Q_values[task_id].max()
                action = OrderedDict([('task_id', task_id), ('start_time', start_time)])

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
            if done:
                target = reward
            else:
                # find the maximum Q-value for all future actions
                max_future_reward = np.array([model.predict(next_obs)[0]
                    for model in self.models]).max()

                # apply Temporal Difference
                task_id = action['task_id']
                old_value = self.models[task_id].predict(s)[0]
                target = old_value + \
                    self.alpha * (reward + self.gamma * max_future_reward - old_value)

            if self.verbose:
                print(f'DEBUG (Agent): Action: {action}, \
    next state: {next_obs}, max future reward: {max_future_reward:.3f}')

            self.models[task_id].fit(obs, [[target]], epochs=1, verbose=0)

    def get_best_schedule(self):
        """Returns the scheduling actions based on highest Q-values
        """
        pass # not implemented
