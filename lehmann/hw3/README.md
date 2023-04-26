# Files
- `hw3_time_tests.py` -> how i tested the time consumption of the different loops
- `hw3_final.py` -> final file, calculating square root without external libraries
- `hw3_lc.py` -> using list comprehensions
- `hw3_numpy.py` -> using numpy lists

# My approach
1. To find time expensive functions, i used `time.time()` to check start and end time of a function. <- `hw3_time_tests.py`
	1. The most time expensive is the isPerfect function, as it contains a loop and gets called inside of the `getLowUpper()` loops
	2. Because of this, the `getLowUpper()` function is slow too. These "nested" loops appear 2 times which at least doubles the required time
	3. The loop in the main function mysqrt() is not a problem as its not depended on `n`, but will take a while as the numbers get bigger
2. The Homework Code has a complexity of $O(n^2)$
	1. isPerfect = $O(n)$
	2. getLowUpper = $O(log~n)$ -> because `i` closes in on `n` with evey loop but will never reach it, but you could also argue that its $O(n)$
	3. mysqrt = $O(1)$ -> also not contained in the other loops
	4. Results could be $O(n²)$, BUT you could argue that `i` will never be as big as `n` in the getLowUpper loop, so the final results would be more like $O(n~log ~n)$
3. For better results we can do following things
	1. Use Vectorization, either numpy or list comprehension OR use one basic while loop (visible in `hw3_final.py`)
	2. get rid of the second while loop in getLowUpper, as the upper border is always lower border+1
	3. In my final and best cases i use a simple while loop, iterating $i+=1$ until $i^2$ surpasses $n$. So the last `i` is the lowest possible square root and the upper border would obviusly be $i+1$
4. Results
    1. Tests with the number 10 Million and linux `time` command
    2. `hw3_final.py`: user+sys = 465 ms
    3. `hw3_lc.py`: user+sys = 1515 ms 
    4. `hw3_numpy.py` user+sys = 537 ms
    5. These Numbers include the tests and numpy sqrt() function provided in the main function of the previous Homework, but the difference is still valid
    6. My best and final result is in `hw3_final.py`with $O(log~n)$
5. My Sources
    1. numpy doc for `np.where()` function and i searched for the linux `time` command