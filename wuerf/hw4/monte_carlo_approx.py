# %%
import numpy as np
import matplotlib.pyplot as plt
from numba import jit ## COMMENTS: it was not needed for this assignment...


@jit
def f(X: np.array, R: float) -> np.array:
    return np.sqrt(np.abs(np.power(X[:, 1, :], 2) - R**2))


@jit
def monte_carlo_approx_vectorized(M: np.array, N: np.array, r: float = 1.0) -> np.array:
    """
    Calculates an approximation of the integral of a function over a square of
    length R using the Monte Carlo method. The approximation is based on the
    ratio of the number of data points that lie inside the square to the total
    number of data points generated.

    :param N: Number of random data points to generate per sample
    :param M: Number or samples
    :param r: the length of the square

    :return: An approximation of the integral of the function for multiple samples.
    """

    random = (r * np.random.random(M * N * 2)).reshape(M, 2, N)
    filtered = np.where(random[:, 0] < f(random, r), random[:, 1], np.nan)

    Ninf = np.sum(~np.isnan(filtered), axis=1)

    return 4 * Ninf / N


@jit
def main():
    M = 100
    N = 1000

    list_mu = []
    list_sigma = []

    # I tired to unfold this loop, but the memory overhead is way too big
    for i in range(M):
        list_rst = monte_carlo_approx_vectorized(M, N)
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()

# %%
