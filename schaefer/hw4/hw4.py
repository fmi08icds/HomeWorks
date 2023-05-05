import numpy as np
import matplotlib.pyplot as plt
import time

def uniform(a,b) :
        return (b-a)*np.random.random() + a

def f(x,R) :
        return np.sqrt(abs(x*x-R*R))

def MonteCarlo_sim(N) :

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

# Vectorized 'MonteCarlo_sim' function
def MonteCarlo_sim_vec(N):

    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0, R, N)
    list_y = np.random.uniform(0, R, N)

    list_accepted_x = []
    for i in range(N):
        if list_y[i] < f(list_x[i], R):
            list_accepted_x.append(list_x[i])

    Ninf = len(list_accepted_x)
    fin = Ninf / float(N)

    return 4 * fin

# improved Vectorized 'MonteCarlo_sim' function
def MonteCarlo_sim_vec_fast(N):

    Ninf = 0
    R = 1.0

    list_x = np.random.uniform(0, R, N)
    list_y = np.random.uniform(0, R, N)

    list_accepted_x = list_x[list_y < f(list_x, R)]

    Ninf = len(list_accepted_x)
    fin = Ninf / float(N)

    return 4 * fin


def main () :

    M = 100
    N = 1000

    list_mu = []
    list_sigma= []


    for i in range(M) :

        list_rst = [MonteCarlo_sim(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)


    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


if __name__ =="__main__" :

    # Non-vectorized version
    start = time.time()
    result = MonteCarlo_sim(1000000)
    end = time.time()
    endtime = end - start
    print("Non-vectorized version time in seconds:", endtime)
    print("Result of the calculation", result)

    # Vectorized version
    start = time.time()
    result_v = MonteCarlo_sim_vec(1000000)
    end = time.time()
    endtime = end - start
    print("Vectorized version time in seconds:", endtime)
    print("Result of the calculation", result_v)

    # improved Vectorized version
    start = time.time()
    result_v_f = MonteCarlo_sim_vec_fast(1000000)
    end = time.time()
    endtime = end - start
    print("Improved vectorized version time in seconds:", endtime)
    print("Result of the calculation", result_v_f)

    #main()