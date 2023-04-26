# Running time in Landau notation (O notation)

## isperfect(n) function

The first block (lines 20 to 21) runs in O(1).
The second block (lines 24 to 27) runs in O(n) (for loop over range(n)).
Hence we have O(n).

## getLowUpper(n) function

The major parts of this function are the while loops.
The while loops combined run (u-l) times, 
where u is the upper perfect square root (closest to n)
and l is the closest lower perfect square root.
(u-l) is bound by 2n for n being a natural number.
Therefore, we have 2n times the running time of `isperfect()`.
Which is in O(n^2).

## mysqrt(n, err=0.000000001) function

We cut the current error in each round by about one half.
Hence, we are looking at a logarithmic number of rounds of the while loop.
Therefore, we should be looking at a running time of O(n^2*log(n)).

# Optimization suggestions

The profiling resulted in the following major time consuming parts:

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)


    31/29    0.067    0.002    0.084    0.003 :0(create_dynamic)
        1    0.013    0.013    0.013    0.013 :0(setprofile)
        1    0.001    0.001    0.020    0.020 _add_newdocs.py:1(<module>)
        1    0.001    0.001    0.001    0.001 _compat_pickle.py:9(<module>)
        1    0.001    0.001    0.043    0.043 core.py:1(<module>)
        1    0.001    0.001    0.010    0.010 hmac.py:1(<module>)
        1    0.002    0.002    0.002    0.002 linalg.py:2150(lstsq)
        1    0.001    0.001    0.001    0.001 linalg.py:469(inv)
        1    0.001    0.001    0.033    0.033 numeric.py:1(<module>)
        1    0.001    0.001    0.007    0.007 scimath.py:1(<module>)
        1    0.001    0.001    0.095    0.095 template_hw3.py:115(main)
       21    0.014    0.001    0.036    0.002 template_hw3.py:66(mysqrt)

It is obvious that the `mysqrt()` took most of the time. Except for methods 
like `create_dynamic` which we can influence (as I understand it) only by creating less objects
and `setprofile` which i don't know how to manipulate (it seems to have to do something with
parallelism). So we should try to improve the `mysqrt()` function.

We could improve the algorithm of `mysqrt()` especially at the part of checking n for being a perfect square root.
For example, we could store the first x perfect square roots in a tree structure 
to find them more efficiently (in O(log(n)). This costs memory (depending on x).
For n greater x we could fall back on the method we used in hm2.

Secondly, we could optimize the search of the lower and upper perfect square roots by another
binary search between n and 2n for the upper and n/2 and n for the lower perfect
square root. Binary search is in O(log(n)).
So, this would give 2*log(n) times the `isperfect()` function, hence (for n≤x) O(log(n)^2).


