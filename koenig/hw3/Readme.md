# Home work 3 by Ralf König

* Lecture: Introduction to Computing in Data Science, Summer Term 2023
* University of Leipzig

## Task 1: Profile the Square root program

**Task Description:** _Use `--n 1000` or bigger. Test multiple numbers.
Determine which helper functions needs how much time._

This solution is in the file `sqrt_naive.py`.
It is the original Python code from ``template1_hw.py`` with just the "None"s replaced.

The random test suite (100 numbers) in that file was commented out.

I tested with the Profiler built into PyCharm.

| number `n` |  `getLowUpper` (own time) |  `isperfect` (own time) |
|--------|------------------------|---------------------------|
| 1200 | 1 call, 0 ms  | 70 call, 3 ms |
| 2400 | 1 call, 0 ms | 98 calls, 8 ms |
| 4800 | 1 call,  0 ms | 140 call, 25 ms |
| 9600 | 1 call, 0 ms | 196 calls, 74 ms |
| 19200 | 1 call, 0 ms |  278 calls, 210 ms |
| 38400 | 1 call, 0 ms |  392 calls, 564 ms |
| 76800 | 1 call, 0 ms |  556 calls, 1592 ms |
| 120000 | 1 call, 0 ms | 694  calls, 3063 ms |
| 153600 | 1 call, 0 ms | 784  calls, 4468 ms |


## Task 2: Find an approximation of the time complexity.

**Task description:** _Identify all the loops, parameters, worst case complexity
in Big-O-Notation._

`getLowUpper` is called once. Due to the internal while loops it has O(n) time complexity (own time), if the sub calls 
are not taken into account. However, time spent in those loops is so small (<1ms), that the profiler rounded own time  
down to 0 ms.

`isPerfect` is called inside getLowUpper inside `while` loops (that are in O(n)) and an inside `for` loop, that 
depends on `n` again. Overall, the whole program `sqrt_naive.py` has worst case O(n²) execution time complexity.

This can also be seen in the benchmark results.

## Task 3: Suggest optimal code / script.

**Task Description:**
* _Compute sqrt as fast as possible in Python._
* _Consider vectorization in Python => replace for-loops and while-Loops by Broadcasting via `numpy`._

I built three approaches (``sqrt_improved.py``, ``sqrt_improved_vec.py``, ``sqrt_bin_search.py``) and a small benchmark application 
``benchmark.py``.

### ``sqrt_improved.py``

This version uses a Python list to hold the data structure of precomputed squares.
It uses a precomputed data structure that holds square integers up to a certain 
threshold value. It then uses list functions in the code to find the entries in this data structure.

### ``sqrt_improved_vec.py``

This version uses a `numpy.ndarray` to hold the data structure of precomputed squares.
It also uses a precomputed data structure that holds square integers up to a certain 
threshold value. It uses numpy vectorized versions of the calculations.

### ``sqrt_bin_search.py``

This version uses pure binary search on the whole range from 0 to n/2+1. 
It does not use any of the helper functions.

## Benchmarking

Comparison of the execution times is performed by ``benchmark.py``.
It has an internal parameter repetitions to perform a number of cycles.

### Benchmarking against `sqrt_naive.py`

* 10 repetitions of sqrt calculations per run. Reason: ``sqrt_naive.py`` is so slow.
* All times in seconds.

|``n``|``sqrt_naive.py``|``sqrt_optimized.py``|``sqrt_optimized_vec.py``|``np.sqrt``|
|-----------|-----------|-----------|-----------|-----|
| 1200|	   0.02823|	   0.00046|	   0.00078|	   0.00003|
| 2400|	   0.09119|	   0.00031|	   0.00052|	   0.00002|
| 4800|	   0.25638|	   0.00030|	   0.00043|	   0.00002|
| 9600|	   0.69796|	   0.00032|	   0.00044|	   0.00002|
|19200|	   1.93333|	   0.00033|	   0.00049|	   0.00002|
|38400|	   5.45138|	   0.00036|	   0.00051|	   0.00002|

### Benchmarking against ``numpy.sqrt``

* 100 repetitions of sqrt calculations per run
* All times in seconds.

|n       	|sqrt_optimized	|sqrt_optimized_vec	|sqrt_bin_search	|np.sqrt|
|----------|-----------|-----------|-----------|-------|
|  300	   |0.00312	   |0.01083	   |0.00560	   |0.00024|
|  600	   |0.00542	   |0.00436	   |0.00434	   |0.00017|
| 1200	   |0.00378	   |0.00383	   |0.00485	   |0.00017|
| 2400	   |0.00312	   |0.00408	   |0.00503	   |0.00019|
| 4800	   |0.00334	   |0.00812	   |0.00418	   |0.00017|
| 9600	   |0.00348	   |0.00404	   |0.00424	   |0.00018|
|19200	   |0.00369	   |0.00398	   |0.00414	   |0.00018|
|38400	   |0.00626	   |0.00584	   |0.00461	   |0.00026|
|76800	   |0.00640	   |0.00516	   |0.00420	   |0.00018|
|900000	   |0.00722	   |0.00358	   |0.00514	   |0.00024|
|2000000   |0.01228   |0.00368	   |0.00376	   |0.00016|
