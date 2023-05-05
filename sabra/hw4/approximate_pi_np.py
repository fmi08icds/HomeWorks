'''
Welcome to your fourth homework!
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''
import numpy as np
import matplotlib.pyplot as plt



def approximate_pi_with_monte_carlo_np(N,M):

    list_x = np.random.uniform(0, 1, size=(N,M))
    list_y = np.random.uniform(0, 1, size=(N,M))

    results = np.sqrt(np.abs(list_x**2 - 1.0**2))

    # Count True values in each column
    counts = np.sum(list_y < results, axis=0)

    fin = counts/N

    return 4 * fin


def main_np () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :
        results = approximate_pi_with_monte_carlo_np(N, M)
        list_mu.append(np.mean(results))
        list_sigma.append(np.std(results))

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()




if __name__ =="__main__" :
        main_np()

