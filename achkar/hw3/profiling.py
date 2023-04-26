import cProfile
import pstats
from pstats import SortKey
from hw2 import *
import numpy as np

def main():
    with cProfile.Profile() as pr:
        mysqrt(100000)
        pstats.Stats(pr).sort_stats(SortKey.TIME).print_stats()
    
    with cProfile.Profile() as pr:
        np.sqrt(100000)
        pstats.Stats(pr).sort_stats(SortKey.TIME).print_stats()

if __name__ == '__main__':
    main()