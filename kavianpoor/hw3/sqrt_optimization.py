import cProfile
import pstats
import math
from pstats import SortKey
from template_hw1 import *
import numpy as np

'''def main():
    with cProfile.Profile() as pr:
        mysqrt(100)
        pstats.Stats(pr).sort_stats(SortKey.TIME).print_stats()
    
    with cProfile.Profile() as pr:
        np.sqrt(100)
        pstats.Stats(pr).sort_stats(SortKey.TIME).print_stats()

if __name__ == '__main__':
    main()'''

import timeit



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



'''def fast_sqrt(x, n_steps=5):
    if x < 0:
        raise ValueError("Cannot compute square root of negative number")
    if x == 0:
        return 0
    guess = x / 2
    for i in range(n_steps):
        guess = guess - ((guess ** 2 - x) / (2 * guess))
    return guess'''









'''def mysqrt_optimized(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    x = n // 2
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y'''


import cProfile
import pstats
from pstats import SortKey
from template_hw1 import *
import numpy as np

'''def main():
    inputs = {n: None for n in range(1, 10001)}

    for n in inputs:
        with cProfile.Profile() as pr:
            mysqrt_optimized(n)
        inputs[n] = pr

    for n, stats in inputs.items():
        print(f"n = {n}:")
        pstats.Stats(stats).sort_stats(SortKey.TIME).print_stats()'''


'''def main():
    inputs = [1000000000000, 10, 1000, 100000]
    for num in inputs:
        with cProfile.Profile() as pr:
            n= 1000
            mysqrt(num)
        stats = pstats.Stats(pr).sort_stats(SortKey.TIME)
        stats.print_stats()
        print("="*40)
  

if __name__ == '__main__':
    main()'''


  