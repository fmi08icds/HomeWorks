import timeit


def main():
    """
    Benchmarking application for multiple implementations to calculate_Pi
    """

    repetitions = 100*100
    number_of_datapoints = [125, 250, 500, 1000]

    print("| n       ",
          " non_vector (s) ",
          " vector (s) |", sep="|")
    print("|-------- ",
          "---------------",
          "------------|", sep="|")
    for n in number_of_datapoints:
        print('| {:>5}   '.format(n),
              # For comparison: non-vectorized version
              ############################################################################
              "{:10.5f} ".format(timeit.timeit("calc_pi.calculate_pi_non_vector(n)",
                                              setup=f"""import koenig.hw4.calc_pi as calc_pi; n={n}""",
                                              number=repetitions)),
              # For comparison: numpy vectorized version
              ############################################################################
              "{:10.5f} |".format(timeit.timeit("calc_pi.calculate_pi_vector(n)",
                                              setup=f"""import koenig.hw4.calc_pi as calc_pi; n={n}""",
                                              number=repetitions)),
              sep="|")


if __name__ == '__main__':
    main()
