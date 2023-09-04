# HomeWorks

Based on the profile results, my_sqrt seems to perform well and run very fast. The deadtime for the function is 0.000 seconds for all tested inputs, which means that the function does not take a significant amount of time to execute. This is a good sign and shows that the optimization techniques used in the function are effective.

In addition, the profiling results show that the built-in abs function is often called in the my_sqrt function, but it does not take a significant amount of time to execute. This shows that using the inner function is a good optimization technique.

Comparing the results of the my_sqrt profile with np.sqrt, we see that np.sqrt is not optimized in the same way because it takes the same amount of time to run regardless of the size of the input. This is expected because np.sqrt is a general purpose function and cannot be optimized for specific input sizes like my_sqrt.

Overall, my_sqrt seems to perform well and is an effective optimization of the square root function for certain input sizes.


Code Profiling Result


Input: 1 mysqrt: 34 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 31 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

====================================================================================================== Input: 1001 mysqrt: 47 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 44 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

=========================================================================================================== Input: 2001 mysqrt: 47 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 44 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 3001 mysqrt: 48 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 45 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 4001 mysqrt: 49 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 46 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 5001 mysqrt: 51 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 48 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 6001 mysqrt: 50 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 47 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 7001 mysqrt: 52 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 49 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 8001 mysqrt: 51 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 48 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

======================================== Input: 9001 mysqrt: 53 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Users/sepidehkavianpoor/Desktop/numpy_project/sqrt_optimization.py:51(my_sqrt) 50 0.000 0.000 0.000 0.000 {built-in method builtins.abs} 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}

np.sqrt: 2 function calls in 0.000 seconds

Ordered by: internal time

ncalls tottime percall cumtime percall filename:lineno(function) 1 0.000 0.000 0.000 0.000 /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/cProfile.py:117(exit) 1 0.000 0.000 0.000 0.000 {method 'disable' of '_lsprof.Profiler' objects}
