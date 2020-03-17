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
  """Used to track the state of tasks in a Job Shop Environment
  """
  def __init__ (self, jobs_data):
    """jobs_data: list of jobs, where
        each job is a list of multiple tasks: (machine_id, processing_time)

    Example:
      jobs_data = [
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
      ]
    """
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
    """Reset the state of all tasks
    """
    for t in self.tasks:
      t.reset()

    self.observation = {
      'is_scheduled':  [0] * self.length()
    }
    return self.observation

  def length(self):
    """Return the total number of tasks
    """
    return len(self.tasks)

  def get_num_machines(self):
    """Return the total number of machines
    """
    return len(self.machines_to_tasks)

  def get_task(self, task_id):
    """Retrieve a task
    task_id: the task index
    """
    return self.tasks[task_id]

  def get_machines_to_tasks(self):
    """Returns the mapping of machines to tasks
    """
    return self.machines_to_tasks

  def schedule_task(self, task_id, start_time):
    """Schedule a task and returns the observation
    task_id: the task index
    start_time: the task start time
    """
    # start_time = 0 means task has not been scheduled
    if start_time <= 0:
      raise Exception('start_time should be > 0')
    task = self.get_task(task_id)
    task.schedule(start_time)

    # update observation
    machine_id = task.machine_id
    self.observation['is_scheduled'][task_id] = start_time

    return self.observation

  def get_makespan(self):
    """Return the makespan (duration of the earliest start time
    to the latest end time)
    """
    start_times = [t.start_time for t in self.tasks if t.is_scheduled()]
    end_times = [t.end_time for t in self.tasks if t.is_scheduled()]

    if len(end_times) > 0:
      return max(end_times) - min(start_times)
    else:
      return 0 # nothing has been scheduled

  def get_related_tasks(self, task_id):
    """Return all tasks related to the current task. Here "related to"
    means sharing the same job
    task_id: the task index
    This returns a tuple of lists: pretasks, posttasks
    """
    task_ids = np.array(self.jobs_to_tasks[self.tasks[task_id].job_id])

    pre = task_ids[task_ids < task_id]
    post = task_ids[task_ids > task_id]
    return pre, post

  def all_tasks_scheduled(self):
    """Return whether all tasks have been scheduled
    """
    return sum(self.get_tasks_is_scheduled()) == self.length()

  def get_tasks_is_scheduled(self):
    """Return a list of 1 or 0 indicating if each
    has been scheduled
    """
    return [int(t.is_scheduled()) for t in self.tasks]

  def __repr__(self):
    return '\n'.join([f'{i}: {self.tasks[i].__repr__()}'
      for i in range(len(self.tasks))])

class Task:
  """Encapsulates the state of a task in a Job Shop Environment
  """
  def __init__(self, job_id, machine_id, processing_time):
    """job_id: the job id this task belongs to
    machine_id: the machine id that this task must run
    processing_time: the task processing time
    """
    self.job_id = job_id
    self.machine_id = machine_id
    self.processing_time = processing_time
    self.reset()

  def reset(self):
    """Reset this task
    """
    self.start_time = 0
    self.end_time = -1

  def schedule(self, start_time):
    """Schedule this task
    """
    self.start_time = start_time
    self.end_time = self.start_time + self.processing_time

  def is_scheduled(self):
    """Return whether this task has already been scheduled
    """
    return self.end_time != -1

  def __repr__(self):
    return f'Job: {self.job_id}, Machine: {self.machine_id}, \
Start: {self.start_time}, End: {self.end_time}'

class JobshopEnv(gym.Env):
  """Custom Environment for a Job Shop Scheduling Problem

  For details on the scheduling problem:
  https://developers.google.com/optimization/scheduling/job_shop
  
  For details on the gym.Env class:
  https://github.com/openai/gym/blob/master/gym/core.py
  """
  # render to the current display or terminal
  metadata = {'render.modes': ['human']}

  def __init__(self, jobs_data, max_schedule_time=20, verbose=False):
    """jobs_data: list of jobs, where
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
    # here, we observe the latest tasks scheduled, with their
    # (non-zero) start times specified.
    # https://github.com/openai/gym/blob/master/gym/spaces/multi_discrete.py
    #
    # Example:
    #  {
    #   'is_scheduled': [0, 0, 1, 0, 5, 0, 10, 1] - tasks 2, 4, 6, 7 already scheduled
    #                                               tasks 0, 1, 3, 5 not yet scheduled
    #  }
    #
    is_scheduled_vec = [self.max_schedule_time] * self.tasks.length()

    # A dictionary give flexibility to add other observations in the future
    self.observation_space = spaces.Dict({
      'is_scheduled': spaces.MultiDiscrete(is_scheduled_vec)
    })
        
    # Rewards range describes the min and max possible rewards
    # This is the default range, but we'll specify it explicitly below:
    self.reward_range = (-float('inf'), float('inf'))

    # Initialise our state
    self.reset()

  def reset(self):
    """Reset the environment to an initial state
    """
    return self.tasks.reset()

  def calculate_reward(self, action):
    """Compute the reward for taking an action
    action: the action being considered

    Returns the reward and any error info
    """
    reward = 0
    error_info = ''
    id = action['task_id']
    start_time = action['start_time']

    task = self.tasks.get_task(id)
    end_time = start_time + task.processing_time

    pre, post = self.tasks.get_related_tasks(id)
    machine_tasks = self.tasks.machines_to_tasks[task.machine_id]

    # Constraint 1
    # Task already assigned
    if task.is_scheduled():
      reward -= 100
      error_info = 'Duplicate Scheduling'
      if self.verbose:
        print(f'DEBUG (Env): Task already scheduled: {id}')

    # Constraint 2
    # Machine already in use
    # To detect this case, we collect all the start and end times
    # for scheduled/to-be-run tasks on the machine, sort by start times,
    # then flatten the tuples into [start, end, start, end, ...]
    # none of the times should overlap
    mtasks = [(self.tasks.get_task(mt).start_time, self.tasks.get_task(mt).end_time)
      for mt in machine_tasks if (mt != id and self.tasks.get_task(mt).is_scheduled())]
    mtasks.append((start_time, end_time))
    mtasks.sort(key=lambda t:t[0])
    flattened = np.array([t for ts in mtasks for t in ts])
    overlap = sum(flattened[:-1] > flattened[1:]) > 0
    if self.verbose:
      print(f'DEBUG (Env): Checking for overlap: {flattened}')

    if overlap:
      reward -= 100
      error_info = 'Machine Overlap'
      if self.verbose:
        print(f'DEBUG (Env): Machine overlap: {task.machine_id}, {flattened}')

    # Constraint 3
    # Makespan exceeded
    makespan = self.tasks.get_makespan()
    if makespan >= self.max_schedule_time:
      reward -= 100
      error_info = 'Makespan Exceeded'
      if self.verbose:
        print(f'DEBUG (Env): Makespan exceeded: {makespan}')

    # Constraint 4
    # Tasks must be in the right order
    not_in_order = 0

    # Task assigned in correct order and no overlap
    pre_tasks = [self.tasks.get_task(p) for p in pre]
    for pre in pre_tasks:
      if pre.is_scheduled() and pre.end_time >= start_time:
        not_in_order += 1

    post_tasks = [self.tasks.get_task(p) for p in post]
    for post in post_tasks:
      if post.is_scheduled() and post.start_time <= start_time:
        not_in_order += 1

    if not_in_order > 0:
      error_info = 'Out-of-sequence tasks'
      reward -= (100 * not_in_order)
      if self.verbose:
        print('DEBUG (Env): Out-of-sequence tasks')

    # If we made it this far, none of the constraints have been violated
    # reward for more tasks scheduled without errors
    if reward >= 0:
      reward += 50 * sum(self.tasks.get_tasks_is_scheduled())

    return reward, error_info

  def step(self, action):
    """Take an action
    action: the action being taken
    """
    # calculate the reward
    reward, error_info = self.calculate_reward(action)

    # take the action and get the next observation
    observation = self.tasks.schedule_task(action['task_id'],
      action['start_time'])

    # check if we should stop (all tasks scheduled)
    done = self.tasks.all_tasks_scheduled()
    makespan = self.tasks.get_makespan()
    if self.tasks.all_tasks_scheduled():
      reward += 100 * (self.max_schedule_time - makespan)

    info = {'makespan': makespan}
    if len(error_info):
      info['errors'] = error_info
    return observation, reward, done, info

  def render(self, mode='human', close=True):
    """Print state of the current environment
    """
    print(f'Job-view:\n{self.tasks}')

    print(f'\nMachine-view:')
    for machine, tasks in self.tasks.get_machines_to_tasks().items():
      task_info = []
      for t in tasks:
        task = self.tasks.get_task(t)
        if task.is_scheduled():
          task_info.append((t, task.start_time, task.end_time))

      status = ''
      timeline = ''
      if len(task_info) > 0:
        task_info.sort(key=lambda t:t[1]) # sort by start time
        prev = 0

        for ti in task_info:
          if prev > ti[1]: # overlap
            status += '\n' + (' ' * ti[1]) + f'{ti[0]}' * (ti[2] - ti[1])
          else:
            status += (' ' * (ti[1] - prev)) + f'{ti[0]}' * (ti[2] - ti[1])
          prev = ti[2]

        timeline = ['-'] * max(task_info, key=lambda t:t[2])[2]
        if len(timeline) >= 5:
          timeline[::5] = ['|' for t in timeline[::5]]
        timeline = '\n' + ''.join(timeline)
      else:
        status = 'idle'

      print(f'\nMachine {machine}:{timeline}')
      print(status)

# Unit test
if __name__ == "__main__":
  # Each job is a list of multiple tasks: (machine_id, processing_time)
  jobs_data = [
    [(0, 3), (1, 2), (2, 2)],  # Job0
    [(0, 2), (2, 1), (1, 4)],  # Job1
    [(1, 4), (2, 3)]  # Job2
  ]

  env = JobshopEnv(jobs_data, verbose=True)
  obs = env.reset()
  env.render()

  for i in range(10):
    action = env.action_space.sample()
    print(f'======{i}======\naction: {action}')

    obs, reward, done, info = env.step(action)
    print(f'obs: {obs}, reward: {reward}, done: {done}, info: {info}')
    env.render()

    if done:
      print(f'took {i+1} action(s)')
      break