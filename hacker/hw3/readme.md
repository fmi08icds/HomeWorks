## Results

First we can have a look at the baseline. We simply instrument the code and write the results to a file by adding the following lines of code:

```python
import cProfile, pstats, io

pr = cProfile.Profile()
pr.enable()
res = callFunc()
pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
# write output to file
ps.print_stats()
with open('out.txt', 'w+') as f:
    f.write(s.getvalue())
```

### Baseline
If we call the srt function now with a high number
```bash
python profiled_main.py --n 99999
```
We get the following results:
```
675 function calls in 3.328 seconds
Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
634    3.327    0.005    3.327    0.005 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:6(isperfect)
1    0.000    0.000    3.323    3.323 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:29(getLowUpper)
1    0.000    0.000    3.328    3.328 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:62(mysqrt)
38    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
As we can see  the 'isperfect' function is taking the most time (3.327s) as it is called so many times and also very expensive.

### Optimized sqrt function
We can optimize the code by making a couple changes:
- get the initial estimate with the subtraction estimation function to either get the sqrt if it is perfect or a close estimate
- beginning at the estimate we can then find the sqrt iteratively

If we call the optimezed function with the same n we get the following output:

```
4 function calls in 0.000 seconds
Ordered by: internal time

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.000    0.000 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:6(sqrt_sub_method)
1    0.000    0.000    0.000    0.000 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:17(opt_sqrt)
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
```
We can repeat the same call with a higher number to see some results:

```bash
python profiled_main.py --n 99999999999999
```

```
4 function calls in 1.007 seconds
Ordered by: internal time
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    1.007    1.007    1.007    1.007 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:6(sqrt_sub_method)
1    0.000    0.000    1.007    1.007 /home/leo/Documents/UNI/ITCDS/HomeWorks/hacker/hw3/src/profiled_main.py:17(opt_sqrt)
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
```