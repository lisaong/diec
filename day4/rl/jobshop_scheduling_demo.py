#
# Demonstration of Reinforcement Learning using Temporal
# Differencing for Job Shop Scheduling.
#
# Job Shop scheduling problem:
# https://developers.google.com/optimization/scheduling/job_shop
#

import gym
import gym_jobshop.envs.jobshop_env as jsenv
import numpy as np
from collections import OrderedDict

def RunAgent(env, agent, episode_count, steps_per_episode):
    done = False
    reward = 0

    # track history of pass / fail
    pass_count = 0

    for episode in range(episode_count):
        print(f'======Episode {episode}======')
        obs = env.reset()
        for s in range(steps_per_episode):
            action = agent.act(obs, reward, done)
            obs, reward, done, info = env.step(action)

            print(f'Action: {action}, State: {obs}, \
Reward: {reward}, Done: {done}, Info: {info}')
            if done:
                print(f'Episode finished after {s+1} actions\n')
                done = False # reset for next episode
                pass_count += \
                    np.sum(obs['is_scheduled']) == len(obs['is_scheduled'])
                break
            env.render()

        env.close()

    print(f'Passing rate: {pass_count/episode_count * 100:.2f}')

class RandomAgent:
    """The world's simplest agent!
      https://github.com/openai/gym/blob/master/examples/agents/random_agent.py
    """
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()

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
    verbose: whether to print debugging messages
    """
    def __init__(self, jobs_data, max_schedule_time=20,
        gamma=.8, alpha=.1, verbose=False):
        self.gamma = gamma
        self.alpha = alpha
        self.verbose = verbose
        self.max_schedule_time = max_schedule_time

        # utility for parsing jobs data
        self.tasks = jsenv.TaskList(jobs_data)

        # Q-values (aka the "brain" of the agent)
        # These are the values of taking an action given
        # the current observation
        self.Q = dict()

    def _get_valid_actions(self, observation):
        # Gets all possible actions based on what is
        # currently assigned to each machine
        valid_actions = []
        start_times = np.array(observation['available_times'])
        is_scheduled = np.array(observation['is_scheduled'])

        # get the indices where condition is true
        candidate_task_ids = np.where(is_scheduled == 0)[0] # [0]: true, [1]: false
        candidate_tasks = [(i, self.tasks.get_task(i)) for i in candidate_task_ids]

        # create a mapping of available candidate tasks for each machine
        machines_to_tasks = {i:[] for i in range(len(start_times))}
        for c in candidate_tasks:
            machines_to_tasks[c[1].machine_id].append(c[0])

        # for each machine, randomly select one task
        # set the start time to the end time of its machine
        for (machine_id, tasks_ids), start_time in zip(machines_to_tasks.items(), start_times):
            if len(tasks_ids) > 0:
                task_id = np.random.choice(tasks_ids)
                valid_actions.append(OrderedDict([('task_id', task_id),
                    ('start_time', start_time)]))

        if self.verbose:
            print(f'DEBUG (Agent): Valid Actions: {valid_actions}')
        return valid_actions

    def get_QValues(self, observation, actions):
        """Returns the Q values for a state and set of actions
        observation: the current state
        action: the action
        """
        result = []
        for action in actions:
            key = f'{observation}_{action}'
            if key not in self.Q:
                self.Q[key] = 0.

            result.append(self.Q[key])
        return np.array(result)

    def set_QValue(self, observation, action, value):
        """Updates a Q-value
        observation: the state
        action: the action
        value: the Q-value
        """
        key = f'{observation}_{action}'
        self.Q[key] = value

    def act(self, observation, reward, done):
        """Update the Q-values, then take an action
        observation: current state
        reward: reward from the previous action (unused)
        done: whether the episode is completed
        """
        if done:
            return None
        
        # randomly select the next action/observation from valid actions
        valid_actions = self._get_valid_actions(observation)
        action = valid_actions[np.random.choice(len(valid_actions))]
        task = self.tasks.get_task(action['task_id'])

        # find the maximum Q-value for any future actions
        next_observation = observation.copy()
        next_observation['available_times'][task.machine_id] = action['start_time'] \
            + task.processing_time
        next_observation['is_scheduled'][action['task_id']] = 1
        next_valid_actions = self._get_valid_actions(next_observation)

        max_future_reward = 0.
        if len(next_valid_actions) > 0:
            max_future_reward = \
                self.get_QValues(next_observation, next_valid_actions).max()
        else:
            max_future_reward = 100 # done

        if self.verbose:
            print(f'DEBUG (Agent): Action: {action}, \
next state: {next_observation}, max future reward: {max_future_reward:.3f}')

        # update the Q matrix using Temporal Difference
        # Note: the previous action's reward is used instead
        old_value = self.get_QValues(observation, [action])[0]
        new_value = old_value + \
            self.alpha * (reward + self.gamma + max_future_reward - old_value)
        self.set_QValue(observation, action, new_value)

        if self.verbose >= 10:
            print(f'DEBUG (Agent): Q-values\n{self.Q.values()}')

        return action

    def get_best_schedule(self):
        """Returns the scheduling actions based on highest Q-values
        """
        pass


if __name__ == "__main__":
    # Each job is a list of multiple tasks: (machine_id, processing_time)
    jobs_data = [
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
    ]

    env = gym.make('gym_jobshop:jobshop-v0', 
        jobs_data=jobs_data, max_schedule_time=12)

    agents = [
        RandomAgent(env.action_space),
        QLearningTDAgent(jobs_data=jobs_data, max_schedule_time=12)
    ]

    for agent in agents:
        print(f'\n*********{agent}*********')

        env.reset()
        # in order for all tasks to be scheduled,
        # steps_per_episode should exceed number of tasks
        RunAgent(env, agent, episode_count=100, steps_per_episode=10)