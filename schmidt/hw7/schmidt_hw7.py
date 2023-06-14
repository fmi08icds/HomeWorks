from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import numpy as np
from matplotlib import pyplot as plt
from numpy.typing import NDArray
from typing import Callable, Dict, Tuple


def initialise(N: int, n: int, x_l: float, x_u: float) -> Tuple[NDArray, NDArray]:
    """
    Initialise the population for the differential evolutionary algorithm.

    :param N:       Population size
    :param n:       The dimension of the solution space
    :param x_l:     Lower bound of the solution space
    :param x_u:     Upper bound of the solution space

    :return:        A tuple for the population containing two numpy arrays:
                    One for the populations x values, and the other their eta values
    """
    # Create a random population within bounds x_l and x_u and initialize the eta values (strategy parameters)
    # for all individuals
    all_x = np.random.uniform(x_l, x_u, size=(N, n))
    all_eta = np.random.uniform(x_l, x_u, size=(N, 1))
    return all_x, all_eta


def evaluate(pop: Tuple[NDArray, NDArray], f: Callable) -> NDArray:
    """
    Calculate the fitness values of all individuals in the population.

    :param: pop:    The population's individuals as a tuple of numpy arrays (objective variables, strategy parameters)
    :param f:       The objective function to evaluate the fitness

    :return:        An array of fitness values for all individuals in the population
    """
    fitness_values = np.apply_along_axis(f, 1, pop[0])
    return fitness_values


def mutate(pop: Tuple[NDArray, NDArray]) -> Tuple[NDArray, NDArray]:
    """
    Mutate the individuals of a population using their strategy parameters eta
    :param pop:     The population's individuals as a tuple of numpy arrays (objective variables, strategy parameters)
    :return:        A mutated population as a tuple of two arrays:
                    One for the populations x values, and the other their eta values
    """
    # Get the individual components
    old_x, old_eta = pop

    # Get the population size and the dimension of the solution space
    N, n = old_x.shape

    # Set values for tau and tau prime
    tau = 1 / (np.sqrt(2 * np.sqrt(n)))
    tau_prime = 1 / (np.sqrt(2 * n))

    # Get the new population by random mutations using the eta values and standard normal distribution
    new_x = old_x + old_eta * np.random.normal(loc=0.0, scale=1.0, size=(N, n))
    new_eta = old_eta * np.exp(tau_prime * np.random.normal(loc=0.0, scale=1.0, size=(N, 1)) +
                               tau * np.random.normal(loc=0.0, scale=1.0, size=(N, 1)))

    return new_x, new_eta


def select(pop: Tuple[NDArray, NDArray], fitness_values: NDArray, N: int, q=10):
    """
    :param pop:             The population's individuals as a tuple of numpy arrays
                            (objective variables, strategy parameters)
    :param fitness_values:  The fitness values for all individuals
    :param N:               Number of individuals to be selected for the next iteration
    :param q:               Number of opponents to compare an individual against
    :return:                Tuple of arrays corresponding to the N individuals with the most wins against opponents
    """
    wins = np.zeros_like(fitness_values)
    for i, fitness in enumerate(fitness_values):
        # Choose q opponents uniformly at random;
        # Count wins by summing over opponents for which the individuals fitness is lower
        opponents_idx = np.random.choice(len(fitness_values), size=q, replace=False)
        wins[i] = np.sum(fitness < fitness_values[j] for j in opponents_idx)

    # Get the indices of N individuals having the most wins; [::-1] to get descending order
    selection_idx = np.argsort(wins)[::-1][:N]

    # Create the new population using the selection indices
    return (pop[0][selection_idx], pop[1][selection_idx])


def dea(params: Dict):
    """
    Perform differential evolutionary algorithm given a dictionary of parameters
    :param params:
    :return:
    """
    T = params['T']
    prev_pop = params["init_pop"]
    t = 0

    mean_fit = [np.mean(evaluate(prev_pop, params['f']))]
    while t < T:
        # 1. Get the mutations and create a larger population for selection (new and previous pop)
        new_pop = mutate(prev_pop)
        evaluation_pop = (np.concatenate((prev_pop[0], new_pop[0]), axis=0),
                          np.concatenate((prev_pop[1], new_pop[1]), axis=0))
        # 2. Calculate fitness values
        fitness_values = evaluate(pop=evaluation_pop, f=params['f'])

        # 3. Select the new population out of new and previous population
        prev_pop = select(pop=evaluation_pop, fitness_values=fitness_values, N=params['N'], q=params['q'])

        # 4. Print the mean fitness if verbose
        m = np.mean(evaluate(prev_pop, params['f']))
        mean_fit += [m]
        if params['verbose']:
            print(f"Mean fitness {t} : ", m)

        t += 1

    return prev_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1, help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3., help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=3., help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10, help='number of mutants for parwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False,
                        help="Print the mean fitness evolution on a standard output ")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main():
    args = parseArguments()
    f = lambda x: sum(x**2)  # Here you will define your objective function

    params = {'n': args.length, 'T': args.T, 'q': args.q, 'N': args.N, 'f': f, 'verbose': args.verbose, 'xU': args.xU,
              'xL': args.xL, 'init_pop': initialise(args.N, args.length, args.xL, args.xU)}

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    # Todo: Fix function printing
    plt.title(f"Optimization of the function {f.__doc__}")
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()


if __name__ == "__main__":
    main()
