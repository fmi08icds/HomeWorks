from numpy import random, mean
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N, n, x_l, x_u):
    """
    Initialise the population with N individuals,
    each individual has n-dimension, and each dimension is between x_l and x_u.

    :param N: the population size
    :param n: the dimension of the solution space
    :param x_l: the lower bound of the solution space
    :param x_u: the upper bound of the solution space

    :return: a list of tuples (x, eta) where x is the solution and eta is the direction vector
    """
    all_x = random.uniform(low=x_l, high=x_u, size=(N, n))
    all_eta = random.uniform(low=x_l, high=x_u, size=(N, n))
    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
    Evaluate the fitness of the population by the function f

    :param pop: a list of tuples (x, eta) where x is the solution and eta is the direction vector
    :param f: the objective function

    :return: a list of fitness values
    """

    fitness_value = [f(x[0]) for x in pop]
    return fitness_value


def mutate(pop):
    """
    Perform mutation operation on the population

    :param pop: a list of tuples (x, eta) where x is the solution and eta is the direction vector

    :return: a list of tuples (x', eta') where x' is the mutated solution and eta' is the mutated direction vector
    """
    n = len(pop[0][0])  # get the dimension of the solution space
    N = len(pop)  # the population size

    new_pop = []
    tau = 1 / np.sqrt(2 * n)
    tau_prime = 1 / np.sqrt(2 * np.sqrt(n))

    for xi, eta in pop:
        xi_prime = xi + eta * random.normal(0, 1, n)
        eta_prime = eta * np.exp(
            tau_prime * random.normal(0, 1) + tau * random.normal(0, 1, n)
        )
        new_pop.append((xi_prime, eta_prime))

    return new_pop


def select(pop, fitnesses, N, q=10):
    """
    Select N individuals from the population for reproduction
    based on the fitness score

    :param pop: a list of tuples (x, eta) where x is the solution and eta is the direction vector
    :param fitnesses: a list of fitness values
    :param N: the number of individuals to select
    :param q: the number of individuals to compete in each tournament

    :return: a list of tuples (x, eta) where x is the solution and eta is the direction vector
    """
    num_individuals = len(pop)
    victories = [[i, 0] for i in range(num_individuals)]

    for idx, _ in enumerate(pop):
        opponents = np.random.choice(range(num_individuals), size=q, replace=False)
        victories[idx][1] = sum(fitnesses[idx] < fitnesses[opp] for opp in opponents)

    # Sort by victories in descending order and take the indices
    selected_indices = [
        idx for idx, _ in sorted(victories, key=lambda x: x[1], reverse=True)[:N]
    ]

    # Select the best individuals based on their indices
    selected_population = [pop[i] for i in selected_indices]

    return selected_population


def dea(params):
    """
    The Differential Evolutionary Algorithm

    :param params: a dictionary of parameters

    :return: the best population and the mean fitnesses over the generations
    """
    T = params["T"]
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [np.mean(evaluate(prev_pop, params["f"]))]

    while t < T:
        mutated_pop = mutate(prev_pop)
        total_pop = prev_pop + mutated_pop
        total_fitness = evaluate(total_pop, params["f"])

        prev_pop = select(total_pop, total_fitness, params["N"], params["q"])
        m = np.mean(evaluate(prev_pop, params["f"]))
        mean_fit.append(m)

        if params["verbose"]:
            print(f"Mean fitness at generation {t}: {m}")

        t += 1

    return prev_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS
    )
    parser.add_argument(
        "-n",
        "--length",
        type=int,
        default=1,
        help="The dimension of the solution space",
    )
    parser.add_argument(
        "-T", type=int, default=50, help="Number of generation of the DEA"
    )
    parser.add_argument("-N", type=int, default=100, help="Population size")
    parser.add_argument(
        "-xL", type=float, default=-3.0, help="Lower bound of the the solution space"
    )
    parser.add_argument(
        "-xU", type=float, default=3.0, help="Upper bound of the the solution space"
    )
    parser.add_argument(
        "-q", type=int, default=10, help="number of mutants for parwise comparison"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        default=False,
        help="Print the mean fitness evolution on a standard output ",
    )
    parser.add_argument(
        "-seed", type=int, default=None, help="Seed for the initial population"
    )
    return parser.parse_args()


def main():
    args = parseArguments()

    # Define the three functions to be optimized
    f1 = lambda x: x**4 + x**3 - x**2 - x
    f2 = lambda x: np.sum(x**2)
    f3 = lambda x: np.sum(
        [100 * (x[j + 1] - x[j] ** 2) ** 2 + (x[j] - 1) ** 2 for j in range(len(x) - 1)]
    )

    # Define the parameters for each function
    params1 = {
        "n": 1,
        "T": args.T,
        "q": args.q,
        "N": args.N,
        "f": f1,
        "verbose": args.verbose,
        "xU": 2,
        "xL": -2,
    }
    params2 = {
        "n": 30,
        "T": args.T,
        "q": args.q,
        "N": args.N,
        "f": f2,
        "verbose": args.verbose,
        "xU": 100,
        "xL": -100,
    }
    params3 = {
        "n": 2,
        "T": args.T,
        "q": args.q,
        "N": args.N,
        "f": f3,
        "verbose": args.verbose,
        "xU": 30,
        "xL": -30,
    }

    # Initialize the populations for each set of parameters
    params1["init_pop"] = initialise(args.N, 1, -2, 2)
    params2["init_pop"] = initialise(args.N, 30, -100, 100)
    params3["init_pop"] = initialise(args.N, 30, -30, 30)

    # Run the DEA algorithm for each set of parameters and plot the results
    for i, params in enumerate([params1, params2, params3], start=1):
        best_pop, mean_fitnesses = dea(params)
        print(f"Best population for function {i}: ", best_pop)
        plt.figure(i)
        plt.plot(mean_fitnesses, "o-")
        plt.title(f"Optimization of the function {i}")
        plt.xlabel("Generation(t)")
        plt.ylabel("Population mean fitness")
        plt.show()


if __name__ == "__main__":
    main()
