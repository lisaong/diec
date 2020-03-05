#
# A Simple Path Finding OpenAI Gym Environment
#
# Inspired by: http://mnemstudio.org/path-finding-q-learning-tutorial.htm
# Author: Lisa Ong, NUS/ISS
#

import gym
from gym import spaces
import numpy as np
import random

class FrysHomeEnv(gym.Env):
  """Custom Environment describing Fry's home  
  
  For details on the gym.Env class:
  https://github.com/openai/gym/blob/master/gym/core.py
  """

  # render to the current display or terminal
  metadata = {'render.modes': ['human']}

  def __init__(self, rewards):
    super(FrysHomeEnv, self).__init__()

    self.rewards = rewards
    self.num_rooms = self.rewards.shape[0]

    # Action space describes all possible actions that can be taken
    # here, we can select 1 out of 6 rooms
    self.action_space = spaces.Discrete(self.num_rooms)

    # Observation space describes the valid observations
    # since we are moving between rooms, we can be in 1 of 6 rooms
    self.observation_space = spaces.Discrete(self.num_rooms)

    # Rewards range describes the min and max possible rewards
    self.reward_range = (self.rewards.min(), self.rewards.max())

    # Room 5 is our goal
    self.goal = 5

    # Initialise our state
    self.reset()

  def reset(self):
    """Reset the environment to an initial state"""

    # Randomly initialise the state
    self.state = random.randint(0, self.num_rooms-1)

    # Return the observation (same as the state in our case)
    obs = self.state
    return obs

  def step(self, action):
    """Execute one step within the environment"""

    # take the selected action
    prev_state = self.state
    self.state = action

    # calculate the reward
    reward = self.rewards[prev_state][action]

    # check if we've reached our goal
    done = (prev_state == self.goal or self.state == self.goal)

    # get the next observation
    obs = self.state

    return obs, reward, done, {}

  def render(self, mode='human', close=True):
    """Print state of the current environment"""
    print(f'Current room: {self.state}, Reached goal: {self.state == self.goal}')