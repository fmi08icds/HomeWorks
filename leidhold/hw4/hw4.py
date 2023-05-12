
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt
import time
import cProfile

def uniform(a,b) :
        return (b-a)*np.random.random() + a

def f(x,R) :
        return np.sqrt(abs(x*x-R*R))

def simulatePI(N) :
    """
     This function is approximating the circular number PI by the Monte-Carlo-simualtion.

    """
    Ninf = 0
    R = 1.0

    list_x = []
    list_y = []
    
    # this for loop is generating two lists with N (=1000) random uniform distributed points between 0 and 1
    for i in range(N) :
            list_x.append(uniform(0,R))
            list_y.append(uniform(0,R))


    list_accepted_x = []
    
    # this for loop is checking for every point if it lies inside a quarter circle with radius R=1.0 
    for i in range(N) :
            if (list_y[i]< f(list_x[i],R)) :
                    # if the point lies inside the quarter circle it is added to a list of accepted points
                    list_accepted_x.append(list_x[i])


    # ratio of the points inside the quarter circle to total number of generated points
    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)

    # calculation of Pi by taking for times the ration computed before
    return 4*fin


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []

    start = time.time()
    for i in range(M) :

        list_rst = [simulatePI(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)

    et = time.time()
    elapsed_time = et - start
    print('Execution time: ', elapsed_time, ' seconds')
    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()

        # cProfiling
        cProfile.run('main()',"oldoutput.dat")

        import pstats
        from pstats import SortKey

        with open("oldoutput_time.txt", "w") as f:
              p = pstats.Stats("oldoutput.dat", stream=f)
              p.sort_stats("time").print_stats()
