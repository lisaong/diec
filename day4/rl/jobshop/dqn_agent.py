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

class DQNAgent:
    """Deep Q-Learning Agent
    observation_space: the observation space
    action_space: the action space
    """
    def __init__(self, observation_space, action_space, verbose=False):
        self.verbose = verbose

        input_size = observation_space.shape
        n_nets = action_space['task_id'].n
        output_size = action_space['start_time']
        
        action_size = action_space['task_id'].n * \
            action_space['start_time'].n

        # create neural network
        self.model = Sequential([
            Dense(input_size*4, input_dim=input_size, activation='relu'),
            Dense(input_size*4, activation='relu'),
            Dense(action_size, activation='softmax')
        ])


    def act(self, observation, reward, done):
        


        pass
    
    def get_best_schedule(self):
        pass # not implemented
