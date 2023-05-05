# ICDS FMI-08, Homework 4

Author: Ralf König
May 5th, 2023

# Task 1: Figure out what the code does

The non-vectorized code is in ``calc_pi.py`` in the function ``calculate_pi_non_vector(n)``. 
It was derived from ``template_hw2.py``.

The program uses a frequentist approach and does a simple Monte Carlo simulation 
(repeated m times) on the area under a function f. In f(), there is the circle formula with 
origin (0,0): ``x² + y² = r²``. `r` is the radius of the circle.

In each of the m=100 runs, it calculates a list of m=100 results.
In each of these m*m runs, it uniformly selects 1000 data points (x,y) in the square [0,0] - [r,r].
Then it checks, whether the data_point is inside the circle (under f) or not.
Then it counts those data points in the quarter circle and divides by the total number of data points.
This way, it gets the probability, that a data point in the square [0,0] - [r,r] is inside the 
quarter circle. Multiplied by 4, we get an approximation of pi.

Then it calculates mean and standard deviation of each of the m runs, getting m means.

Finally, it outputs a histogram for these means, which roughly represents a normal 
distribution around the mean = target value pi.

## Task 2: Provide a vectorized version of the function NoName() 

The non-vectorized code is in ``calc_pi.py`` in the function ``calculate_pi_vector(n)``. 

## Task 3: Time Analysis
*Compare the computational times of the vectorized to the non-vectorized version and report on it.*

A small benchmark application ``benchmark.py`` does 100 x 100 runs on 4 numbers of datapoints 
(125, 250, 500, 1000) in each run. The times in seconds are shown in the following table.

While the execution time of the non_vectorized implementation is roughly linear in n, 
the vectorized function is sublinear and has a speedup of roughly 25 to 100 in the 
selected range of benchmarks.

| n       | non_vector (s) | vector (s) |
|-------- |---------------|------------|
|   125   |   4.16954 |   0.17589 |
|   250   |   8.33799 |   0.19843 |
|   500   |  16.68414 |   0.26681 |
|  1000   |  34.70471 |   0.37352 |

