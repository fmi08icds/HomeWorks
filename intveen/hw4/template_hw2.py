
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''
import cProfile
import numpy as np
import matplotlib.pyplot as plt

def uniform(a,b) :
        return (b-a)*np.random.random() + a

def f(x,R) :
        return np.sqrt(abs(x*x-R*R))

def estimate_pi(N) :
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0

    list_x = []
    list_y = []

    for i in range(N): # generates x,y-pairs
            list_x.append(uniform(0,R)) # list with N values uniformly distributed in the interval between [0,1]
            list_y.append(uniform(0,R)) # list with N values uniformly distributed in the interval between [0,1]

    # list_x = np.random.random(N)
    # list_y = np.random.random(N)

    list_accepted_x = []

    for i in range(N): # filters list_x and accept only values i where f(list_x[i], R) < list_y[i]
            if (list_y[i]< f(list_x[i],R)) :
                    list_accepted_x.append(list_x[i])

    # R_vec = np.array(N*[1.0])
    # list_accepted_x_vec = list_x[np.where(f(list_x, R_vec) > list_y, True, False)]


    Ninf = len(list_accepted_x) # get the number of accepted values
    # Ninf = len(list_accepted_x_vec)
    fin = Ninf/float(N) # calculates the ratio of accepted values


    return 4*fin # returns 4 times the accepted ratio


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [estimate_pi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print(i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        cProfile.run("main()")
