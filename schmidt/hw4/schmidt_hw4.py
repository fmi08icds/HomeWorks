
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt

def uniform(a,b):
        return (b-a)*np.random.random() + a

def f(x,R):
        return np.sqrt(abs(x*x-R*R))

def estimate_pi(N):
    """
     This function uses the Monte-Carlo method to estimate pi
     :param N:  How many points to generate for the estimation
    """
    R = 1.0

    array_x = np.random.uniform(low=0.0, high=R, size=(N,))
    array_y = np.random.uniform(low=0.0, high=R, size=(N,))

    array_curve = np.apply_along_axis(f, 0, array_x, R)
    Ninf = np.sum(array_y < array_curve)

    fin = Ninf/float(N)

    return 4*fin


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [estimate_pi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
