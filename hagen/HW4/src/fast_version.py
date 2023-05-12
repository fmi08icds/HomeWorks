
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt


# Function "uniform" returns a random float with one decimal point, which is in the interval of a and b.
def uniform(a,b) :
        return (b-a)*np.random.random() + a


# Function "f" is a graph, that describes a half circle around the origin between -R and R on the x-axis. 
# Meaning, for positive x and y, it shows a quarter circle with radius R.
def f(x,R) :
        return np.sqrt(abs(x*x-R*R))

def circleArea(N) :
    """
     I named this function circleArea because it calculates the area for a circle with radius R (fixed R=1.0 but could be changed)
     without using the common formula A=π·r^2.
     Instead, it generates random points in a coordinate system and calculates the proportion of them, that fall under the function f(),
     so within the quarter circle with radius R. This *4 results in the area of the whole circle. Here, R is 1.0, so the area is π.
     In main(), by calling circleArea() many times the mean of all the result will be an approximation of the true circle area. 
    """
    Ninf = 0
    R = 1.0


    # As R=1, we can just use the built-in random for our coordinates (and don't need the uniform function).
    list_x = np.random.rand(N)
    list_y = np.random.rand(N)
    # Now we have 1000 points in a 2D-coordinate system with all coordinates being between 0 and 1.
    # This 1000 points are uniformly distributed like a cloud of points.
    # A single point i has the coordinates list_x[i] and list_y[i].

    list_accepted_x = list_x[ f(list_x,R) > list_y ]  # vectorized!
    # Now we have chosen only the points, that are below the function f, so within the quarter circle
    
    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)  # The proportion of points included (from all points) in the quarter circle.


    return 4*fin  # returns this proportion *4, so we get the full circle and not jut the quarter.


def main () :

    M = 100  # Number of repeats
    N = 1000  # Number of points in coordinate system

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [circleArea(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))  # calculate mean of results => circle area approximation.
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    #plt.show()


if __name__ =="__main__" :
        main()
