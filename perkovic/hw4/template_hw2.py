
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''

#imports nessasary libaries 
import numpy as np
import matplotlib.pyplot as plt

# returns a random number between 0 and 1 since 0 and R is passed from function approximasationOfPi
def uniform(a,b) :
        return (b-a)*np.random.random() + a


# returns a y (point on the quadrant of a circle) for every x value
def f(x,R) :
        return np.sqrt(abs(x*x-R*R))




def approximasationOfPi(N) :
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0

#creates two lists with random values on the x and y axis, where the values are generated by the uniform function
    list_x = []
    list_y = []

    for i in range(N) :
            list_x.append(uniform(0,R))
            list_y.append(uniform(0,R))

#creates a list for all the accepted x values
    list_accepted_x = []

#Iterates over each pair of x and y values, and checks if return from the f(x,R) function (a point on the quadrant) is bigger then the y from the list_y
#if this is the case the x value of the respective position is stored in the list of accepted x values
    for i in range(N) :
            if (list_y[i]< f(list_x[i],R)) :
                    list_accepted_x.append(list_x[i])


#Calculate the ratio of accepted x values to total number of N

    Ninf = len(list_accepted_x)
    fin = Ninf/float(N)

#Multiply by 4 to obtain the approximation value of Pi
    return 4*fin
    
  

def main () :

    M = 100
    N = 1000

# Create lists for mean and standard deviation
    list_mu = []
    list_sigma= []

# Iterates M times, and for each iteration, generate a list of N estimated values of Pi using the approximasationOfP function
    for i in range(M) :

        list_rst = [approximasationOfPi(N) for _ in range(M)]

# Append the mean and standard deviation of the list of estimated values of Pi to list_mu and list_sigma
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)

#Plots a histogram of the mean values with 100 bins between 3.12 and 3.17
    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :
        main()
