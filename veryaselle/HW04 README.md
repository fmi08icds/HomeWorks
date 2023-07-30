HW04:


Task 1: The code performs a simulation using the Monte Carlo method to estimate the value of "pi" and generates a histogram of the results.



Task 2: Vectorized version of the function monte_carlo_sim:

montecarlo.py

def monte_carlo_sim_vec(N):
    R = 1.0

    list_x = np.random.uniform(0, R, N)
    list_y = np.random.uniform(0, R, N)

    list_accepted_x = list_x[list_y < f(list_x, R)]

    Ninf = len(list_accepted_x)
    fi = Ninf / N

    return 4 * fi

The function monte_carlo_sim_vec is a vectorized version of monte_carlo_sim, where we use NumPy's array operations and boolean indexing to efficiently generate random numbers and perform the calculations.



Task 3: Comparing computational times of the vectorized to the non-vectorized version:

To compare the computational times of both versions of the MonteCarlo_sim function, it has been used the 'time' module. With increasing 'N', the vectorized version becomes faster, providing significant speedup:


N = 1,000
Non-vectorized version time in seconds: 0.0028388500213623047
Vectorized version time in seconds: 0.00176239013671875

N = 100,000
Non-vectorized version time in seconds: 0.23164987564086914
Vectorized version time in seconds: 0.1428978443145752

N = 1,000,000
Non-vectorized version time in seconds: 2.3124899864196777
Vectorized version time in seconds: 1.419015884399414

To calculate the speedup, we divided the non-vectorized time by the vectorized time for each case. The vectorized version is approximately 1.6 times faster than the non-vectorized version.

Additionally, an improved vectorized version (monte_carlo_sim_vec_fast) was created, which showed even more significant speedup compared to the original vectorized version:


N = 1,000
Improved vectorized version time in seconds: 0.0

N = 100,000
Improved vectorized version time in seconds: 0.0031442642211914062

N = 1,000,000

Improved vectorized version time in seconds: 0.0465395450592041
The improved vectorized version provides substantial speedup, making it the most efficient option among the three implementations.