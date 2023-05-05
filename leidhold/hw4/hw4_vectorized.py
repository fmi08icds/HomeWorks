
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
     This function is approximating the circular number PI by the Monte-Carlo-simualtion and the law of large numbers.

    """
    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0,R,size=N)
    list_y = np.random.uniform(0,R,size=N)
    

    is_inside = list_y < f(list_x,R)

    list_accepted_x = list_x[is_inside]

    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)

    return 4*fin


def main () :
    start=time.time()

    M = 1000
    N = 10000

    lst_rst = np.array([simulatePI(N) for _ in range(M)])

    list_mu = np.mean(lst_rst)
    list_sigma = np.std(lst_rst)

    et = time.time()
    elapsed_time = et - start
    print('Execution time: ', elapsed_time, 'seconds')
    
    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        
        main()

        # cProfiling
        cProfile.run('main()',"output.dat")

        import pstats
        from pstats import SortKey

        with open("output_time.txt", "w") as f:
              p = pstats.Stats("output.dat", stream=f)
              p.sort_stats("time").print_stats()