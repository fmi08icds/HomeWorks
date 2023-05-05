
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

def NoName(N) :
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0

    list_x = []
    list_y = []

    for i in range(N) :
            list_x.append(uniform(0,R))
            list_y.append(uniform(0,R))

    list_accepted_x = []

    for i in range(N) :
            if (list_y[i]< f(list_x[i],R)) :
                    list_accepted_x.append(list_x[i])



    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)


    return 4*fin


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [NoName(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()