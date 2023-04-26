# Homework 3 

## Profiling the square-root code 

First I profiled the program with the number 505451.
During this I discovered my first mistake.
In HW1 i used `range(0,100)` to search for the first matching square root, obviously this is not working for bigger numbers and ended up stuck in a continous loop, so I changed it into `range(n)`. 
After fixing the mistake I could successfully calculate the root for the number 505451, but recognized a very long runtime.
I timed the runtime for the above command with the bash time command `time python template_hw1.py --n 505451` and it ran in 57,48 seconds in total.
Next, I used cProfile to further profile the runtime of the different functions. So I added `cProfile.runctx('mysqrt(input_n)', {'input_n': input_n, 'mysqrt': mysqrt}, {})` when executing the mysqrt-function. 

This returned the following time profile: 

```bash
time python template_hw1.py --n 505451
        1467 function calls in 28.798 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000   28.798   28.798 <string>:1(<module>)
    1    0.002    0.002   28.774   28.774 template_hw1.py:46(getLowUpper)
    1422   28.795    0.020   28.795    0.020 template_hw1.py:8(isperfect)
    1    0.000    0.000   28.798   28.798 template_hw1.py:82(mysqrt)
    40    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
    1    0.000    0.000   28.798   28.798 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


The input is n = 505451
Your square root of 505451 is 710.9507718541417
The numpy square root of 505451 is 710.9507718541419
The error precision is  1.1368683772161603e-13
All tests past.
Congratulation on achieving your first assignment.
python3.8 template_hw1.py --n 505451  57,48s user 0,31s system 100% cpu 57,498 total
```
So there were 1422 total calls to the isperfect-function which consumed 28.795 seconds from a total runtime of 28.798 seconds. So this function is using nearly all the time. The remaining time 57,498s - 28.798s = 28,7s are used to calculate the rest of the program.

The bottleneck function to change is the isperfect function.


## Approximation of the functions in Big O

isperfect: O(n) - best case finding the sqare-root: O(sqrt(n)), worst case: O(n)n 
getLowUpper: O(n²) or maybe O(sqrt(n) * n) - not quite sure, but the isupper has a runtime of n, which get called dependant on n times while not true
mysqrt: O(n²) or maybe O(sqrt(n) * n) - depends on the getLowerUpper because this is the most time consuming function (because of multiple calls to the isperfect function)


## Speeding up the bottleneck code


After replacing the for-loop from 
```python
for i in range(n) : # Hint: you can use the range, or any sequence type. if you don't remember how it works, have a look at the documentation.
    if i*i == n : # replace None by the appropriate code.
        return True, i
return False, n
```

to a vectorized calculation:
```python
# vector-based implementation 
vec = np.arange(n) # [0,1,2,3,4,...,n]
x = np.where(vec*vec == n, True, False)
if np.any(x):
    return True, vec[x][0]
```

I got the following time profile:
```bash
time python template_hw1.py --n 505451
         18531 function calls in 3.901 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1422    0.001    0.000    0.044    0.000 <__array_function__ internals>:177(any)
     1422    0.002    0.000    0.522    0.000 <__array_function__ internals>:177(where)
        1    0.000    0.000    3.901    3.901 <string>:1(<module>)
     1422    0.000    0.000    0.000    0.000 fromnumeric.py:2302(_any_dispatcher)
     1422    0.002    0.000    0.040    0.000 fromnumeric.py:2307(any)
     1422    0.003    0.000    0.037    0.000 fromnumeric.py:69(_wrapreduction)
     1422    0.001    0.000    0.001    0.000 fromnumeric.py:70(<dictcomp>)
     1422    0.000    0.000    0.000    0.000 multiarray.py:341(where)
        1    0.299    0.299    3.898    3.898 template_hw1.py:46(getLowUpper)
     1422    1.746    0.001    3.602    0.003 template_hw1.py:8(isperfect)
        1    0.000    0.000    3.901    3.901 template_hw1.py:82(mysqrt)
       40    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        1    0.000    0.000    3.901    3.901 {built-in method builtins.exec}
     1422    1.290    0.001    1.290    0.001 {built-in method numpy.arange}
     2844    0.523    0.000    0.563    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1422    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
     1422    0.033    0.000    0.033    0.000 {method 'reduce' of 'numpy.ufunc' objects}


The input is n = 505451
Your square root of 505451 is 710.9507718541417
The numpy square root of 505451 is 710.9507718541419
The error precision is  1.1368683772161603e-13
All tests past.
Congratulation on achieving your first assignment.
python3.8 template_hw1.py --n 505451  3,56s user 4,89s system 103% cpu 8,135 total
```

So the runtime of the mysqrt-function decreased from 28.798 seconds to 3.901 seconds.
The runtime of the whole program decreased from 57,498 seconds to 8,135 seconds. This is ~7 times faster than the original execution time.
