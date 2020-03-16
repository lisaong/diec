FROM lisaong/rpi-buster-tf2.0:1.1

RUN pip3 --no-cache-dir install \
  gym

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     python3-matplotlib

RUN  apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install our example custom environment
# https://pip.pypa.io/en/stable/reference/pip_install/#git
# VCS installs will create an egg-link, use /tmp as clone root
WORKDIR "/tmp"
RUN pip3 --no-cache-dir install -e \
  "git+https://github.com/lisaong/diec#egg=gym_fryshome&subdirectory=day4/rl/gym-fryshome"

RUN pip3 --no-cache-dir install -e \
  "git+https://github.com/lisaong/diec#egg=gym_jobshop&subdirectory=day4/rl/gym-jobshop"

# Test
RUN python3 -c "import gym; print(gym.__version__); \
  import gym_fryshome; print(gym_fryshome); \
  import gym_jobshop; print(gym_jobshop);"

WORKDIR "/code"
