
'''
Welcome to your fourth homework!
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''
## COMMENTS: well done.
import numpy as np
import matplotlib.pyplot as plt
import time


def f(x,R) :
        return np.sqrt(abs(x*x-R*R))


def estimate_pi(N):
    R = 1.0
    x = np.random.uniform(0, R, N)
    y = np.random.uniform(0, R, N)
    Ninf = np.sum(y < f(x, R))
    fin = Ninf / N
    return 4 * fin

def main():
    M = 100
    N = 1000

    list_mu = []
    list_sigma= []

    start_time = time.time() # Start timer

    for i in range(M):
        list_rst = np.array([estimate_pi(N) for _ in range(M)])
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print(i)

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()

    end_time = time.time() # End timer

    elapsed_time = end_time - start_time

    print(f"Elapsed time: {elapsed_time:.2f} seconds")




if __name__ =="__main__" :
        main()
