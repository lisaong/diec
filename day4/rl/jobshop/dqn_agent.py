#
# Deep Q-Learning Agent for Jobshop Scheduling
#
# Author: Lisa Ong, NUS/ISS
#
# References:
# https://github.com/srnand/Reinforcement-Learning-using-OpenAI-Gym/blob/master/DQN/cartpole_dqn.py
# https://github.com/keras-rl/keras-rl/blob/master/examples/dqn_cartpole.py

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam

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

        # 1 neural network per task to predict the Q values of start time
        # given the input observation
        input_size = observation_space.shape
        n_models = action_space['task_id'].n
        output_size = action_space['start_time'].n
        
        self.models = []
        for i in range(n_models):
            model = Sequential([
                Dense(input_size*4, input_dim=input_size, activation='relu'),
                Dense(input_size*4, activation='relu'),
                Dense(output_size, activation='linear')
            ])

            # start with a slow learning rate as we are fitting incrementally
            model.compile(loss='mse', optimizer=Adam(lr=1e-3))
            self.models.append(model)

    def act(self, observation, reward, done):
        """Update the Q-values, then take an action
        observation: current state
        reward: reward from the previous action (unused)
        done: whether the episode is completed
        """


        pass
    
    def get_best_schedule(self):
        """Returns the scheduling actions based on highest Q-values
        """
        pass # not implemented
