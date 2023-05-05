# Homework 2 - Estimate the Value of PI

## Description

The Code calculates an estimation of PI.

The NoName()-function is calculting the ratio of random uniformly sampled points from the interval 0 to 1 [0, 1] lying inside the circle with radius 1 to all points N. This ratio is multiplied by 4 to estimate Pi.

A = pi * r²  
r = 1:  
A = pi * 1²  
A = pi  

By increasing N and M the estimation gets closer to the real number of pi.


## Code Profiling - Unvectorized vs. vectorized version

### Unvectorized

```
 20000000    3.888    0.000    8.549    0.000 template_hw2.py:10(uniform)
 10000000    5.400    0.000    5.717    0.000 template_hw2.py:13(f)
    10000    5.632    0.001   20.841    0.002 template_hw2.py:16(estimate_pi)
        1    0.001    0.001   24.108   24.108 template_hw2.py:51(main)
      100    0.121    0.001   20.962    0.210 template_hw2.py:62(<listcomp>)
   ```

The estimate_pi()-function is called M*M (10000) times and takes 5.632 seconds to run.  

### Vectorized

```
    10000    0.031    0.000    0.037    0.000 template_hw2.py:13(f)
    10000    0.095    0.000    0.524    0.000 template_hw2.py:16(estimate_pi)
        1    0.000    0.000    2.597    2.597 template_hw2.py:51(main)
      100    0.005    0.000    0.530    0.005 template_hw2.py:62(<listcomp>)
```

The estimate_pi()-function is called M*M (10000) times and takes 0.095 seconds to run.  

-> the vectorized version is 59,28 times faster than the initial implementation