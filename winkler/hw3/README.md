# Homework 3


## Step 1: Profile existing implementation from Homework 2

In the first step, the existing implementation created in homework 2 was profiled using `cProfile`.
The script was executed with an input number of `100000` (10^5) and with the `cProfile` module.
The output is really verbose and was limited to function calls that happen in the script. Additionally, the overall runtime was measured using the `time` command.

This leads to the following output: 

```
> python3 -m cProfile square_root_old.py --n 100000 | grep "square_root_old"

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.175    0.175 square_root_old.py:1(<module>)
        1    0.000    0.000    0.011    0.011 square_root_old.py:115(main)
       21    0.001    0.000    0.003    0.000 square_root_old.py:71(mysqrt)
      270    0.001    0.000    0.001    0.000 square_root_old.py:5(isperfect)
       17    0.000    0.000    0.001    0.000 square_root_old.py:36(getLowUpper)


> time python3 square_root_old.py --n 1000000 >/dev/null

real    0m0,257s
user    0m0,237s
sys     0m0,021s
```

This was repeated for larger input value of `1000000` (10^6) which yields:

```
> python3 -m cProfile square_root_old.py --n 1000000 | grep "square_root_old"

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    3.405    3.405 square_root_old.py:1(<module>)
        1    0.000    0.000    3.231    3.231 square_root_old.py:115(main)
       21    0.001    0.000    3.223    0.153 square_root_old.py:71(mysqrt)
       21    0.003    0.000    3.222    0.153 square_root_old.py:36(getLowUpper)
     6616    3.219    0.000    3.219    0.000 square_root_old.py:5(isperfect)


> time python3 square_root_old.py --n 10000000 >/dev/null

real    0m2,063s
user    0m2,031s
sys     0m0,032s
```

**Observations:**

- The `mysqrt` function is always called 21 times independently of `--n`.
  This is due to the fact that the square root is calculated for the input number and also for 20 randomly generated test values.
  However, the number of calls to the `getLowerUpper` function varies each run because `mysqrt` does not need to call it if the randomly generated test value is already a perfect square.

- The function that is executed the most is `isperfect`, which makes up most of the execution time when N = 10^6. For the smaller input the total time does not contribute much to the runtime of the program.


## Step 2: Determine time complexity

Next, the time complexity of the square root calculation will be derived from the source code. The square root is calulcated by the `mysqrt` function. This function depends on two parameters: The integer whose square root should be computed and the error threshold. In the following, they will be denoted as $n$ and $\epsilon$, respectively.

The `mysqrt` function relies on two other helper functions. They are analyzed first: 

**`isperfect`**: This helper function consists of one loop that runs from `0` to `n-1`. In the worst case the function has to complete the entire loop until a result is returned. Hence, the function has a *linear* time complexity, i. e., $\mathcal{O}(n)$.

**`getLowUpper`**: In this function there are two loops that are executed sequentially. They check every integer smaller or bigger than $n$ until a perfect square number is found. In other words, the function tries to find $a, b \in \mathbb{N}$ such that $a^2 < n < b^2$. Consequently, the function must run the `isperfect` function exactly $b^2 - a^2$ times for any $n > 1$. This means that the number of iterations increases quadraticly. Since `isperfect` has a linear time-complexity, this leads to a *cubic* time complexity, i. e., $\mathcal{O}(n^3)$.

Finally, these information can be used to determine the time complexity of `mysqrt`. In the worst case, it must call both helper functions exactly once. This means that the time complexity is $\mathcal{O}(n)$ because `getLowUpper` is the dominant factor. It must also be taken into account that the `mysqrt` function also contains a loop in order to approximate the floating point value of the square root. However, the number of iterations depends on the error threshold $\epsilon$ and not $n$. The time complexity of this loop is $\mathcal{O}(\log_2(\epsilon))$ because the difference between `maxsqrt` and `minsqrt` is halfed at every iteration until this difference is below the threshold.

To summarize, the overall time complexity of calculating the square root of $n$ with an error threshold of $\epsilon$ using the function `mysqrt` is $\mathcal{O}(n^3 + \log_2(\epsilon))$.


## Step 3: Code optimization

NOTE: Use vectorization
