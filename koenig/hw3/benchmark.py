import timeit


def main():
    """
    Benchmarking application for multiple implementations of sqrt
    """
    # Use the following when the naive method!
    # numbers_to_test = [ 1200, 2400, 4800, 9600, 19200, 38400]
    # Use the following only, if the naive method is not activated!
    numbers_to_test = [300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 76800, 900000, 2000000]

    # Use with the naive method!
    # repetitions = 10

    repetitions = 100

    print("n       ",
          # "sqrt_naive",
          "sqrt_optimized",
          "sqrt_optimized_vec",
          "sqrt_bin_search",
          "np.sqrt", sep="\t")
    for n in numbers_to_test:
        print('{:>5}'.format(n),
              # Naive Method: this is the file template1_hw.py with just the None replaced
              ###########################################################################
              #"{:10.5f}".format(timeit.timeit("sqrt_naive.mysqrt(n)",
              #                                setup=f"""import koenig.hw3.sqrt_naive as sqrt_naive; n={n}""",
              #                                number=repetitions)),
              # Improved / optimized method with *no* vectorizations via numpy
              ############################################################################
              "{:10.5f}".format(timeit.timeit("sqrt_improved.mysqrt(n)",
                                              setup=f"""import koenig.hw3.sqrt_improved as sqrt_improved; n={n}""",
                                              number=repetitions)),
              # Improved / optimized method *with* vectorizations via numpy
              ############################################################################
              "{:10.5f}".format(timeit.timeit("sqrt_improved.mysqrt(n)",
                                              setup=f"""import koenig.hw3.sqrt_improved_vec as sqrt_improved; n={n}""",
                                              number=repetitions)),
              # Improved / optimized method *with* pure binary search
              ############################################################################
              "{:10.5f}".format(timeit.timeit("sqrt_improved.mysqrt(n)",
                                              setup=f"""import koenig.hw3.sqrt_bin_search as sqrt_improved; n={n}""",
                                              number=repetitions)),
              # For comparison: native numpy.sqrt method
              ############################################################################
              "{:10.5f}".format(timeit.timeit("np.sqrt(n)",
                                              setup=f"""import numpy as np; n={n}""",
                                              number=repetitions)),
              sep="\t")


if __name__ == '__main__':
    main()
