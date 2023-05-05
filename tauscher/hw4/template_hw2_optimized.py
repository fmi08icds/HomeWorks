
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt


def uniform(a,b) :

        '''
        this function returns a random number between a and b from a uniform distribution 
        '''
        return (b-a)*np.random.random() + a


def f(x,R) :
        '''
        this function indicates some length check beween x and R
        in other words if x is within the boundary of R.
        '''
        return np.sqrt(abs(x*x-R*R))


"""insert comments on what the code below is doing"""
def pi_approximation_vec(N) :
    """
    This function returns the value of pi by using the Monte Carlo method. It first assigns some radius R.
    Afterwards N points on a square are generated that are uniformly distributed between 0 and R. 
    Then the function f is used to check if the points are within the boundary of R.
    """
    # this is the radius
    R = 1.0
    # these lists hold the x and y coordinates of the points
    
    # this sampling method generates N points and stores them in the lists
    # without using a slow forloop.
    rng = np.random.default_rng()
    list_x, list_y = rng.uniform(low=0.0, high=1.0, size=(2, N))

    # the following line checks if the points are within the boundary of a circular R.
    fin = np.count_nonzero(np.hypot(list_x,list_y)<R)/len(list_x)
    
    # because the simulation only covers one quadrant of the circle, the value of pi is multiplied by 4
    return 4*fin


def main () :

    # this is the number of times the simulation is repeated
    M = 100
    # this is the number of points that are generated for each simulation
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :
        # this list holds the results of the simulation with regards to mean and standard deviation
        list_rst = [pi_approximation_vec(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)

    # finally, the mean and standard deviation of the results are shown in a histogram.
    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
