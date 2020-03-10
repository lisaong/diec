#
# A Job Shop Scheduling OpenAI Gym Environment
#
# Inspired by: https://developers.google.com/optimization/scheduling/job_shop
# Author: Lisa Ong, NUS/ISS
#

import gym
from gym import spaces
import numpy as np

class TaskList:
  def __init__ (self, jobs_data):
    num_jobs = len(jobs_data)
    self.tasks = [Task(i, *task) for i in range(num_jobs)
       for task in jobs_data[i]]

    self.jobs_to_tasks = {i:[] for i in range(num_jobs)}
    for i in range(len(self.tasks)):
      self.jobs_to_tasks[self.tasks[i].job_id].append(i)

    self.num_machines = 1 + max(t[0] for j in jobs_data for t in j)
    self.machines_to_tasks = {i: [] for i in range(self.num_machines)}
    for i in range(len(self.tasks)):
      self.machines_to_tasks[self.tasks[i].machine_id].append(i)

    self.reset()

  def reset(self):
    for t in self.tasks:
      t.reset()

    self.observations = {
      'latest_tasks': [0] * self.num_machines,
      'end_times':  [0] * self.num_machines
    }
    return self.observations

  def length(self):
    return len(self.tasks)

  def get_task(self, task_id):
    return self.tasks[task_id]

  def schedule_task(self, task_id, start_time):
    task = self.get_task(task_id)
    task.schedule(start_time)

    # update observations
    machine_id = task.machine_id
    self.observations['latest_tasks'][machine_id] = task_id
    self.observations['end_times'][machine_id] = task.end_time
    return self.observations

  def get_makespan(self):
    # find the tasks that started (end_time)
    start_times = [t.start_time for t in self.tasks if t.is_scheduled()]
    end_times = [t.end_time for t in self.tasks if t.is_scheduled()]

    if len(end_times) > 0:
      return max(end_times) - min(start_times)
    else:
      return 0 # nothing has been scheduled

  def get_related_tasks(self, task_id):
    task_ids = np.array(self.jobs_to_tasks[self.tasks[task_id].job_id])

    pre = task_ids[task_ids < task_id]
    post = task_ids[task_ids > task_id]
    return pre, post

  def all_tasks_scheduled(self):
    return sum([t.is_scheduled() for t in self.tasks]) == len(self.tasks)

  def __repr__(self):
    return '\n'.join([f'{i}: {self.tasks[i].__repr__()}'
      for i in range(len(self.tasks))])

class Task:
  def __init__(self, job_id, machine_id, processing_time):
    self.job_id = job_id
    self.machine_id = machine_id
    self.processing_time = processing_time
    self.reset()

  def reset(self):
    self.start_time = 0
    self.end_time = -1

  def schedule(self, start_time):
    self.start_time = start_time
    self.end_time = self.start_time + self.processing_time

  def is_scheduled(self):
    return self.end_time != -1

  def __repr__(self):
    return f'Job: {self.job_id}, Machine: {self.machine_id}, \
Start: {self.start_time}, End: {self.end_time}'

class JobshopEnv(gym.Env):
  """Custom Environment for a Job Shop Scheduling Problem
  
  For details on the gym.Env class:
  https://github.com/openai/gym/blob/master/gym/core.py
  """

  # render to the current display or terminal
  metadata = {'render.modes': ['human']}

  def __init__(self, jobs_data, max_schedule_time=20, verbose=False):
    """ jobs_data: list of jobs, where
          each job is a list of multiple tasks: (machine_id, processing_time)

        Example:
          jobs_data = [
            [(0, 3), (1, 2), (2, 2)],  # Job0
            [(0, 2), (2, 1), (1, 4)],  # Job1
            [(1, 4), (2, 3)]  # Job2
          ]

        max_schedule_time: maximum time allowed for the schedule
        verbose: whether to print debug messages
    """
    super(JobshopEnv, self).__init__()

    self.tasks = TaskList(jobs_data)
    self.max_schedule_time = max_schedule_time
    self.verbose = verbose

    # https://gym.openai.com/docs/#observations
    # Action space describes all possible actions that can be taken
    # here, we define an action as assigning 1 task
    # https://github.com/openai/gym/blob/master/gym/spaces/dict.py
    self.action_space = spaces.Dict({
      'task_id' : spaces.Discrete(self.tasks.length()),
      'start_time' : spaces.Discrete(self.max_schedule_time)
    })

    # Observation space describes the valid states
    # states may be used by the agent to determine the next action
    # here, we observe the latest tasks scheduled per machine
    # and their end-times
    # https://github.com/openai/gym/blob/master/gym/spaces/multi_discrete.py
    task_vec = [self.tasks.length()] * self.tasks.num_machines
    times_vec = [self.max_schedule_time] * self.tasks.num_machines
    self.observation_space = spaces.Dict({
      'latest_tasks':  spaces.MultiDiscrete(task_vec),
      'end_times':  spaces.MultiDiscrete(times_vec)
    })
        
    # Rewards range describes the min and max possible rewards
    # This is the default range, but we'll specify it explicitly below:
    self.reward_range = (-float('inf'), float('inf'))

    # Initialise our state
    self.reset()

  def reset(self):
    """Reset the environment to an initial state"""
    self.makespan = 0
    return self.tasks.reset()

  def calculate_reward(self, action):
    reward = 0
    id = action['task_id']
    start_time = action['start_time']

    task = self.tasks.get_task(id)
    end_time = start_time + task.processing_time

    pre, post = self.tasks.get_related_tasks(id)
    machine_tasks = self.tasks.machines_to_tasks[task.machine_id]

    # Constraint 1
    # Task already assigned
    if task.is_scheduled():
      reward -= 1
      if self.verbose:
        print(f'DEBUG: Task already scheduled: {id}')

    # Constraint 2
    # Machine already in use
    mtasks = [self.tasks.get_task(mt) for mt in machine_tasks if mt != id]
    overlap = [mt.is_scheduled() for mt in mtasks 
      if mt.is_scheduled() and
        (mt.start_time >= start_time or mt.end_time <= end_time)]
    if overlap:
      reward -= 1
      if self.verbose:
        print(f'DEBUG: Machine overlap: {task.machine_id}')

    # Constraint 3
    # Makespan exceeded
    makespan = self.tasks.get_makespan()
    if makespan >= self.max_schedule_time:
      reward -= 1
      if self.verbose:
        print(f'DEBUG: Makespan exceeded: {makespan}')

    if reward >= 0:
      # Task assigned in correct order and no overlap
      pre_tasks = [self.tasks.get_task(p) for p in pre]
      for pre in pre_tasks:
        if pre.is_scheduled() and pre.end_time <= start_time:
          reward += 50
      
      post_tasks = [self.tasks.get_task(p) for p in post]
      for post in post_tasks:
        if post.is_scheduled() and post.start_time >= start_time:
          reward += 50

      # reward shorter makespans
      reward += (self.max_schedule_time - makespan)*50

    return reward

  def step(self, action):
    """Execute one step within the environment"""
    # calculate the reward
    reward = self.calculate_reward(action)

    # take the action and get the next observation
    observation = self.tasks.schedule_task(action['task_id'],
      action['start_time'])

    # check if we've reached our goal or failed
    done = self.tasks.all_tasks_scheduled() or (reward < 0)

    return observation, reward, done, {}

  def render(self, mode='human', close=True):
    """Print state of the current environment"""
    print(f'Tasks: {self.tasks}')
    print(f'Makespan: {self.tasks.get_makespan()}')

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
  env.render()

  for i in range(5):
    action = env.action_space.sample()
    print(f'action: {action}')

    obs, reward, done, info = env.step(action)
    print(f'obs: {obs}, reward: {reward}, done: {done}')
    env.render()

    if done:
      print(f'took {i+1} action(s)')
      break