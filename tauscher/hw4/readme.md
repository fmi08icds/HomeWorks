## This is homework no. 4.


In this homework I describe the code given in the template_hw.py file. The description can be read in the code. Overall, the code simulates approximating pi with a monte carlo approach, where a point is either assigned to fall within the bounds of a circle or outside. Since the formular for the area of the circle contains pi, we can solve for pi and retrieve a numerical approximation for pi that way.

## Profiling and time complexity.

Below we find the cProfile and timeit analysis results. The simulation was run 2000 times with 100.000 points simulated per simulation.
These rather high values really showed the performance issues of the not-optimized version of the simulation. Where the not-optimized version took 11 minutes to complete, the optimized version just took 5 seconds, this is a speedup of x116 or two whole orders of magnitude. Also, the by looking at the number of function calls we can see that the not optimized code clearly needs > n*n calls just creating lists (557.087.449 calls, see {method 'append' of 'list' objects}), so its time complexity is at least O(c*n^2). Two bottlenecks of the unoptimized version clearly are sampling from the uniform distribution using the customized function uniform() aswell as the f() function that checks if a point is within the circle or not. These two functions have been radically improved upon by vectorization. The optimized version just calls different functions O(n) in linear time and is highly vectorized. One indicator of the proposed solution being quite good is that the 2nd highest time consuming call is generating the random numbers, which is already highly optimized by the numpy-library itself. To optimize further most likely is not impossible but might be impracticle or exceed the scope of the homework.

The timeit results, lastly, show a slightly lower performance increase by just x4. Most likely these measurements originate in the smaller number of simulation runs (500) and simulation sizes (100) chosen for this approach. A Graph would most likely show that with an increasing N (simulation size) the time of the non-optimized version rises quadratically whereas the optimized version would increase linearily.

```

## cProfiling Results:

Test for m=2000 times with n=100000 number of simulated points.

         1757091451 function calls in 657.687 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2000  185.615    0.093  657.687    0.329 template_hw2.py:30(pi_approximation)
400000000  119.827    0.000  248.043    0.000 template_hw2.py:13(uniform)
200000000  180.797    0.000  192.023    0.000 template_hw2.py:21(f)
400000000  128.216    0.000  128.216    0.000 {method 'random' of 'numpy.random.mtrand.RandomState' objects}
557087449   32.005    0.000   32.005    0.000 {method 'append' of 'list' objects}
200000000   11.225    0.000   11.225    0.000 {built-in method builtins.abs}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




         64006 function calls (64004 primitive calls) in 5.631 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     2000    3.355    0.002    5.631    0.003 template_hw2_optimized.py:28(pi_approximation_vec)
     2000    2.131    0.001    2.131    0.001 {method 'uniform' of 'numpy.random._generator.Generator' objects}
     2000    0.048    0.000    0.124    0.000 {numpy.random._generator.default_rng}
     2000    0.005    0.000    0.056    0.000 contextlib.py:72(inner)
     2000    0.028    0.000    0.028    0.000 {function SeedSequence.generate_state at 0x7f72e8181820}
     4000    0.009    0.000    0.022    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
     2000    0.003    0.000    0.020    0.000 <__array_function__ internals>:2(count_nonzero)
     4000    0.007    0.000    0.018    0.000 _ufunc_config.py:32(seterr)
     2000    0.003    0.000    0.014    0.000 _ufunc_config.py:433(__enter__)
     2000    0.002    0.000    0.014    0.000 numeric.py:424(count_nonzero)
     2000    0.012    0.000    0.012    0.000 {built-in method numpy.core._multiarray_umath.count_nonzero}
     2000    0.003    0.000    0.009    0.000 random.py:721(getrandbits)
     2000    0.002    0.000    0.009    0.000 <__array_function__ internals>:2(concatenate)
     2000    0.002    0.000    0.008    0.000 _ufunc_config.py:438(__exit__)
     4000    0.006    0.000    0.006    0.000 _ufunc_config.py:132(geterr)
     2000    0.005    0.000    0.005    0.000 {built-in method posix.urandom}
     4000    0.003    0.000    0.003    0.000 {built-in method numpy.seterrobj}
     2000    0.001    0.000    0.003    0.000 abc.py:96(__instancecheck__)
     2000    0.002    0.000    0.002    0.000 {built-in method _abc._abc_instancecheck}
     8000    0.002    0.000    0.002    0.000 {built-in method numpy.geterrobj}
     2000    0.001    0.000    0.001    0.000 {built-in method from_bytes}
     2000    0.001    0.000    0.001    0.000 {built-in method builtins.len}
     2000    0.001    0.000    0.001    0.000 numeric.py:420(_count_nonzero_dispatcher)
     2000    0.000    0.000    0.000    0.000 multiarray.py:143(concatenate)
     2000    0.000    0.000    0.000    0.000 contextlib.py:59(_recreate_cm)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.arange}
      2/1    0.000    0.000    0.000    0.000 abc.py:100(__subclasscheck__)
      2/1    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}








________________________________________________________________________________

## timeit Results:



500 runs, timeit mysqrt

0.10538769600043452

vs. proposed optimized solution

0.025843027000519214

________________________________________________________________________________

```



