
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

def estimatePi(N) :
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0
    
    #Run function within np array
    arr_x = np.array([uniform(0,R) for _ in range(N)])
    arr_y = np.array([uniform(0,R) for _ in range(N)])
    
    #Initialise empty np array 
    arr_accepted_x = np.array([])
    
    #Evaluate f(x,R) on all xi in arr_x
    comparison = np.array([f(xi,R) for xi in arr_x])
    
    #Boolean array for decision function
    boolarr_accepted_x = arr_y < comparison
    
    #count number of True comparisons. 
    Ninf = boolarr_accepted_x.sum()
    fin = Ninf / float(N)

    return 4*fin


  


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [estimatePi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
