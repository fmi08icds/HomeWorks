## Homework 3 - Proposing optimized Code

### 1. In this homework I propose a optimized version for finding a squareroot of any number. 
Especially, I optimized the first helper function (isperfect), so it does not perform a loop but a vectorized operation instead. 
* First, I limit the number of elements in my search-array to n+1/2 entries, since sqrt(n) > (n+1/2) for any n>=0.
* Then I simply square all the entries and perform a binary search on the result, since the array is sorted.
* Lastly, if the square of the element in the vector at index i equals n, n is a perfect root of i. 
* If the square of the element in the vector at index i does not equal n, it is not in the vector and thus n is not a perfect root.
* [Most likely the code could be optimized even more if one could improve the range of numbers to look at. (n+1)/2 might be a weak bound]

### 2. Regarding the timecomplexity:
The array is created in O(1) time.
It is searched trough with a binarysearch that typically has O(log(n)) time.
The lookup also happens in O(1) time, thus the proposed optimized helper function has a time complexity of O(log(n)).
The helper function is called several times (constant) within the updated getLowUpper() Function (now called getLowUpper_opt()), thus the time complexity does not change. 

### 3. Profiling Results

#### cProfiling & timeit Results:

```
## cProfiling Results:

Test for n=10000 Numbers.

         763660 function calls in 17.054 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   422540   16.047    0.000   16.047    0.000 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/template_hw1.py:6(isperfect)
    10000    0.839    0.000   17.054    0.002 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/template_hw1.py:130(mysqrt)
     9686    0.146    0.000   15.855    0.002 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/template_hw1.py:57(getLowUpper)
   321433    0.022    0.000    0.022    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




         4143980 function calls in 3.252 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   422540    1.019    0.000    2.773    0.000 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/template_hw1.py:31(vec_isperfect)
   422540    0.578    0.000    0.578    0.000 {built-in method numpy.arange}
   422540    0.398    0.000    0.398    0.000 {method 'searchsorted' of 'numpy.ndarray' objects}
    10000    0.292    0.000    3.252    0.000 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/template_hw1.py:181(mysqrt_opt)
   422540    0.272    0.000    0.981    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
     9686    0.169    0.000    2.865    0.000 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/template_hw1.py:93(getLowUpper_opt)
   422540    0.151    0.000    1.176    0.000 <__array_function__ internals>:2(searchsorted)
   422540    0.151    0.000    0.710    0.000 /home/jonny/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py:1281(searchsorted)
   422540    0.120    0.000    0.559    0.000 /home/jonny/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py:52(_wrapfunc)
   422540    0.043    0.000    0.043    0.000 /home/jonny/.local/lib/python3.8/site-packages/numpy/core/fromnumeric.py:1277(_searchsorted_dispatcher)
   422540    0.041    0.000    0.041    0.000 {built-in method builtins.getattr}
   321433    0.019    0.000    0.019    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




         10001 function calls in 0.009 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    10000    0.009    0.000    0.009    0.000 /home/jonny/Documents/Uni Leipzig/Intro to Computer Science/HomeWorks/tauscher/hw3/profile_mysqrt.py:32(npsqrt)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}






________________________________________________________________________________

## timeit Results:



25000 runs, timeit mysqrt

43.19598458800101

vs. proposed optimized solution

6.585698725999464

vs. numpy implementation

0.19895551000081468

________________________________________________________________________________
```

### Discussion of Results:
The test against numpy is not fair because the compiler most likely interprets the loop in which the function is called as an array, hence the native numpy sqrt-function is computed on all elements at once, whereas in our own implementation, most likely, for every for loop iteration a square root procedure is started. Nethertheless, we can see that the proposed optimization saves quite a lot of time. Most of the time is used for computing the isperfect() function, with 16 seconds. This is optimized to just 1 second using the vec_isperfect()-version of the function, that got rid of the for loop. Overall the proposed solution is 33x slower than the numpy implementation but the template solution is 217x times slower than that. Quite an improvement with just little adjustments. 