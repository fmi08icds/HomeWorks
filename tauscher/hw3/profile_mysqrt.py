import cProfile
from numpy import random, sqrt
import template_hw1
import pstats
import timeit

def main() :
    #generate random numbers
    random.seed(123)  # Set the seed for reproducibility
    rng = random.default_rng()
    random_integers = rng.integers(low=0, high=100, size=25000)

    profiler = cProfile.Profile()
    profiler.enable()
    for number in random_integers:
        template_hw1.mysqrt(number)
    profiler.disable()
    profiler.dump_stats("mysqrt.stats")
 
    stats = pstats.Stats("./mysqrt.stats")
    stats.print_stats()

    profiler2 = cProfile.Profile()
    profiler2.enable()
    for number in random_integers:
        square = sqrt(number)
    profiler2.disable()
    profiler2.dump_stats("numpysqrt.stats")
 
    stats2 = pstats.Stats("./numpysqrt.stats")
    stats2.print_stats()
    


    ### approach 2, timeit:
    print('timeit mysqrt')
    print(timeit.timeit(number=1000, setup='from numpy import random; import template_hw1; random.seed(123)', stmt='template_hw1.mysqrt(random.randint(0, 1000, 1)[0])'))
    print('vs. numpy implementation')
    print(timeit.timeit(number=1000, setup='from numpy import random, sqrt; import template_hw1; random.seed(123)', stmt='sqrt(random.randint(0, 1000, 1)[0])'))


    


if __name__ == '__main__':
    main()
