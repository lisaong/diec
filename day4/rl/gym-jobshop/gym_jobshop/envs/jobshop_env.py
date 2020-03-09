#
# A Job Shop Scheduling OpenAI Gym Environment
#
# Inspired by: https://developers.google.com/optimization/scheduling/job_shop
# Author: Lisa Ong, NUS/ISS
#

import gym
from gym import spaces
import numpy as np
import random

# constants for accessing the tuples
JOB = 0
MACHINE = 1
DURATION = 2

class JobshopEnv(gym.Env):
  """Custom Environment for a Job Shop Scheduling Problem
  
  For details on the gym.Env class:
  https://github.com/openai/gym/blob/master/gym/core.py
  """

  # render to the current display or terminal
  metadata = {'render.modes': ['human']}

  def __init__(self, jobs, max_schedule_time=20):
    """ jobs_data: list of jobs, where
          each job is a list of multiple tasks: (machine_id, processing_time)

        Example:
          jobs_data = [
            [(0, 3), (1, 2), (2, 2)],  # Job0
            [(0, 2), (2, 1), (1, 4)],  # Job1
            [(1, 4), (2, 3)]  # Job2
          ]

        max_schedule_time: maximum time allowed for the schedule
    """
    super(JobshopEnv, self).__init__()

    # Flatten the jobs data by index by encoding the job_id into the tuple
    # the *task syntax will unpack a tuple
    self.jobs_list = [(i, *task) for i in range(len(jobs_data)) 
      for task in jobs_data[i]]

    self.max_schedule_time = max_schedule_time

    # https://gym.openai.com/docs/#observations
    # Action space describes all possible actions that can be taken
    # here, we define an action as assigning 1 task
    # https://github.com/openai/gym/blob/master/gym/spaces/dict.py
    self.action_space = spaces.Dict({
      'task_id' : spaces.Discrete(len(self.jobs_list)),
      'start_time' : spaces.Discrete(max_schedule_time)
    })

    # Observation space describes the valid observations in the environment
    # here, we can track makespan
    self.observation_space = spaces.Discrete(max_schedule_time)

    # Rewards range describes the min and max possible rewards
    # This is the default range, but we'll specify it explicitly below:
    self.reward_range = (-float('inf'), float('inf'))

    # Initialise our state
    self.reset()

  def reset(self):
    """Reset the environment to an initial state"""
    self.tasks_start_times = [-1.] * len(self.jobs_list)
    self.makespan = 0

    return self.makespan

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

# Unit test
if __name__ == "__main__":
  # Each job is a list of multiple tasks: (machine_id, processing_time)
  jobs_data = [
    [(0, 3), (1, 2), (2, 2)],  # Job0
    [(0, 2), (2, 1), (1, 4)],  # Job1
    [(1, 4), (2, 3)]  # Job2
  ]

  env = JobshopEnv(jobs_data)
  obs = env.reset()
  print(obs)

  action = env.action_space.sample()
  print(action)