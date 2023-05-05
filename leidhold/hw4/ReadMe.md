# Homework 4

## Description of the Code

The delivered python code is approximating the value of the circular number PI by applying the Monte Carlo Simulation supported by the law of large numbers. It generates N pairs of random points in a unit square and checks, if the point lies inside a quarter-circle of radius R=1. The ratio of points that lies inside the quarter-circle to the total number of generated points is generated and it approximates the value of pi as 4 times the ratio.

### Getting started

`pip install numpy matplotlib`

`pip install numpy`

### Function Description

The `uniform()` function takes two arguments a and b and returns a random float between 0 and 1 by using the numpy package and shifts it to the desired range.

The function `f()` is calculating the distance of a point from the origin. So if the point is less or equal to R it lies inside the quarter-circle.

The `simulatePI()` function is mainly approximating PI by using the Monte Carlo simulation. It generates N random points inside a specific range from 0 to 1, calculates the distance from each point to the origin and if the point lies inside the quarter-circle it is accepted. The approximation of Pi is given by 4 times the ratio of accepted to generated points.

The `main()` function defines the amount of simulations M and the number of generated points N for each simulation M. For each simulation the mean and standard deviation is calculated. The end result is plotted in a histogram. This is also called LAW OF LARGE NUMBERS, which says that the average of results obtained from a large number of trials is close to the expected value.

## Optimization by Vectorization

The original code used a for loop to generate the random points and check whether they were inside the circle or not. This can be slow for large number of N, because the loop is executed N times.

To optimize the code numpy broadcasting was used to generate the random points in one go, and then use boolean indexing to check which points are inside the circle. For this the NumPy package the function `np.random.uniform()` was used to get N uniform distributed random points. Furthermore the vectorized comparison operation `is_inside = list_y < f(list_x,R)` is checking wether the point is inside the quarter-circle. In the main() function the simulatePI() function is called M times by using `np.array()`. The mean and the standard deviation are calculated through `np.mean()` and `np.std()`.


## Performance Analysis

With `import time` the computational time was measured before and after broadcasting:
- Execution time before: 25.006057024002075 seconds
- Execution time after: 0.2703533172607422 seconds

For more detailed information I used the cProfile to measure the performance and identify the most time consuming and called functions. The profiler is ran on the `main()` function. Here the cumtime of the optimized function simulatePi() is taking 0.321 seconds, while the old function took 48.915 seconds. This is depending mainly on the improving of calls from 10000 to 1000. But as well the computational time per call was reduced significantly by using vectorization.
The results of the Profiling can be found in the cProfile [output_time file](./output_time.txt/) and [output_calls file](./oldoutput_time.txt).

## Conclusion

As we can see after profiling the vectorized code, the number of calls and the computational time decreased. So we successfully improved the algorithm by applying vectorization with the help of pythons NumPy package. But for the same amount of generated points N and simulations M a loss of  precision of Pi is obtained. So to avoid a worse simulation of Pi, more points and simulations need to be done. This leads still to a better time and simulated Pi is again closer to its real value.

