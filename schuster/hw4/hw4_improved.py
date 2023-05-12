
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt

"""
def uniform(a,b) :
        # function returns a random  number in [a, b) if a < b
        return (b-a)*np.random.random() + a
"""

def f(x,R) :
        """
        circle function computing y
        """
        return np.sqrt(abs(x*x-R*R))

def approxPi(N) :
    """
    function returns an approximation of pi
    """
    Ninf = 0
    R = 1.0

    """
    replace lists with numpy arrays
    np.random.rand(N) comuptes N random numbers between 0 and 1 -> no need for uniform(a,b) anymore
    """
            
    list_x = np.random.rand(N)
    list_y = np.random.rand(N)

    # list_accepted_x = []
    
    """
    Using arrays instead of a for-loop
    
    if any(list_y < f(list_x,R)) :
        list_accepted_x = list_x[list_y < f(list_x,R)]

    no need to look if there are some elements with list_y < f(list_x,R) -> "if" isn't needed
    """

    list_accepted_x = list_x[list_y < f(list_x,R)]

    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)


    return 4*fin


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []

    for i in range(M) :

        list_rst = [approxPi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print(i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
