#
# Demonstration of Reinforcement Learning using Temporal
# Differencing for path finding.
# Refer to path_finding_demo.ipynb for more explanation.
#

import gym
import numpy as np
import random

class QLearningTDAgent:
  """Q-Learning Agent with Temporal Differencing"""
  def __init__(self, rewards, gamma=0.8, alpha=0.1, verbose=False):
    """rewards: the rewards matrix
    gamma: the discount factor in considering future rewards
    alpha: how much prior knowledge to include
    """
    self.rewards = rewards

    # Initialise the Q-matrix to zeros:
    # dimensions (row=state, cols=actions)
    self.Q = np.zeros(rewards.shape)

    self.gamma = gamma
    self.alpha = alpha
    self.verbose = verbose

  def _get_valid_actions(self, observation):
    actions = np.arange(self.rewards.shape[1])
    return actions[self.rewards[observation] != -1]

  def act(self, observation, reward, done):
    """Update the Q-matrix, then take an action
    observation: current state
    reward: reward from the previous action (unused)
    done: whether the episode is completed
    """
    # randomly select the next action/observation
    valid_actions = self._get_valid_actions(observation)
    action = np.random.choice(valid_actions)

    if not done:
      # find the maximum Q-value for all future actions
      next_observation = action
      all_actions = self._get_valid_actions(next_observation)
      future_rewards = self.Q[next_observation][all_actions]

      print(f'Action: {action}, next state: {next_observation}, \
  all actions: {all_actions}, all future rewards: {future_rewards}, \
  max future reward: {future_rewards.max():.3f}')

      # update the Q matrix
      # this is where temporal difference is applied
      old_value = self.Q[observation][action]
      self.Q[observation][action] = old_value + \
        self.alpha * (self.rewards[observation][action] + \
                    self.gamma * future_rewards.max() - old_value)

      if self.verbose:
        print(f'Q-values:\n{self.Q}')

    return action

  def best_path(self, initial_state, goal=5):
    """Returns the best path starting from a given state"""
    path = [initial_state]
    state = initial_state

    while(True):
      state = self.Q[state].argmax()
      path.append(state)
      if state == goal:
        break

    return path

if __name__ == "__main__":
  # Global state
  EPISODE_COUNT = 100
  STEPS_PER_EPISODE = 20
  done = False
  reward = 0

  R = np.array([[-1, -1, -1, -1,  0, -1 ],
              [-1, -1, -1,  0, -1, 100],
              [-1, -1, -1,  0, -1, -1 ],
              [-1,  0,  0, -1,  0, -1 ],
              [ 0, -1, -1,  0, -1, 100],
              [-1,  0, -1, -1,  0, 100]])

  # Track how many timesteps it took to finish
  history = {start:[] for start in range(R.shape[0])}

  env = gym.make('gym_fryshome:fryshome-v0', rewards=R)
  agent = QLearningTDAgent(rewards=R)

  for episode in range(EPISODE_COUNT):
    observation = env.reset()
    start = observation

    for t in range(STEPS_PER_EPISODE):
      env.render()

      # take the next action
      action = agent.act(observation, reward, done)

      # step the environment using the selected action
      observation, reward, done, info = env.step(action)

      if done:
        print(f'Episode finished after {t+1} timesteps\n')
        history[start].append(t+1)
        done = False # reset for next episode
        break

  env.close()

  print('======Q-values:======')
  print(agent.Q)

  print('======Best paths:======')
  room_with_beer = 5
  for initial_state in range(room_with_beer+1):
    print(agent.best_path(initial_state))