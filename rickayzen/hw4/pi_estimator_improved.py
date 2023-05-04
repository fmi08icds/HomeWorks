
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''
import random

import numpy as np
import matplotlib.pyplot as plt
import numpy.random


def uniform(a,b):
        return (b-a)*np.random.random() + a


def f(x,r):
        res = np.sqrt((r**2-x**2))
        # print(f"x: {x}, res: {res}")
        return res


def calculate_pi(N):
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0
    
    array_x = numpy.asarray([uniform(0, R) for i in range(N)])
    array_y = numpy.asarray([uniform(0, R) for i in range(N)])
    true_vector = array_y < f(array_x, R)
    array_accepted_x = array_x[true_vector]

    Ninf = len(array_accepted_x)
    fin = Ninf/float(N)
    return 4*fin


def main():

    M = 100
    N = 1000

    list_mu = []
    list_sigma = []

    for i in range(M):

        list_rst = [calculate_pi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ == "__main__":
    main()
