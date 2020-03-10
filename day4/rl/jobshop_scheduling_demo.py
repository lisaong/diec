#
# Demonstration of Reinforcement Learning using Temporal
# Differencing for Jobshop Scheduling.
#

import gym
import numpy as numpy

class RandomAgent:
    """The world's simplest agent!
      https://github.com/openai/gym/blob/master/examples/agents/random_agent.py
    """
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()

def RunRandomAgent(jobs_data, episode_count, steps_per_episode):
    env = gym.make('gym_jobshop:jobshop-v0', jobs_data=jobs_data, max_schedule_time=12)
    agent = RandomAgent(env.action_space)

    done = False
    reward = 0

    for episode in range(episode_count):
        obs = env.reset()
        for s in range(steps_per_episode):
            action = agent.act(obs, reward, done)
            print(f'action: {action}')

            obs, reward, done, info = env.step(action)
            if done:
                print(f'Episode finished after {s+1} actions\n')
                done = False # reset for next episode
                break
            env.render()

        env.close()

if __name__ == "__main__":
    # Each job is a list of multiple tasks: (machine_id, processing_time)
    jobs_data = [
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
    ]

    # in order for all tasks to be scheduled,
    # steps_per_episode should exceed number of tasks
    RunRandomAgent(jobs_data, episode_count=100, steps_per_episode=10)