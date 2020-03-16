# Reinforcement Learning on Edge Computing

## Path Finding with OpenAI Gym on Raspberry Pi

![image](path_finding/path_finding_intro.png)

(Inspiration: http://mnemstudio.org/path-finding-q-learning-tutorial.htm, Futurama)

Explanation of the problem: [Colab Notebook](path_finding/path_finding_demo.ipynb), [Q-Learning Intro Slides](https://github.com/lisaong/diec/blob/master/day4/rl/some%20intro%20slides.pdf)

Running on Raspberry Pi 3 or 4:
1. Launch the Docker container 
```
cd day4/rl/docker
sh launch_docker.sh
```

2. From the Docker container:
```
cd /code/day4/rl/path_finding
python3 path_finding_demo.py
```

Output should look like this:
```
...
Action: 3, next state: 3, all actions: [1 2 4], all future rewards: [ 96.27421912  50.38468669 104.93536212], max future reward: 104.935
Current room: 3, Reached goal: False
Action: 1, next state: 1, all actions: [3 5], all future rewards: [ 66.09247435 132.5242206 ], max future reward: 132.524
Current room: 1, Reached goal: False
Action: 5, next state: 5, all actions: [1 4 5], all future rewards: [43.43638317 54.1499565  74.79296194], max future reward: 74.793
Episode finished after 12 timesteps

======Q-values:======
[[  0.           0.           0.           0.         104.8319749
    0.        ]
 [  0.           0.           0.          66.09247435   0.
  135.25523549]
 [  0.           0.           0.          73.19306276   0.
    0.        ]
 [  0.          97.24873486  50.38468669   0.         104.93536212
    0.        ]
 [ 71.78041677   0.           0.          70.00207955   0.
  142.44007268]
 [  0.          43.43638317   0.           0.          54.1499565
   74.79296194]]
======Best paths:======
[0, 4, 5]
[1, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5, 5]
```

## Job Shop Scheduling with OpenAI Gym on Raspberry Pi

![image](../../day3/swarm/job_shop_scheduling.png)

Running on Raspberry Pi 3 or 4:
1. Launch the Docker container 
```
cd day4/rl/docker
sh launch_docker.sh
```

2. From the Docker container:
```
# Install the gym environment, then run the script
cd /code/day4/rl/jobshop
python3 jobshop_scheduling_demo.py
```

Number of successful episodes for 20000 iterations using QLearning:
![history](jobshop/QLearningTDAgent_20000.png)

Each episode begins with a clean slate, where 8 tasks (for 3 jobs) are to be scheduled on 3 machines. The tasks must run on its assigned machine, and in the specified order in the job.

The episode starts with an action. For example, schedule task_id=3 at start_time=8. 

If a task is scheduled without errors (i.e. no overlap, no out of order tasks), the reward is positive (e.g. 600):
```
======Episode 9999======
Action: OrderedDict([('task_id', 3), ('start_time', 8)]), State: {'is_scheduled': [0, 0, 0, 1, 0, 0, 0, 0]}, Reward: 600, Done: False, Info: {'makespan': 2}
Job-view:
0: Job: 0, Machine: 0, Start: 0, End: -1
1: Job: 0, Machine: 1, Start: 0, End: -1
2: Job: 0, Machine: 2, Start: 0, End: -1
3: Job: 1, Machine: 0, Start: 8, End: 10
4: Job: 1, Machine: 2, Start: 0, End: -1
5: Job: 1, Machine: 1, Start: 0, End: -1
6: Job: 2, Machine: 1, Start: 0, End: -1
7: Job: 2, Machine: 2, Start: 0, End: -1

Machine-view:

Machine 0:
|----|----
        33

Machine 1:
idle

Machine 2:
idle

```

When a task is scheduled with errors (e.g. machine overlap, or out-of-sequence tasks), the reward is negative (-1) and the episode is done:
```
Action: OrderedDict([('task_id', 7), ('start_time', 2)]), State: {'is_scheduled': [1, 0, 1, 1, 1, 0, 0, 1]}, Reward: -1, Done: True, Info: {'makespan': 8, 'errors': 'Machine Overlap'}
Job-view:
0: Job: 0, Machine: 0, Start: 2, End: 5
1: Job: 0, Machine: 1, Start: 0, End: -1
2: Job: 0, Machine: 2, Start: 7, End: 9
3: Job: 1, Machine: 0, Start: 8, End: 10
4: Job: 1, Machine: 2, Start: 3, End: 4
5: Job: 1, Machine: 1, Start: 0, End: -1
6: Job: 2, Machine: 1, Start: 0, End: -1
7: Job: 2, Machine: 2, Start: 2, End: 5

Machine-view:

Machine 0:
|----|----
  000   33

Machine 1:
idle

Machine 2:
|----|---
  777
   4   22
Episode finished after 5 actions

```

When all episodes are complete, the best schedule based on Q-values stored in the agent will be printed. Note that this schedule can still result in errors when the agent has not learnt an optimum policy (aka the objective of reinforcement learning!)

Temporal Differencing Q-Learning for single-agent seems too naive to learn the optimum policy quickly, as it averages less than 1% passing rate for this experiment. It is still slightly better than the baseline (RandomAgent), which has 0% passing rate.

Other experiments to try: Multi-agent learning, Deep Q-learning

```

Passing rate: 57.03%

*********Best Schedule*********
Makespan: 3, Errors: None
Makespan: 21, Errors: None
Makespan: 21, Errors: Makespan Exceeded
Makespan: 21, Errors: Makespan Exceeded
Makespan: 21, Errors: Out-of-sequence tasks
Makespan: 21, Errors: Makespan Exceeded
Makespan: 25, Errors: Out-of-sequence tasks
Makespan: 26, Errors: Out-of-sequence tasks
Job-view:
0: Job: 0, Machine: 0, Start: 8, End: 11
1: Job: 0, Machine: 1, Start: 20, End: 22
2: Job: 0, Machine: 2, Start: 12, End: 14
3: Job: 1, Machine: 0, Start: 1, End: 3
4: Job: 1, Machine: 2, Start: 21, End: 22
5: Job: 1, Machine: 1, Start: 22, End: 26
6: Job: 2, Machine: 1, Start: 23, End: 27
7: Job: 2, Machine: 2, Start: 19, End: 22

Machine-view:

Machine 0:
|----|----|
 33     000

Machine 1:
|----|----|----|----|----|-
                    115555
                       6666

Machine 2:
|----|----|----|----|-
            22     777
                     4
```
