#
# Demonstration of Reinforcement Learning for Job Shop Scheduling.
#
# Job Shop scheduling problem:
# https://developers.google.com/optimization/scheduling/job_shop
#
# Author: Lisa Ong, NUS/ISS
#

import gym
import matplotlib.pyplot as plt
import numpy as np
import argparse

class AgentFactory:
    """Agent Factory to support delayed imports"""
    def available_agents():
        """Static method to return the available agents"""
        return ['baseline', 'qlearning', 'dqn']

    def create(name, env, max_schedule_time=20, verbose=False):
        """Static method to create an agents by name"""
        if name not in AgentFactory.available_agents():
            raise(Exception(f'Unsupported agent: {name}'))
        
        if name == 'baseline':
            from random_agent import RandomAgent
            return RandomAgent(env.action_space)

        if name == 'qlearning':
            from qlearning_td_agent import QLearningTDAgent
            return QLearningTDAgent(jobs_data=jobs_data, epsilon=.4,
                max_schedule_time=max_schedule_time, verbose=verbose)

        if name == 'dqn':
            from dqn_agent import DQNAgent
            return DQNAgent(env.observation_space, env.action_space,
                verbose=verbose)
        return None

def RunAgent(env, agent, episode_count, steps_per_episode):
    done = False
    reward = 0

    # track history of success
    success_history = []

    for episode in range(episode_count):
        print(f'======Episode {episode}======')
        obs = env.reset()
        for s in range(steps_per_episode):
            action = agent.act(obs, reward, done)
            obs, reward, done, info = env.step(action)

            print(f'Action: {action}, State: {obs}, \
Reward: {reward}, Done: {done}, Info: {info}')
            env.render()

            if done:
                print(f'Episode finished after {s+1} actions\n')
                done = False # reset for next episode
                if all(obs['is_scheduled']) and not info.get("errors"):
                    success_history.append([episode, info['makespan']])
                break

        env.close()

    print(f'Passing rate: {len(success_history)/episode_count * 100:.2f}%')

    if (len(success_history)):
        # do a histogram of successes, as the number of actions would be 
        # equivalent to the number of jobs
        fig, ax = plt.subplots()
        data = np.array(success_history)
        ax.hist(data[:, 1])
        ax.set(xlabel='makespan', ylabel='number of runs',
            title=f'{agent.__class__.__name__} after {episode_count} episodes')
        plt.savefig(f'{agent.__class__.__name__}_{episode_count}.png')

    return success_history

if __name__ == "__main__":
    # Each job is a list of multiple tasks: (machine_id, processing_time)
    jobs_data = [
        [(0, 3), (1, 2), (2, 2)],  # Job0
        [(0, 2), (2, 1), (1, 4)],  # Job1
        [(1, 4), (2, 3)]  # Job2
    ]

    parser = argparse.ArgumentParser(description='Job Shop Scheduling RL Demo')

    default_agent = 'qlearning'
    parser.add_argument('--agent', type=str, choices=AgentFactory.available_agents(),
        default=default_agent)

    default_episodes = 20000
    parser.add_argument('--episodes', type=int, default=default_episodes)
    parser.add_argument('--eval_only', type=int)
    parser.add_argument('--verbose', type=int)

    args = parser.parse_args()

    if args.agent is None:
        args.agent = default_agent
    if args.episodes is None:
        args.episodes = default_episodes
    if args.eval_only is None:
        args.eval_only = False
    if args.verbose is None:
        args.verbose = False

    # Create the environment
    env = gym.make('gym_jobshop:jobshop-v0', 
        jobs_data=jobs_data, max_schedule_time=20)
    env.reset()

    # Create the selected agent
    agent = AgentFactory.create(args.agent, env, verbose=args.verbose)
    print(f'\n*********{args.agent}*********')

    if not args.eval_only:
        # Run the agent
        # in order for all tasks to be scheduled,
        # steps_per_episode should exceed number of tasks
        RunAgent(env, agent, episode_count=args.episodes, steps_per_episode=20)

    print('\n*********Best Schedule*********')
    actions = agent.get_best_schedule()
    env.reset()
    for action in actions:
        _, _, _, info = env.step(action)
        print(f'Makespan: {info["makespan"]}, Errors: {info.get("errors")}')
    env.render()
