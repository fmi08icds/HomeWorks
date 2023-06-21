from numpy import random, mean
from itertools import chain
import random
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import inspect


def initialise(N, n, x_l, x_u):
    """
    Generates the initial population using the provided bounds and shape of the
    solution space.

    Args:
        N: Population size
        n: The dimension of the solution space
        x_l: Lower bound of the solution space
        x_u: Upper bound of the solution space
    Returns:
        A list of paris of numpy arrays. A single array in a pair has the dimension
        of n. The first element of a pair presents an individual's objective
        variables and the second element its standard deviations. The returned list
        as a whole represents a population.
    """

    all_x = np.random.rand(N, n) * (x_u - x_l) + x_l
    all_eta = np.random.rand(N, n) * (x_u - x_l) + x_l

    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
    Evaluates for each individual of a population the function f.
    To generate the fitness of an individual, the evaluation is inverted.

    Args
        pop: The population that should be evaluated
    Returns:
        A list of evaluations
    """

    return [f(x[0]) for x in pop]


def mutate(pop):
    """
    Mutates each individual of the given population. Mutation serves as a measurement
    of exploration in the search space. Each individual of the given population gets its
    objective values and standard deviations mutated.

    Args:
        pop: The population that should be mutated.
    Returns:
        The mutated population as a list of individuals.

    """

    n = len(pop[0][0])  # get the dimension of the solution space here.
    N = len(pop)  # the population size
    new_pop = []
    tau = np.power(np.sqrt(2 * np.sqrt(n)), -1)
    tau_prime = np.power(np.sqrt(2 * n), -1)

    for individual in pop:
        x_new = individual[0] + individual[1] * np.random.normal(0, 1)
        eta_new = individual[1] * np.exp(
            tau_prime * np.random.normal(0, 1) + tau * np.random.normal(0, 1, n)
        )
        new_pop.append((x_new, eta_new))

    return new_pop


def select(parents, children, parents_fitness, children_fitness, N, q=10):
    """
    The selection step compares individuals with each other based on their fitness.
    Each individual is compared to a set of randomly drawn opponents. Opponents are
    also individuals, originating from parents and children. The N best performing A
    individuals build the next performance. Best performing is a measurement of count
    of an individuals total wins against its opponents. A win is defined as having a
    lower fitness

    Args:
        parents: The current parent population
        children: The current children population
        parents_fitness: The fitness of the current parent population
        children_fitness: The fitness of the current children population
        N: The amount of best performing individuals that form the new population
        q: The number of opponents of an individual that should be drawn
    """
    parents_with_fitness = zip(parents, parents_fitness)
    children_with_fitness = zip(children, children_fitness)
    union_of_parents_and_children = list(
        chain(parents_with_fitness, children_with_fitness)
    )

    winner_counts = {}
    for i in range(len(union_of_parents_and_children)):
        individual = union_of_parents_and_children[i]
        opponents = random.sample(union_of_parents_and_children, q)
        wins = sum([individual[1] < opponent[1] for opponent in opponents])
        winner_counts[i] = wins

    sorted_winner_counts = sorted(
        winner_counts.items(), key=lambda x: x[1], reverse=True
    )[:N]

    return [
        union_of_parents_and_children[winner_idx][0]
        for winner_idx, _ in sorted_winner_counts
    ]


def dea(params):
    """
    This function optimizes the given target function by using a differential 
    evolutionary algorithm. The algorithm consists of the following steps:
    1. Generate the initial population of N individuals or agents P_t.
    2. Evaluate the Fitness of each individual
    3. Mutate the population P_t to generate a new population P'_t
    4. Select N individual from P_t ∪ P'_t proportionally to their fitnesses.
        The selected individuals will reproduce to the next generation
        and form a new population Pt+1
    5. Stop if the halting criterion is satisfied; otherwise, t = t + 1 and
        go to step 2.

    Args:
        params: A dictionary configuring the differential evolutionary algorithm.
    """

    parents = params["init_pop"]
    parents_fitness = evaluate(parents, params["f"])

    t = 0
    m = mean(parents_fitness)
    mean_fit = [m]
    print(f"Initial mean fitness: ", m)

    while t < params["T"]:
        children = mutate(parents)
        children_fitness = evaluate(children, params["f"])

        parents = select(
            parents,
            children,
            parents_fitness,
            children_fitness,
            params["N"],
            params["q"],
        )
        parents_fitness = evaluate(parents, params["f"])

        m = mean(parents_fitness)
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)
        t += 1
    return parents, mean_fit


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
        "-q", type=int, default=10, help="number of mutants for pairwise comparison"
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
    # f = lambda x: x**4 + x**3 - x**2 - x
    f = lambda x: sum([x_j**2 for x_j in x])
    # f = lambda x: sum([ 100*(x[j+1] - x[j]**2)**2 + (x[j]-1)**2 for j in range(len(x)-1)])

    params = {
        "n": args.length,
        "T": args.T,
        "q": args.q,
        "N": args.N,
        "f": f,
        "verbose": args.verbose,
        "xU": args.xU,
        "xL": args.xL,
    }

    params["init_pop"] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title(f"Optimization of the function {inspect.getsource(f)}")
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.savefig(f'plot{inspect.getsource(f).replace(" ","_")}.png')


if __name__ == "__main__":
    main()
