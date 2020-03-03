# Swarm Computing Applications in Edge Computing

## Job Shop Scheduling

Explanation of the problem: [Colab Notebook](pygmo_scheduling.ipynb)

Running on Raspberry Pi 3 or 4:
1. Launch the Docker container 
```
cd docker
sh launch_docker.sh
```

2. From the Docker container:
```
# Activate the virtual environment, then run the script
. bin/activate
cd /code/day3/swarm
python3 pygmo_demo.py
```

Output should look like this:
```
(app) root@8b08123ad4e1:/code/day3/swarm# python3 pygmo_demo.py
Problem name: <class '__main__.jobshop_function'>
        Global dimension:                       8
        Integer dimension:                      8
        Fitness dimension:                      3
        Number of objectives:                   1
        Equality constraints dimension:         2
        Inequality constraints dimension:       0
        Tolerances on constraints: [0, 0]
        Lower bounds: [0, 0, 0, 0, 0, ... ]
        Upper bounds: [12, 12, 12, 12, 12, ... ]
        Has batch fitness evaluation: false

        Has gradient: false
        User implemented gradient sparsity: false
        Has hessians: false
        User implemented hessians sparsity: false

        Fitness evaluations: 0

        Thread safety: none

Extra info:
        Dimensions: 8
        Jobs: [(0, 0, 3), (0, 1, 2), (0, 2, 2), (1, 0, 2), (1, 2, 1), (1, 1, 4), (2, 1, 4), (2, 2, 3)] 
        Schedule Limit: 12

   Gen:        Fevals:          Best:        Kernel:        Oracle:            dx:            dp:
      1              0              7           1000              0             39        6.99829

solution: [ 3.  6. 11.  1.  6.  9.  2.  7.], fitness value: [12.  0.  0.] (43.820 seconds)
```
