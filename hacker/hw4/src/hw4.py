
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyze a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, io

def uniform(a,b) :
    """
    return a uniformly distributed number in the interval (a, b)
    """
    return (b-a)*np.random.random() + a


def f(x,R) :
    """
    return the value of f at f(x,R)
    """
    return np.sqrt(abs(x*x-R*R))

def estimate_pi(N) :
    """
    this function estimates pi, if N is higher the accuracy is higher as well
    """
    Ninf = 0
    R = 1.0

    list_x = []
    list_y = []

    # create two list of uniformly distributed floats between 0 and 1
    for i in range(N) :
        list_x.append(uniform(0,R))
        list_y.append(uniform(0,R))

    list_accepted_x = []
    
    # append each element of the x list to a new list if f(x,R) is smaller than
    # the corresponding y value 
    for i in range(N) :
        if (list_y[i]< f(list_x[i],R)) :
            list_accepted_x.append(list_x[i])   

        
    
    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)


    return 4*fin

def estimate_pi_vectorized(N) :
    """
    this function estimates pi, if N is higher the accuracy is higher as well
    """
    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0,R, N)
    list_y = np.random.uniform(0,R, N)

    list_accepted_x = []

    # apply the filter function vectorized resulting in an array of
    # bools 
    list_accepted_x = list_y < np.vectorize(f)(list_x,R)
        
    # count the 'true' values in resulting list
    Ninf = np.count_nonzero(list_accepted_x)
    fin = Ninf/float(N)

    return 4*fin

def write_to_file(p, filename):
    s = io.StringIO()
    ps = pstats.Stats(p, stream=s)
    # write output to file
    ps.strip_dirs()
    ps.sort_stats('tottime')
    ps.print_stats()
    with open(filename + '.txt', 'w+') as f:
        f.write(s.getvalue())

def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []

    pr1 = cProfile.Profile()
    pr2 = cProfile.Profile()
    pr1.enable()
    for i in range(M) :
        list_rst = [estimate_pi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
    pr1.disable

    write_to_file(pr1, "non_v")
    pr2 = cProfile.Profile()

    pr2.enable()
    for i in range(M) :
        list_rst = [estimate_pi_vectorized(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
    pr2.disable

    write_to_file(pr2, "v")

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()



if __name__ =="__main__" :
        main()
