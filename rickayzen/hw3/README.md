## Homework 3
### Structure
The doc-folder contains the files "new_performances.txt" and "old_performances.txt" which describe the runtime O of the functions. This has been calculated by going through how many operations there are, how often the functions get called and how often the loops get iterated through.

The code itself can be found in the src-folder. "hw2.py" contains the old version and "hw3_improved.py" contains the new version.

Both functions have be altered to count the number of operations and return them. 

The "performance_test.py" script executes a performance test of the functions and saves the profiled stats by cProfiler in "perf.stats".
### Improved function
The improved function was improved by replacing the isperfect function with a similar function. Instead of just checking if the number is a perfect square and just returning n if not, it will now always return the closest integer whose square is smaller or equal to n. The function does not return a boolean anymore because that can be simply checked by squaring the result and comparing it with the input.
<br>
Furthermore, as the function returns the highest integer whose square is ≤ n, the upper bound can be simply calculated by adding 1. 
<br>
Through this, the getLowUpper function has been made redundant and instead of countless isperfect calls, the new function will only be called once at the start.

### Theoretical runtimes
In the two txt-files the theoretical Big O runtime gets calculated. This is done by explicitly counting the number of operations in each function.  
### Performance test
The performance test can perform two tasks:
* Executing the performance test
* Displaying the stats of "perf.stats"

You can ignore the performance test by adding the argument `--p` and ignore the stats by adding the argument `--s`.
<br>
E.g. `python performance_test.py --p` will only display the results.
<br>
When executing the test you can also enter the argument `--t int` to set the timeout time. 
<br>
With the optional argument `--t float` it is also possible to set the precision of the result.
#### Execution of performance test
For the test, the functions get tested for the numbers in the following array: [101, 501, 1001, 5001, 10001, 50001, 100001, 500001, 1000001, 5000001, 10000001, 50000001, 100000001, 500000001] (The numbers were chosen to avoid perfect squares.)
<br>
For each number three functions get tested: the benchmark numpy.sqrt(), the old function and the improved function where for each function a timeout will occur after the inputted time. Default is 10 seconds.
<br>
For all functions the computation time will be printed out and for the old and new version the number of operations will be displayed. 
<br>
If a function (mainly the old version) can't compute a number, the following numbers will be skipped. If both the old version as well as the new version fail to compute a number in the given timeframe, the test concludes.
<br>
As long as both functions are computing a number, cProfiler will track the profiling data and save them in "perf.stats".

### Displaying the stats
The stats of the old and the new function are printed out separately by using `pstats.print_callee()`. It shows how often the functions in the main function were called and how much time they consumed. However, for the improved function it always displays a time of 0 - probably because the main computation happens directly in the main function.

## Results
According to "old_performance.txt", a runtime of O(n*sqrt(n)) is expected and for the improved version the runtime should be O(sqrt(n)) (see new_performance.txt). However, both rely on an unknown variable because it is unclear and dependent on the error threshold how often the last loop gets iterated through.
<br>
By altering the error threshold of the performance test between the default value and extremely large numbers (e.g. 10000) where it shouldn't have an impact on the runtime anymore it seems that the unknown variable results in roughly 0-200 operations for both functions independently of the size of n. 
<br>
Looking at the operations of the old function it seems like it is approximately 4n * sqrt(n) which is O(n * sqrt(n)).
<br>
Similarly, the new function executes roughly 2 * sqrt(n) operations which matches O(sqrt(n)).

Examples: 
 * n = 101: 2\*sqrt(n) = ~20, new_sqrt(n) = 41 operations, 4\*n\*sqrt(n) = 4060, old_sqrt(n) = 4523
 * n = 5'001: 2\*sqrt(n) = 141, new_sqrt(n) = 165 operations, 4\*n\*sqrt(n) = 1.4E6, old_sqrt(n) = 1.2E6
 * n = 500'001: 2\*sqrt(n) = 1414, new_sqrt(n) = 1455 operations, 4\*n\*sqrt(n) = 1.4E9, old_sqrt(n) = 1.4E9

The improvements are especially noticeable in the execution time. While for n=50001 it already takes the old version longer than a second, the improved version computes it in .0016 seconds. While the execution time of old version increases rapidly, the new version remains fairly quick up until n=50'000'001. However, the improved version is still no comparison to the function included in numpy which computes the result even for those numbers in microseconds.