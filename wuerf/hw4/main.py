
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''
# %%
import numpy as np
import matplotlib.pyplot as plt
from numba import jit

def no_name_vectorized(N):
    """
    This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0

    random = np.random.random(N * 2).reshape(2, N)
    sqrt = np.sqrt(np.abs(np.power(random[1], 2) - R**2))
    filtered = random[1].where(random[0] < sqrt)
    #         list_accepted_x.append(list_x[i])

    Ninf = len(filtered)
    fin = Ninf / float(N)

    return 4 * fin
@jit
def no_name_vectorized(M,N):
    """
    This is a no name function. after figuring out what it does you're allowed to rename
    """

    R = 1.0

    random = np.random.random(M * N * 2).reshape(M, 2, N)
    sqrt = np.sqrt(np.abs(np.power(random[:, 1, :], 2) - R**2))
    filtered = np.where(random[:, 0] < sqrt, random[:, 1], np.nan)

    Ninf = np.sum(~np.isnan(filtered), axis=1)

    return 4 * Ninf / N


# %%
@jit
def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []



    for i in range(M) :
        list_rst = no_name_vectorized(M,N)
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))

    # plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    # plt.show()
#

if __name__ =="__main__" :
        main()

