FROM lisaong/rpi-buster-tf2.0:1.1

RUN pip3 --no-cache-dir install \
  gym

# Install our example custom environment
# https://pip.pypa.io/en/stable/reference/pip_install/#git
RUN pip3 --no-cache-dir install -e \
  "git+https://github.com/lisaong/diec#egg=gym_fryshome&subdirectory=day4/rl/gym-fryshome"

WORKDIR "/code"

# Test
RUN python3 -c "import gym; print(gym.__version__); import gym_fryshome; print(gym_fryshome)"
