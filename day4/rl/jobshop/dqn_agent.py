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
    """
    def __init__(self, observation_space, action_space, verbose=False):
        self.verbose = verbose

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
        


        pass
    
    def get_best_schedule(self):
        pass # not implemented
