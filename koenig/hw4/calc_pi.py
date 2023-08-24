"""
Welcome to your fourth homework!
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
"""

import numpy as np
import matplotlib.pyplot as plt


def uniform(a, b):
    return (b - a) * np.random.random() + a


def f(x, r):
    return np.sqrt(abs(x * x - r * r))


def calculate_pi_non_vector(n):
    """
     This is a function to calculate the value of pi with Python functions.
    """
    r = 1.0

    list_x = []
    list_y = []

    for i in range(n):
        list_x.append(uniform(0, r))
        list_y.append(uniform(0, r))

    list_accepted_x = []

    for i in range(n):
        if list_y[i] < f(list_x[i], r):
            list_accepted_x.append(list_x[i])

    ninf = len(list_accepted_x)
    fin = ninf / float(n)

    return 4 * fin


def calculate_pi_vector(n):
    """
     This is a function to calculate the value of pi with numpy vectorized functions.
    """
    r = 1.0

    list_x = np.random.uniform(0, r, n) # Good
    list_y = np.random.uniform(0, r, n) # Good 

    ninf = np.count_nonzero(list_y < f(list_x, r))
    fin = ninf / float(n)

    return 4 * fin


def main():
    # number of Monte Carlo simulation runs
    m = 200
    # number of data points in each run
    n = 1000

    list_mu = []
    list_sigma = []

    for i in range(m):
        list_rst = [calculate_pi_vector(n) for _ in range(m)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print(i)

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ == "__main__":
    main()
