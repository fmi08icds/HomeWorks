1.) What is the time complexity of a recursive implementation of the Fibonacci series?

In a recursive implementation of the Fibonacci series, the time complexity is O(2^n), where 'n' represents the number we want to calculate in the series. The algorithm computes each Fibonacci number by recursively calling the two previous Fibonacci numbers. As a result, each function call generates two additional function calls. This exponential growth in the number of function calls leads to a time complexity of O(2^n) as the input size increases. Consequently, the recursive approach becomes inefficient for larger values of 'n'.

2.) How does our square root algorithm perform in terms of time complexity?

The 'isperfect(n)' function, which contains a loop iterating over 'n' values, has a time complexity of O(n).

The 'getLowUpper(n)' function invokes the 'isperfect(n)' function twice with different 'n' values. As a result, its time complexity is also O(n).

The 'mysqrt(n)' function comprises three parts:

A constant-time check for 'n' being equal to 0 or 1.
A call to the 'isperfect(n)' function, which has a time complexity of O(n).
A loop that continues until an error threshold is met. The number of iterations required for this loop depends on the value of 'n', leading to a time complexity of O(log(n)).
Considering the parts together, the overall time complexity of the square root program is O(n). Despite the loop in the 'mysqrt(n)' function having a time complexity of O(log(n)), the dominant factor affecting the entire code is the call to 'isperfect(n)', which has a time complexity of O(n).

3.) How can we improve the code's time complexity?

To enhance the time complexity, we can adopt a more efficient algorithm for finding perfect squares. For instance, using binary search would provide a time complexity of O(log(n)). By implementing this improvement, we can modify the 'isperfect(n)' function, which is called multiple times by the 'getLowUpper(n)' and 'mysqrt(n)' functions (Lines 24-33).

After profiling the code using the 'cProfile' (cProfile.run('mysqrt(12345)')) module, we observe a notable reduction in execution time:
    265 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 test1234.py:34(getLowUpper)
      224    0.001    0.000    0.001    0.000 test1234.py:5(isperfect)
        1    0.000    0.000    0.001    0.001 test1234.py:67(mysqrt)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects

Additionally, the code's execution speed was measured using the 'timeit' module:
elapsed_time = timeit.timeit(lambda: mysqrt(1234), number=1000)
print("Elapsed time:", elapsed_time)

Result of the original version of the code:
"Elapsed time: 6.782756900007371"

Result of the improved code:
"Elapsed time: 0.1983786000055261"

This significant improvement demonstrates the benefits of optimizing algorithms to achieve better performance. By employing more efficient algorithms, we can reduce time complexity and enhance the overall efficiency of our programs.




