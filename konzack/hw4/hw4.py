
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt

def uniform(a,b) :
        """ Return a random value sampled from a uniform distribution on [a,b]"""
        return (b-a)*np.random.random() + a

def f(x,R) :
        """ Get the corresponding y for an x in a circle with radius R """
        return np.sqrt(abs(x*x-R*R))

def approximate_pi(N) :
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0

    list_x = []
    list_y = []

    # Generate N random values between 0 and R in x and y
    for i in range(N) :
            list_x.append(uniform(0,R))
            list_y.append(uniform(0,R))

    list_accepted_x = []

    # Accepts f(x) values with radius R that are bigger than a random y
    for i in range(N) :
            if (list_y[i]< f(list_x[i],R)) :
                    list_accepted_x.append(list_x[i])



    Ninf = len(list_accepted_x)
    # The relative frequency of the accepted values relative to N
    # This corresponds to the area under the circle between 0 and R
    # This is 1/4 of the full area of the circle
    fin = Ninf/float(N)

    # Return the area of the full circle
    # This is given by pi * R*R
    # With R = 1 we get pi
    return 4*fin

def vectorized_approximate_pi(n: int):
    R = 1.0

    # Generate a 2xn matrix of uniformly random numbers between 0 and 1
    random_numbers = np.random.random((2, n))
    xs = random_numbers[0]
    ys = random_numbers[1]

    # Get the number of points under the curve of f for randomly sampled points
    points_under_curve = np.sum(ys < f(xs, R))

    # Divide by n to get the integral of the approximate integral of the curve
    integral = points_under_curve / n

    return 4*integral


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma = []


    for i in range(M) :

        # Generate M times pi
        list_rst = [approximate_pi(N) for _ in range(M)]
        # Get the mean of our pi approximation
        list_mu.append(np.mean(list_rst))
        # Get the standard deviation of the approximations
        # This variable is unsused so it should not be calculated
        #list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
#     plt.show()


if __name__ =="__main__" :
        main()