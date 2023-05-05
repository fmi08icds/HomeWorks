import cProfile
from numpy import random, sqrt
import template_hw1
import pstats
from pstats import SortKey
import timeit
import io

def main() :
    #generate random numbers
    random.seed(123)  # Set the seed for reproducibility
    rng = random.default_rng()
    random_integers = rng.integers(low=0, high=2500, size=2500)

    n_numbers= f'Test for n={len(random_integers)} Numbers.'

    profiler = cProfile.Profile()
    profiler.enable()
    for number in random_integers:
        template_hw1.mysqrt(number)
    profiler.disable()
    profiler.dump_stats("./hw3/mysqrt.stats")

    profiler2 = cProfile.Profile()
    profiler2.enable()
    for number in random_integers:
        template_hw1.mysqrt_opt(number)
    profiler2.disable()
    profiler2.dump_stats("./hw3/mysqrt_opt.stats")
    

    ## for profiling the numpy function we need a wrapper containing the numpy native implementation.
    def npsqrt(*args):
        sqrt(*args)

    profiler3 = cProfile.Profile()
    profiler3.enable()
    for number in random_integers:
        template_hw1.mysqrt_fast(number)
    profiler3.disable()
    profiler3.dump_stats("./hw3/mysqrt_fast.stats")
 
    ### approach 2, timeit:
    ntimes = 2500
    timeit_1=(timeit.timeit(number=ntimes, setup='from numpy import random; import template_hw1; random.seed(123)', stmt='template_hw1.mysqrt(random.randint(0, 2500, 1)[0])'))
    timeit_2=(timeit.timeit(number=ntimes, setup='from numpy import random; import template_hw1; random.seed(123)', stmt='template_hw1.mysqrt_opt(random.randint(0, 2500, 1)[0])'))
    timeit_3=(timeit.timeit(number=ntimes, setup='from numpy import random; import template_hw1; random.seed(123)', stmt='template_hw1.mysqrt_fast(random.randint(0, 2500, 1)[0])'))


    with open("./hw3/stats_out.txt", "w") as f:
        # Markdown content
        formatting_str = ''
        f.write('## cProfiling Results:\n\n')
        f.write(n_numbers+'\n\n')

        s = io.StringIO()
        ps = pstats.Stats(profiler, stream=s).sort_stats('tottime')
        ps.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
        f.write(s.getvalue())
        f.write('\n\n')
        
        s = io.StringIO()
        ps = pstats.Stats(profiler2, stream=s).sort_stats('tottime')
        ps.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()

        f.write(s.getvalue())
        f.write('\n\n')

        s = io.StringIO()
        ps = pstats.Stats(profiler3, stream=s).sort_stats('tottime')
        ps.strip_dirs().sort_stats(SortKey.CUMULATIVE).print_stats()
        f.write(s.getvalue())

        f.write('\n\n')
        f.write('\n\n')
        f.write(f'{formatting_str:_<80}')
        f.write('\n\n')
        f.write('## timeit Results:\n\n')
        f.write('\n\n')

        f.write(f'{ntimes} runs, timeit mysqrt\n\n')
        f.write(timeit_1.__str__())
        f.write('\n\n')

        f.write('vs. proposed optimized solution\n\n')
        f.write(timeit_2.__str__())
        f.write('\n\n')

        f.write('vs. mysqrt_fast implementation\n\n')
        f.write(timeit_3.__str__())
        f.write('\n\n')
        f.write(f'{formatting_str:_<80}')






if __name__ == '__main__':
    main()
