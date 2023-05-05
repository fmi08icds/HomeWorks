# Homework 4

## Step 1: Figure out what the function `NoName` does

The function `NoName` in the original code example (see `original.py`), is uniformly sampling `N` random points in a square and counting how many points are in a quarter-circle inside this square. The square has a side length of 1 and the circle also has a radius of 1. Since the probability of a random point lying inside the quarter-circle is equal to a quarter of the circle's area, the resulting ratio assigned to `fin` is approximately $\frac{\pi}{4}$. This number is multiplied by 4 which means that the function `NoName` approximates the surface area of a circle with a radius of 1, i. e., $A = \pi r^2 = \pi$. This method is known as Monte-Carlo simulation.

## Step 2: Provide a vectorized version of this function

The vectorized version of the program can be found in the script file `optimized.py`. 

As a small challenge, I tried to come up with the most compact (in regards to lines of code) version that does exactly the same thing as the original program. This code golfing experiment can be found in `optimized_bonus.py`.

## Step 3: Compare computionational times

To compare the runtimes of the original (non-vectorized) and vectorized implementation, the scripts were analyzed using `cProfile`. The output of `cProfile` shows the total time that was spent in the function `NoName` is **17.5 seconds** while the function `approximate_area` only needs **120 milliseconds** in total. This means that the vectorized implementation is more than 100 times faster than the non-vectorized version.

```
> python3 -m cProfile original.py | grep "NoName"
   
   ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
    10000   17.570    0.002   55.129    0.006 original.py:16(NoName)
```

```
> python3 -m cProfile optimized.py | grep "approximate"

   ncalls  tottime  percall  cumtime  percall filename:lineno(function) 
    10000    0.119    0.000    0.640    0.000 optimized.py:10(approximate_area)
```

