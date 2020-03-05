from gym.envs.registration import register

register(
    id='fryshome-v0',
    entry_point='gym_fryshome.envs:FrysHomeEnv',
)

# register additional environments here