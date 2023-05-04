import cProfile
import numpy as np
import template_hw2
import template_hw2_optimized
import pstats
from pstats import SortKey
import timeit
import io

def main() :
    #size of simulation
    M = 2000
    # size of simulated points
    N = 100000
    n_numbers= f'Test for m={M} times with n={N} number of simulated points.'

    profiler = cProfile.Profile()
    profiler.enable()
    for i in np.arange(M):
        template_hw2.pi_approximation(N)
    profiler.disable()
    profiler.dump_stats("./hw4/template.stats")

    profiler2 = cProfile.Profile()
    profiler2.enable()
    for i in np.arange(M):
        template_hw2_optimized.pi_approximation_vec(N)
    profiler2.disable()
    profiler2.dump_stats("./hw4/template_optimized.stats")
     
    ### approach 2, timeit:
    ntimes = 500
    timeit_1=(timeit.timeit(number=ntimes, setup='import template_hw2', stmt='template_hw2.pi_approximation(100)'))
    timeit_2=(timeit.timeit(number=ntimes, setup='import template_hw2_optimized', stmt='template_hw2_optimized.pi_approximation_vec(100)'))


    with open("./hw4/stats_out.txt", "w") as f:
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

        f.write(f'{formatting_str:_<80}')




if __name__ == '__main__':
    main()
