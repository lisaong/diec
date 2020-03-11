#
# Demonstration of Reinforcement Learning using Temporal
# Differencing for Jobshop Scheduling.
#

import gym
import gym_jobshop.envs.jobshop_env as jsenv
import numpy as np
from collections import OrderedDict

def RunAgent(env, agent, episode_count, steps_per_episode):
    done = False
    reward = 0

    for episode in range(episode_count):
        print(f'======Episode {episode}======')
        obs = env.reset()
        for s in range(steps_per_episode):
            action = agent.act(obs, reward, done)
            print(f'action: {action}')

            obs, reward, done, info = env.step(action)
            print(obs)
            if done:
                print(f'Episode finished after {s+1} actions\n')
                done = False # reset for next episode
                break
            env.render()

        env.close()

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

    def _create_action(self, task_id, start_time):
        return OrderedDict([('task_id', task_id),
            ('start_time', start_time)])

    def _get_valid_actions(self, observation):
        # Gets all possible actions based on what is
        # currently assigned to each machine
        valid_actions = []

        latest_tasks = observation['latest_tasks']
        end_times = observation['end_times']
        n = len(latest_tasks)

        is_scheduled = np.array(self.tasks.get_tasks_is_scheduled())
        available_tasks = np.where(is_scheduled == 0)
        available_tasks_by_machine = {
            m_id : [tid]
        }

        # for each machine
        # randomly select a task
        # set the start time to the end time of its machine
        for i, t, e in zip(range(n), latest_tasks, end_times):
            if e == 0: # no tasks assigned to machine (yet)
                # randomly select a task for a machine
                task_id = np.random.choice(np.array(machines_to_tasks[i]))
                start_time = np.random.choice(self.max_schedule_time)
                valid_actions.append(self._create_action(task_id, start_time))

            else: # task assigned to machine
                # randomly select a remaining task

                start_time = np.random.choice(self.max_schedule_time)

                _, post = self.tasks.get_related_tasks(t)
                print(t, post)
                if len(post) > 0:
                    task_id = post[0]
                    machine_id = self.tasks.get_task(task_id).machine_id
                    start_time = end_times[machine_id]
                    valid_actions.append(self._create_action(task_id, start_time))
                    print(self._create_action(task_id, start_time))
        return valid_actions

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

        # find the maximum Q-value for future actions
        # an action is (task_id, start_time)
        next_observation = observation.copy()
        task = self.tasks.get_task(action['task_id'])
        next_observation['latest_tasks'][task.machine_id] = action['task_id']
        next_observation['end_times'][task.machine_id] = action['start_time'] \
            + task.processing_time

        print(f'Next observation: {next_observation}')

        return action

if __name__ == "__main__":
    # Each job is a list of multiple tasks: (machine_id, processing_time)
    jobs_data = [
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
    ]

    env = gym.make('gym_jobshop:jobshop-v0', 
        jobs_data=jobs_data, max_schedule_time=20, verbose=True)

    agent = QLearningTDAgent(jobs_data=jobs_data, max_schedule_time=20)

    # in order for all tasks to be scheduled,
    # steps_per_episode should exceed number of tasks
    RunAgent(env, agent, episode_count=100, steps_per_episode=10)