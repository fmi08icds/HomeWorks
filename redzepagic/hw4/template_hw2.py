
'''
Welcome to your fourth homework!
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt

def uniform(a,b) :
        return (b-a)*np.random.random() + a

# gives the y coordinate to the given x coordinate, sucht that (x, y) is on the circle with radius R and center (0, 0)
def f(x,R) :
        return np.sqrt(abs(x*x-R*R))

# this function generates points in a square with a = R and returns the portion of points which are in a circle with radius r, so it gives the integral of a quarter circle
# so it approximates the area of a quarter of a circle and returns the approximated area of the whole circle

##COMMENTS: very import to mention the technique used to approximate that area. Monte Carlos simulation.
def approximate_circle_area(N) :
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

# calculates and shows the distribution of the means of the approximated circle areas in a plot
def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [approximate_circle_area(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
