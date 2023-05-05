
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt
from time import time


# def uniform(a, b):
#     return (b-a)*np.random.random() + a

def uniform(N):
    return np.random.random(N), np.random.random(N)


def f(x):
    return np.sqrt(abs(x**2-1))


def pi_estimator(N):
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0

    list_x, list_y = uniform(N)

    Ninf = np.sum(list_y < f(list_x))

    fin = Ninf/float(N)

    return 4*fin


def main():

    t0 = time()

    M = 100
    N = 1000

    list_mu = []

    for i in range(M):

        list_rst = [pi_estimator(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    print('Runtime %d sec.' % (time()-t0))
    plt.show()


if __name__ == "__main__":
    main()
