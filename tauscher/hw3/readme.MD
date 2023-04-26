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
## cProfiling Results:## cProfiling Results:

Test for n=5000 Numbers.

         841886 function calls in 236.748 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5000    0.433    0.000  236.748    0.047 template_hw1.py:127(mysqrt)
   660435  236.064    0.000  236.064    0.000 template_hw1.py:6(isperfect)
     4928    0.240    0.000  234.757    0.048 template_hw1.py:54(getLowUpper)
   171522    0.011    0.000    0.011    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




         6125366 function calls in 6.646 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5000    0.167    0.000    6.646    0.001 template_hw1.py:178(mysqrt_opt)
     4928    0.281    0.000    6.415    0.001 template_hw1.py:90(getLowUpper_opt)
   660435    2.246    0.000    6.187    0.000 template_hw1.py:28(vec_isperfect)
   660435    0.268    0.000    2.060    0.000 <__array_function__ internals>:2(searchsorted)
   660435    1.881    0.000    1.881    0.000 {built-in method numpy.arange}
   660435    0.490    0.000    1.711    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
   660435    0.254    0.000    1.221    0.000 fromnumeric.py:1281(searchsorted)
   660435    0.202    0.000    0.968    0.000 fromnumeric.py:52(_wrapfunc)
   660435    0.697    0.000    0.697    0.000 {method 'searchsorted' of 'numpy.ndarray' objects}
   660435    0.081    0.000    0.081    0.000 fromnumeric.py:1277(_searchsorted_dispatcher)
   660435    0.068    0.000    0.068    0.000 {built-in method builtins.getattr}
   171522    0.011    0.000    0.011    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}




         5001 function calls in 0.004 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     5000    0.004    0.000    0.004    0.000 profile_mysqrt.py:33(npsqrt)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}






________________________________________________________________________________

## timeit Results:



50000 runs, timeit mysqrt

844.4759574430009

vs. proposed optimized solution

32.29419110199888

vs. numpy implementation

0.4124020120016212

________________________________________________________________________________
```

### Discussion of Results:
The test against numpy is not fair because the compiler most likely interprets the loop in which the function is called as an array, hence the native numpy sqrt-function is computed on all elements at once, whereas in our own implementation, most likely, for every for loop iteration a square root procedure is started. Nethertheless, we can see that the proposed optimization saves quite a lot of time. Most of the time is used for computing the isperfect() function, with 236 seconds. This is optimized to just 6 second using the vec_isperfect()-version of the function, that got rid of the for loop. So the proposed solution is nearly x36 faster.