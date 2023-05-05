# What it does
1. The `NoName()` function estimates $\pi$ with the Monte Carlo Pi approach
2. The `Main` function calculates the mean and sd of `M` Monte Carlo approximations `M` times. Afterwards it plots the results

# Time complexity
1. Vectorized Monte Carlo calculation would be $O(2N)$, so $O(n)$
2. The main function would have a complexity of $O(M*M)$ so $O(M^2)$ or $O(n^2)$
3. complete file would be $O(M^2*N)$

# computational times
1. My tests regarding the computational times can be seen in the notebooks folder
2. For testing i ran the functions 100 times with N=10.000 and calculated the mean
3. The vectorized version seems to run a little quicker


|run | vectorized (s) | normal (s)|
|---|---|---|
|1 | 0.027 | 0.032|
|2 | 0.027 | 0.028|
|3 | 0.026 | 0.030|
|4 | 0.026 | 0.032|
|5 | 0.026 | 0.030|