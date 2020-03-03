#
# Demonstration of using PyGMO to solve the Job Shop Scheduling problem.
# Refer to pygmo_scheduling.ipynb for more explanation.
# (https://en.wikipedia.org/wiki/Job_shop_scheduling)
#

import pygmo as pg
import numpy as np

# constants for accessing the tuples
JOB = 0
MACHINE = 1
DURATION = 2

class jobshop_function:
  def __init__(self, jobs, max_schedule_time=20):
    """ jobs: list of jobs (job_id, machine_id, duration)
        max_schedule_time: maximum time allowed for the schedule
    """
    self.jobs = jobs_list
    self.dim = len(jobs_list)
    self.t_max = max_schedule_time
    self.t_min = 0

    self.job_start_indices = []
    for i in range(1, self.dim):
      if self.jobs[i-1][JOB] != self.jobs[i][JOB]:
        self.job_start_indices.append(i)
    self.machines_count = 1 + max(job[MACHINE] for job in jobs)

  def fitness(self, x):
    """The fitness: the objective to minimize and any constraints
    x: contains the start times
    """
    # Compute the objective:
    # the length of time from the earliest start time of the jobs to the
    # latest end time
    start_times = x # code readability
    end_times = [job[DURATION]+s for job, s in zip(self.jobs, start_times)]
    objective = max(end_times) - min(start_times)
    assert(objective > 0)

    # Compute the constraints:
    # 1) Precedence: for any two consecutive tasks in the same job, the first must 
    # be completed before the second can be started
    #
    # Say we have 3 tasks with their start and end times:
    #   (s1, e1), (s2, e2), (s3, e3)
    # Check that:
    #   s1 >= 0, s2 >= e1, s3 >= e2
    # If any of these are FALSE, the constraint is not met

    # Compute the prev task's end times, initializing end times to
    # -1 for the first task of each job
    # (-1 is used instead of 0 to allow for start times at 0)
    prev_end_times = np.array([-1] + end_times[:-1])
    prev_end_times[self.job_start_indices] = -1

    # Count how many times the constraint is not met
    # (i.e. when prev task's end time exceeds next task's start time
    violate_precedence = float(sum((prev_end_times - start_times) > 0))

    # 2) No overlap: a machine can't work on two tasks at the same time.
    # Say we have 2 tasks on the same machine with their start and end times,
    # where the start times are sorted
    #   (s1, e1), (s2, e2)
    # Check that e1 <= s2. We can do this by sorting first by start times,
    # then flattening the tuples out to make sure that the values are sorted
    #
    # Extract tasks assigned to each machine, their start and end times
    tasks_by_machines = {machine:[] for machine in range(self.machines_count)}
    for i in range(self.dim):
      tasks_by_machines[self.jobs[i][MACHINE]].append(
          (start_times[i], end_times[i]))

    # sort by start time, then compute whether overlap happens
    # none of the numbers should overlap
    overlap = 0.
    for machine in tasks_by_machines.keys():
      tasks_by_machines[machine].sort(key=lambda t:t[0]) # inplace sort
      flattened = np.array([t for ts in tasks_by_machines[machine] for t in ts])
      # overlap means previous value exceeds the next value
      overlap += float(sum(flattened[:-1] > flattened[1:]))

    # subtract the earliest start time to get the makespan
    return [objective, violate_precedence, overlap]

  def get_bounds(self):
    """The bounds of the vector
    """
    return ([self.t_min] * self.dim,[self.t_max] * self.dim)

  def get_nix(self):
    """Returns the number of integer dimensions"""
    return self.dim

  def get_nec(self):
    """The number of equality constraints:
    1 no-overlap constraint
    1 precedence constraint
    """
    return 2

  def get_extra_info(self):
    return f'\tDimensions: {self.dim} \
      \n\tJobs: {self.jobs} \
      \n\tSchedule Limit: {self.t_max}'

if __name__ == "__main__":

    # Each job is a list of multiple tasks: (machine_id, processing_time)
    jobs_data = [
      [(0, 3), (1, 2), (2, 2)],  # Job0
      [(0, 2), (2, 1), (1, 4)],  # Job1
      [(1, 4), (2, 3)]  # Job2
    ]

    # Flatten the jobs data by index by encoding the job_id into the tuple
    # the *task syntax will unpack a tuple
    jobs_list = [(i, *task) for i in range(len(jobs_data)) for task in jobs_data[i]]

    # Create the problem
    prob = pg.problem(jobshop_function(jobs=jobs_list), max_schedule_time=12)
    print(prob)

    # Optimise
    population_size = 1000
    iterations = 100
    pop = pg.population(prob, size=population_size, seed=123)
    algo = pg.algorithm(pg.gaco(gen=iterations, ker=population_size, seed=123))
    algo.set_verbosity(1000)
    pop = algo.evolve(pop)

    print(f'solution: {pop.champion_x}, fitness value: {pop.champion_f}')
