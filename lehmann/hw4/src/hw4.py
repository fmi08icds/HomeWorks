
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt

def uniform(a,b) :
        return (b-a)*np.random.random() + a

def f(x,R) :
        return np.sqrt(abs(x*x-R*R))

def monteCarlo(N: int) :
    """
     Estimates Pi based on the Monte Carlo approach.
     
     N: Number of points to be generated 
    """
    Ninf = 0
    R = 1.0

    list_c = [uniform(0,R) for _ in range(N*2)]
    list_y = list_c[:N]
    list_x = list_c[N:]
    # list_x = [uniform(0,R) for _ in range(N)]
    # list_y = [uniform(0,R) for _ in range(N)]

    list_accepted_x = [list_x[i] for i in range(N) if list_y[i] < f(list_x[i],R)]

    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)


    return 4*fin


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [monteCarlo(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
