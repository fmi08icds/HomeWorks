# Runtime complexity
- hw2.isperfect: O(n)
  - worst case: we iterate over every i in range(n) and don't find a perfect square
- hw2.getLowUpper: O(n^2)
  - worst case: we have to call isperfect multiple time
  - this will not happen n times but it is upper bound by n
  - with some maths, one might be able to further restrict this
- hw2.mysqrt: O(n^2)
  - the most expensive operation is the call to getLowerUpper
  - the other while loop is much cheaper and can be neglected

# Runtime measure
- measuring code is found in time_hw3.py
- I tried measuring the time with the python time module
- outputs here are hard to reason about as they vary widely so I switched to using the profiler

# Profiling (hw2)
- for big ns isperfect takes the longest time
- I measure cumtime per call, because this does not exclude internal function calls, like tottime does and shows the time for only one call to the function
- one example output (n=100001) is found in profiler.txt, 
  - isperfect: 0.009s
  - getLowUpper: 0.418s
  - mysqrt: 0.379s
- for small ns (e.g. n=101) 0.000s are displayed for the functions and the setup and import code dominates

# Optimizations
- results are found in hw3.py
- 3 optimisations
  1. in isperfect: iterate up to n // 2 instead of n
  2. in isperfect: break when the square is bigger than n
  3. in mysqrt: removed unused iteration variable
  4. in mysqrt: no longer compute rst again as I did in hw2
  5. in isperfect: replaced loop by numpy functions


  # Optimized runtime (hw3 without optimization 5)
  hw3.isperfect: O(sqrt(n))
    - worst case: we break out of the loop after sqrt(n)
  hw3.getLowUpper: O(n*sqrt(n))
    - this function and hw3.mysqrt benefit from the improvements in hw3.isperfect
  hw3.mysqrt: O(n*sqrt(n))
