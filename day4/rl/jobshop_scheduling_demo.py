#
# Demonstration of Reinforcement Learning using Temporal
# Differencing for Jobshop Scheduling.
#

import gym
import gym_jobshop.envs.jobshop_env as jsenv
import numpy as numpy

def RunAgent(env, agent, episode_count, steps_per_episode):
    done = False
    reward = 0

    for episode in range(episode_count):
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
    gamma: the discount factor in considering future rewards
    alpha: how much prior knowledge to include
    verbose: whether to print debugging messages
    """
    def __init__(self, jobs_data, action_space, gamma=.8, alpha=.1, verbose=False):
        self.gamma = gamma
        self.alpha = alpha
        self.verbose = verbose
        self.action_space = action_space

        # utility for parsing jobs data
        self.tasks = jsenv.TaskList(jobs_data)

        # Q-values (aka the "brain" of the agent)
        self.Q = dict()

    def act(self, observation, reward, done):
        # TODO
        # update Q values
        action = self.action_space.sample()

        key = f'{observation}_{action.items()}'
        print(key)

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

    agent = QLearningTDAgent(jobs_data, env.action_space)

    # in order for all tasks to be scheduled,
    # steps_per_episode should exceed number of tasks
    RunAgent(env, agent, episode_count=100, steps_per_episode=10)