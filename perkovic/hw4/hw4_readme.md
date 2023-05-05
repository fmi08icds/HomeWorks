# README

## Monte Carlo Simulation to Approximate the Value of Pi

This python program performs a Monte Carlo simulation to approximate the value of Pi. It creates random (x,y) pairs within a radius 1 circle and computes the ratio of the number of points within the first quadrant of the circle to the total number of points generated, which is used to approximate the value of Pi. This process is repeated several times, which then computes the mean and standard deviation of the estimated Pi values and produces a histogram of the mean values.

## Performance

Running the program with cProfile on the old and optimized code produces the following results:

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function) |
|--------|---------|---------|---------|---------|---------------------------|
| 1      | 0.000   | 0.000   | 9.742   | 9.742   | hw4_vectorized.py:28(main) |
| 1      | 0.000   | 0.000   | 48.656  | 48.656  | template_hw2.py:58(main)   |


We see that the new vectorized version of the Monte Carlo simulation to estimate the value of Pi is almost 5 times faster in processing the code. The optimized implementation uses NumPy arrays and is much faster than the original implementation.
