'''
Welcome to your fourth homework!
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt


def uniform(a, b):
    return (b - a) * np.random.random() + a


def f(x, R):
    return np.sqrt(abs(x * x - R * R))


def estimPI(N):
    R = 1.0

    list_x = np.random.uniform(0, R, size=N)
    list_y = np.random.uniform(0, R, size=N)

    list_accepted_x = list_x[list_y < f(list_x, R)]# GOOD!
    Ninf = len(list_accepted_x)

    fin = Ninf / N

    return 4 * fin


def main():
    M = 100
    N = 1000

    list_mu = []
    list_sigma = []

    for i in range(M):
        list_rst = np.array([estimPI(N) for _ in range(M)])
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print(i)

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ == "__main__":
    main()
