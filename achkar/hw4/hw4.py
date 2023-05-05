
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

import numpy as np
import matplotlib.pyplot as plt
import time

def uniform(a,b):
        """ 
        This function returns a random number between a and b
        """
        return (b-a)*np.random.random() + a

def f(x,R) :
        """
        This function returns the value of the function f(x) = sqrt(R^2 - x^2). 
        """
        return np.sqrt(abs(x*x-R*R))

def MonteCarlo(N):
        """
        This is a Monte Carlo method to calculate pi using N random points.
        """
        
        Ninf = 0 # number of points inside the circle
        R = 1.0 # radius of the circle

        list_x = [] # list of x coordinates
        list_y = [] # list of y coordinates

        for i in range(N) : # loop over the number of points
                list_x.append(uniform(0,R)) # generate a random x coordinate
                list_y.append(uniform(0,R)) # generate a random y coordinate
        
        list_accepted_x = [] # list of accepted x coordinates 

        for i in range(N) : # loop over the number of points 
                if (list_y[i]< f(list_x[i],R)) : # check if the point is inside the circle 
                        list_accepted_x.append(list_x[i]) # add the x coordinate to the list of accepted x coordinates

        Ninf = len(list_accepted_x) # number of points inside the circle
        fin = Ninf/float(N) # fraction of points inside the circle 


        return 4*fin # return the value of pi

def MonteCarlo_vec(N):
        """
        This is a Monte Carlo method to calculate pi using N random points. It uses vectorization to speed up the code.
        """
        
        Ninf = 0 
        R = 1.0 

        list_x = np.random.uniform(0,R,N) # np.random.uniform generates N random numbers between 0 and R
        list_y = np.random.uniform(0,R,N)

        list_accepted_x = list_x[list_y < f(list_x,R)] # using boolean indexing to select the points inside the circle

        Ninf = len(list_accepted_x) 
        fin = Ninf/float(N) 

        return 4*fin 

def main () :

        M = 100
        N = 1000

        list_mu = []
        list_sigma= []

        # start_time = time.time()
        # for i in range(M) :

        #         list_rst = [MonteCarlo(N) for _ in range(M)]
        #         list_mu.append(np.mean(list_rst))
        #         list_sigma.append(np.std(list_rst))
        #         print (i)
        
        # print("--- %s seconds ---" % (time.time() - start_time))

        # plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
        # plt.show()

        start_time = time.time()
        for i in range(M) :

                list_rst = [MonteCarlo_vec(N) for _ in range(M)]
                list_mu.append(np.mean(list_rst))
                list_sigma.append(np.std(list_rst))
                print (i)
        print("--- %s seconds ---" % (time.time() - start_time))
        plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
        plt.show()


if __name__ =="__main__" :
        main()

