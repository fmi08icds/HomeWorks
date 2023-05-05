## HW4

The function in question produces an estimation of pi. If N is increased the accuracy of the estimation is higher.

## Vectorizing

By vectorizing the creation of the two arrays and the comparison between them the function performs significantly better. The vectorized function only takes a fraction of the time that the initial function took it is roughly 148x faster (in tottime). Of course when we look at the cumulative time this effect is not as huge on my system as f still takes allot of time. But still we have even then the function is 3x as fast in vectorized form.

Here is the relevant output of both functions: 
    ncalls  tottime percall cumtime percall filename:lineno(function)
    10000   20.704  0.002   66.121  0.007   hw4.py:24(estimate_pi)
    10000   0.139   0.000   21.155  0.002   hw4.py:55(estimate_pi_vectorized)

