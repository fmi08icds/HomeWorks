
'''
Welcome to your fourth homework!	 
This exercise aims to teach you how to analyse a given code and explain in detail what it does.
'''
import argparse
import random

import numpy as np
import matplotlib.pyplot as plt
import numpy.random
import time
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def uniform(a,b):
        return (b-a)*np.random.random() + a


def f(x,r):
        res = np.sqrt((r**2-x**2))
        # print(f"x: {x}, res: {res}")
        return res


def calculate_pi(N):
    """
     This is a no name function. after figuring out what it does you're allowed to rename
    """
    Ninf = 0
    R = 1.0
    
    array_x = numpy.asarray([uniform(0, R) for i in range(N)])
    array_y = numpy.asarray([uniform(0, R) for i in range(N)])
    array_accepted_x = array_x[array_y < f(array_x, R)]

    Ninf = len(array_accepted_x)
    fin = Ninf/float(N)
    return 4*fin


def main():

    M = 100
    N = 1000

    list_mu = []
    list_sigma = []

    for i in range(M):

        list_rst = [calculate_pi(N) for _ in range(M)]
        list_mu.append(np.mean(list_rst))
        list_sigma.append(np.std(list_rst))
        print (i)

    plt.hist(list_mu, bins=np.linspace(3.12, 3.17, 100))
    plt.show()


def single_performance(n):
    start = time.time()
    calculate_pi(n)
    end = time.time()
    print(f"n: {n}, time: {end-start}s")
    return end-start


def test_performance():
    n_arr = np.asarray([100,1000,10000,100000,1000000, 10000000, 50000000])
    perf = [single_performance(n) for n in n_arr]
    f = open("perf_improved.txt", "w")
    f.write("n\t\t\ttime in s\n")
    for i in range(len(n_arr)):
        f.write(f"{n_arr[i]}\t\t\t{perf[i]}\n")
    f.close()


if __name__ == "__main__":
    doc_ =  """
               Calculates pi by estimation. 
            """
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS, description=doc_)
    parser.add_argument('--p', type=bool, action=argparse.BooleanOptionalAction, default=False, help="An integer input for which we compute the sqrt root.")
    args = parser.parse_args()
    if args.p:
        test_performance()
    else:
        main()

