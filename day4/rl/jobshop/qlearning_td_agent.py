#
# Q-Learning Agent with Temporal Differencing for Jobshop Scheduling
#
# Author: Lisa Ong, NUS/ISS
#

import numpy as np
import random
from collections import OrderedDict
from copy import deepcopy
import pickle

import gym_jobshop.envs.jobshop_env as jobshop_env

class QLearningTDAgent:
    """Q-Learning Agent with Temporal Differencing
    jobs_data: list of jobs, where
          each job is a list of multiple tasks: (machine_id, processing_time)
    Example:
      jobs_data = [
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
      ]
    max_schedule_time: maximum schedule time
    gamma: the discount factor in considering future rewards
    alpha: how much prior knowledge to include
    epsilon: how much exploration (vs greedy exploitation)
    Q0: initial value of Q to use (higher values encourage exploration)
    verbose: whether to print debugging messages
    """
    def __init__(self, jobs_data, max_schedule_time=20,
        gamma=.8, alpha=.1, epsilon=0.2, Q0=0., verbose=False):
        self.gamma = gamma
        self.alpha = alpha
        self.verbose = verbose
        self.epsilon = epsilon
        self.Q0 = Q0
        self.max_schedule_time = max_schedule_time

        # utility for parsing jobs data
        self.tasks = jobshop_env.TaskList(jobs_data)

        # Q-values (aka the "brain" of the agent)
        # These are the values of taking an action given
        # the current observation
        # Schema:
        # {
        #   '[1, 5, 0, 0, 0, 10, 0, 0]' : 
        #   {
        #      action1: value1,
        #      action2: value2,
        #   }
        # }
        # Non-string keys may also be used but we are opting
        # for readability
        self.Q = dict()

    def _get_valid_actions(self, observation):
        # Gets all possible actions based on what is
        # currently assigned to each machine
        valid_actions = []
        is_scheduled = np.array(observation['is_scheduled'])

        # get the indices where condition is true
        candidate_task_ids = np.where(is_scheduled == 0)[0] # [0]: true, [1]: false
        candidate_tasks = [(i, self.tasks.get_task(i)) for i in candidate_task_ids]

        # create a mapping of available candidate tasks for each machine
        machines_to_tasks = {i:[] for i in range(self.tasks.get_num_machines())}
        for c in candidate_tasks:
            machines_to_tasks[c[1].machine_id].append(c[0])

        # for each machine, randomly select one task
        # select a random start time
        for machine_id, tasks_ids in machines_to_tasks.items():
            if len(tasks_ids) > 0:
                task_id = np.random.choice(tasks_ids)

                # start time must be > 0
                start_time = np.random.choice(self.max_schedule_time-1) + 1
                valid_actions.append(OrderedDict([('task_id', int(task_id)),
                    ('start_time', int(start_time))]))

        if self.verbose:
            print(f'DEBUG (Agent): Valid Actions: {valid_actions}')
        return valid_actions

    def _observation_to_key(self, observation):
        return f'{observation["is_scheduled"]}'

    def _action_to_key(self, action):
        return f'{action["task_id"]}_{action["start_time"]}'

    def _key_to_action(self, action_key):
        parts = action_key.split('_')
        return OrderedDict([('task_id', np.int64(parts[0])),
            ('start_time', np.int64(parts[1]))])

    def get_QValues(self, observation, actions=None):
        """Returns the Q values for a state and set of actions
        observation: the current state
        action: the set of actions, or None for all actions

        If actions=None, a dictionary is returned, 
        else a np.array is returned
        """
        result = []
        obs_key = self._observation_to_key(observation)
        if obs_key not in self.Q:
            self.Q[obs_key] = {}

        if actions is None:
            return self.Q[obs_key]
        else:
            for action in actions:
                action_key = self._action_to_key(action)
                if action_key not in self.Q[obs_key]:
                    self.Q[obs_key][action_key] = self.Q0

                result.append(self.Q[obs_key][action_key])
        return np.array(result)

    def set_QValue(self, observation, action, value):
        """Updates a Q-value
        observation: the state
        action: the action
        value: the Q-value
        """
        obs_key = self._observation_to_key(observation)
        action_key = self._action_to_key(action)
        if obs_key not in self.Q:
            self.Q[obs_key] = {}

        self.Q[obs_key][action_key] = value

        # save every N iterations
        if len(self.Q.keys()) % self.tasks.length() == 0:
            pickle.dump(self.Q, open(f'qlearning_td_Q.pkl', 'wb'))

    def act(self, observation, reward, done):
        """Update the Q-values, then take an action
        observation: current state
        reward: reward from the previous action (unused)
        done: whether the episode is completed
        """
        if done:
            return None

        action = None

        # epsilon-greedy
        if random.uniform(0, 1) < self.epsilon:
            # randomly select the next action/observation from valid actions
            valid_actions = self._get_valid_actions(observation)
            action = valid_actions[np.random.choice(len(valid_actions))]
        else:
            # find the action that has the maximum Q-value 
            action = self._get_best_action(observation)

        task = self.tasks.get_task(action['task_id'])

        # find the maximum Q-value for any future actions
        next_observation = deepcopy(observation)
        next_observation['is_scheduled'][action['task_id']] = action['start_time']
        next_valid_actions = self._get_valid_actions(next_observation)

        max_future_reward = 0.
        if len(next_valid_actions) > 0:
            max_future_reward = self.get_QValues(next_observation, next_valid_actions).max()
        else:
            max_future_reward = reward # done

        if self.verbose:
            print(f'DEBUG (Agent): Action: {action}, \
next state: {next_observation}, max future reward: {max_future_reward:.3f}')

        # update the Q matrix using Temporal Difference
        # Note: the previous action's reward is used instead
        old_value = self.get_QValues(observation, [action])[0]
        new_value = old_value + \
            self.alpha * (reward + self.gamma * max_future_reward - old_value)
        self.set_QValue(observation, action, new_value)

        if self.verbose >= 10:
            print(f'DEBUG (Agent): Q-values for {observation}\n\
{self.get_QValues(observation).values()}')

        return action

    def _get_best_action(self, observation):
        action_Qvalues = self.get_QValues(observation)
        if len(action_Qvalues):
            # sort by highest Q-value
            sorted_Qvalues = sorted(action_Qvalues.items(),
                key=lambda item:item[1], reverse=True)
            best_action = self._key_to_action(sorted_Qvalues[0][0])
        else:
            # no Q-values associated with this observation, use logic
            assert(f'{observation} has no Q values yet, will generate a start time')
            is_scheduled = observation['is_scheduled']
            task_id = (np.array(is_scheduled) == 0).argmax()
            last_scheduled_task = self.tasks.get_task(np.array(is_scheduled).argmax())
            start_time = np.array(is_scheduled).max() + last_scheduled_task.processing_time

            best_action = OrderedDict([('task_id', task_id), ('start_time', start_time)])

        return best_action

    def get_best_schedule(self):
        """Returns the scheduling actions based on highest Q-values
        This requires the model weights to be already saved.
        """
        self.Q = pickle.load(open(f'qlearning_td_Q.pkl', 'rb'))

        actions = []
        is_scheduled = [0] * self.tasks.length()

        # all() returns True if all elements are true, or if is_scheduled is empty
        while (not all(is_scheduled)):
            observation = OrderedDict([('is_scheduled', is_scheduled)])
            best_action = self._get_best_action(observation)
            actions.append(best_action)
            is_scheduled[best_action['task_id']] = best_action['start_time']

        return actions
