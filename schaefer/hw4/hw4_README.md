# Homework 4

## Task 1: Figure out what the code does (in one sentence)

It performs a simulation to estimate the value of "pi" using the "Monte Carlo method" and creates a histogram of
the results.

(A more detailed explanation of the three functions 'uniform(a,b)', 'f(x,R)' and 'NoName(N)' is not desired.)


## Task 2: Provide a vectorized version of the function NoName()

I renamed the 'NoName()' function to 'MonteCarlo_sim' and created a new function 'MonteCarlo_sim_vec' 
where I vectorized it:
```
def MonteCarlo_sim_vec(N):

    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0, R, N)
    list_y = np.random.uniform(0, R, N)

    list_accepted_x = []
    for i in range(N):
        if list_y[i] < f(list_x[i], R):
            list_accepted_x.append(list_x[i])

    Ninf = len(list_accepted_x)
    fin = Ninf / float(N)

    return 4 * fin
```
'list_x' and 'list_y' are generated with the 'random.uniform()' function from NumPy.
They replace the loops for creating two lists of 'N' random numbers between 0 and 1.

Then it creates a list 'list_accepted_x' and if the y-value is less than the calculated square root then 'x' is added 
to the list.
In other words, the code selects all x-values whose corresponding y-value falls below the curve of the
function f() (in this case a semicircle). This is part of the process of generating a Monte Carlo estimate
of the value of pi.

The function then devides the length of 'list_accepted_x' by the Number 'N' and multiplies the result by 4 to estimate 
the value of Pi.

## Task 3: Compare the computational times of the vectorized to the non-vectorized version and report on it

To compare the computational times of both versions of the 'MonteCarlo_sim' and the new 'MonteCarlo_sim_vec' function 
I used the 'time' module in Python:
```
    import time

    # Non-vectorized version
    start = time.time()
    result = MonteCarlo_sim(N)
    end = time.time()
    endtime = end - start
    
    print("Non-vectorized version time in seconds:", endtime)
    print("Result of the calculation", result)


    # Vectorized version
    start = time.time()
    result_vec = MonteCarlo_sim_vec(N)
    end = time.time()
    endtime = end - start
    
    print("Vectorized version time in seconds:", endtime)
    print("Result of the calculation", result_vec)
```

For 'N' I tried a few iterations, here are some of the results:
```
N = 1.000
Non-vectorized version time in seconds: 0.0028388500213623047
Result of the calculation 3.084
Vectorized version time in seconds: 0.00176239013671875
Result of the calculation 3.172


N = 100.000
Non-vectorized version time in seconds: 0.23164987564086914
Result of the calculation 3.13864
Vectorized version time in seconds: 0.1428978443145752
Result of the calculation 3.1298


N = 1.000.000
Non-vectorized version time in seconds: 2.3124899864196777
Result of the calculation 3.140884
Vectorized version time in seconds: 1.419015884399414
Result of the calculation 3.140056
```
As you can see, the higher N gets, the more accurate the result of the calculation of pi becomes and the more time you 
save in one run.

To calculate the speedup I devided the non-vectorized time by the vectorized time for each case:

For N=1,000:
    Non-vectorized time: 0.0028388500213623047 seconds
    Vectorized time: 0.00176239013671875 seconds
    Speedup: 1.61 times faster

For N=100,000:
    Non-vectorized time: 0.23164987564086914 seconds
    Vectorized time: 0.1428978443145752 seconds
    Speedup: 1.62 times faster

For N=1,000,000:
    Non-vectorized time: 2.3124899864196777 seconds
    Vectorized time: 1.419015884399414 seconds
    Speedup: 1.63 times faster

So we can say the code is round about 1.6 times faster when using the vectorized version.


## Extra: Improved vectorized version

I created an even faster function for the algorithm as you can see in the results:
```
def MonteCarlo_sim_vec_fast(N):

    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0, R, N)
    list_y = np.random.uniform(0, R, N)

    list_accepted_x = list_x[list_y < f(list_x, R)]

    Ninf = len(list_accepted_x)
    fin = Ninf / float(N)

    return 4 * fin
```
Like in the first version of the code, the function uses the 'f' function defined earlier to calculate the square 
root of 'x' squared minus 'R' squared and compares it to the corresponding 'y' value.
If 'y' is less than the calculated square root then 'x' is added to the list 'list_accepted_x'.
But this time it uses NumPy's boolean indexing feature to select the values of 'list_x' where the corresponding value in 'list_y' is 
less than 'f(list_x, R)'.


I tested it with the same 'N' value as the other 2 functions.
```
N = 1.000
Improved vectorized version time in seconds: 0.0
Result of the calculation 3.084

N = 100.000
Improved vectorized version time in seconds: 0.0031442642211914062
Result of the calculation 3.14648

N = 1.000.000
Improved vectorized version time in seconds: 0.0465395450592041
Result of the calculation 3.14298
```

As you can see there is a significant speedup with this version of the function.
