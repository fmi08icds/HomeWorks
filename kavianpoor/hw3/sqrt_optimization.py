


import cProfile
import pstats
from pstats import SortKey
from template_hw1 import *
import numpy as np

def main():
    input_range = range(1, 10001, 1000)

    for num in input_range:
        with cProfile.Profile() as pr:
            my_sqrt(num)
        stats1 = pstats.Stats(pr).sort_stats(SortKey.TIME)

        with cProfile.Profile() as pr:
            np.sqrt(num)
        stats2 = pstats.Stats(pr).sort_stats(SortKey.TIME)

        print(f"Input: {num}")
        print("mysqrt:")
        stats1.print_stats()
        print("np.sqrt:")
        stats2.print_stats()
        print("========================================")



def my_sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    if x == 0:
        return 0
    low = 0
    high = x
    while True:
        mid = (low + high) / 2
        if abs(mid ** 2 - x) < 1e-9:
            return mid
        elif mid ** 2 > x:
            high = mid
        else:
            low = mid


if __name__ == '__main__':
    main()





  
