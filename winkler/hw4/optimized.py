
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt

def approximate_area(N) :
    R = 1.0

    # create vector of random x and y values
    list_x = np.random.uniform(0, R, N)
    list_y = np.random.uniform(0, R, N)

    # count how many points are below the function y = f(x)
    Ninf = np.sum(list_y < np.sqrt(R * R - list_x**2))
    # divide by number of samples N and multiply by 4 to get PI
    return 4 * Ninf / N


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [approximate_area(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()