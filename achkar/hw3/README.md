# HW3

## Code Profiling Results:

### **mysqrt(100000)**
682 function calls in 9.935 seconds

Ordered by: internal time

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function)                                                                                                       |
|--------|---------|---------|---------|---------|------------------------------------------------------------------------------------------------------------------------------|
| 634    | 9.932   | 0.016   | 9.932   | 0.016   | /Users/pierreachkar/Downloads/HomeWorks/achkar/hw3/hw2.py:4(isperfect)                                                        |
| 1      | 0.004   | 0.004   | 9.920   | 9.920   | /Users/pierreachkar/Downloads/HomeWorks/achkar/hw3/hw2.py:28(getLowUpper)                                                      |
| 1      | 0.000   | 0.000   | 9.935   | 9.935   | /Users/pierreachkar/Downloads/HomeWorks/achkar/hw3/hw2.py:61(mysqrt)                                                           |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/pstats.py:108(__init__)                                      |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/pstats.py:118(init)                                          |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/pstats.py:137(load_stats)                                   |
| 38     | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.abs}                                                                                                 |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/cProfile.py:50(create_stats)                                |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.isinstance}                                                                                          |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.hasattr}                                                                                             |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.len}                                                                                                 |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {method 'disable' of '_lsprof.Profiler' objects}                                                                               |

### **np.sqrt(100000)**

8 function calls in 0.000 seconds

Ordered by: internal time

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function) |
|--------|---------|---------|---------|---------|--------------------------|
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/pstats.py:108(__init__) |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/pstats.py:137(load_stats) |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/pstats.py:118(init) |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/cProfile.py:50(create_stats) |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.isinstance} |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.len} |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {built-in method builtins.hasattr} |
| 1      | 0.000   | 0.000   | 0.000   | 0.000   | {method 'disable' of '_lsprof.Profiler' objects} |

---

## Interpretation:

Based on the profiling results, it is clear that the ```mysqrt``` function is much slower than ```np.sqrt``` when calculating the square root of 100,000.

The ```mysqrt``` function takes almost 10 seconds to execute and makes 682 function calls, whereas ```np.sqrt``` takes only 0.000 seconds and makes only 8 function calls. It appears that the function ```isperfect()``` in ```mysqrt``` is the function that consumes the most time, 9.932 seconds out of a total of 9.935 seconds. This indicates that the function is implemented inefficiently. 

---
## Time complexity:

```isperfect()``` 
- The if statement at the beginning takes constant time, *O(1)*.
- The for loop has n iterations, so it takes *O(n)* time.

&rarr; *The total time complexity of this function is O(n).*

``` getLowUpper()``` 

- The while loop that iterates until low[0] is True has at most n iterations, so it takes *O(n)* time.
- The same applies to the while loop that iterates until upper[0] is True.
- The rest of the function consists of constant-time operations

&rarr; *The total time complexity of this function is O(n).*

``` mysqrt()``` 

- The first if statement takes constant time, *O(1)*.
- The second if statement calls the ```isperfect()``` function, which takes *O(n)* time.
- Calling the ``` getLowUpper()``` function takes also *O(n)*.
- The ```while```  a loop that runs until a condition is met, and it performs constan time operations inside the loop body. The loop runs at most *log(n)* times (because the interval between minsqrt and maxsqrt is halved at each iteration), so it takes *O(log n)* time.

&rarr; *The total time complexity of ``` mysqrt()```  is O(n) + O(log n) = O(n).*

&rArr; Therefore, the overall time complexity of is ***O(n)***.

---

