from numpy import random, mean, sqrt, concatenate, exp, zeros, argsort, array, argmin
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

from typing import Tuple, List, Callable, Dict, Any
from numpy.typing import NDArray


def initialise(n: int, d: int, x_l: float, x_u: float) -> NDArray:
    """Generate a random initial population

    Parameters:
        n: Population size
        d: Number of dimension of the solution space
        x_l: Lower bound of the solution space
        x_u: Upper bound of the solution space
    
    Returns: Array of shape `(n, 2 * d)` with random values sampled from a uniform distribution
    """
    all_x = random.uniform(low=x_l, high=x_u, size=(n, d))  # objective variables
    all_eta = random.uniform(low=x_l, high=x_u, size=(n, d))  # strategy parameters

    return concatenate((all_x, all_eta), axis=1)


def evaluate(population: NDArray, f: Callable) -> NDArray:
    """Evaluate the fitness of each agent in the population

    Parameters:
        population: Population of agents as an array of shape `(n, 2 * d)`, where `n` is the population size 
            and `d` the dimension of the objective variable
        f: target function of the optimization problem

    Returns: Array of shape `(n,)` containing the fitness for each agent
    """
    d = population.shape[1] // 2

    return array([ f(population[i,:d]) for i in range(population.shape[0]) ])


def mutate(population: NDArray) -> NDArray:
    """Mutate every agent of the population to generate a new population with their offsprings

    Parameters:
        population: Population of agents as an array of shape `(n, d + 1)`, where `n` is the population size 
            and `d` the dimension of the objective variable

    Returns: Copy of the `population` array with the same shape 
    """
    # create copy so that previous population is not changed
    new_population = population.copy()

    n = population.shape[0]  # population size
    d = population.shape[1] // 2  # dimension of objective variable
    tau = 1 / sqrt(2 * sqrt(n))
    tau_prime = 1 / sqrt(2 * n)

    # update objective variables
    new_population[:, :d] = population[:, :d] + population[:, d:] * random.normal(size=(n, d))
    # update strategy parameters
    new_population[:, d:] = population[:, d:] * exp(tau_prime * random.normal(size=(n,1)) + tau * random.normal(size=(n, d)))

    return new_population


def select(population: NDArray, fitness: NDArray, keep: int, q: int = 10) -> NDArray:
    """Select fittest agents from a population by letting each agent compete against `q` opponents. At the end, only
    `keep` agents with the most wins are kept in the final population.

    Parameters:
        population: Population of agents as an array of shape `(n, 2 * d)`, where `n` is the population size 
            and `d` the dimension of the objective variable
        fitness: Array of shape `(n,)` with the fitness score for each agent (lower is better)
        keep: Number of agents that will be selected
        q: Number of randomly picked opponents from the population each agent must compete against
    
    Returns: Population of selected agents as an array of shape `(keep, 2 * d)`
    """
    n = population.shape[0]
    ranking = zeros(n)

    for i in range(population.shape[0]):
        # choose opponents from the entire population (except the agent itself)
        opponents = random.choice([idx for idx in range(population.shape[0]) if idx != i], size=q, replace=False)
        # determine number of wins over the opponents 
        wins = 0
        for j in opponents:
            if fitness[i] < fitness[j]:
                wins += 1
        # write number of wins into the ranking
        ranking[i] = wins

    # get indices of `keep` best agents based on ranking
    best_agents = argsort(ranking)[::-1][:keep]

    return population[best_agents].copy()


def dea(params: Dict[str, Any]) -> Tuple[NDArray, List[float]]:
    """Differential evolution algorithm"""
    prev_population = params["init_pop"]
    n = prev_population.shape[0]  # population size
    mean_fit = []
    for _ in range(params["T"]):
        # compute fitness for each agent of the current population
        prev_fitness = evaluate(prev_population, params["f"])
        mean_fit.append(mean(prev_fitness))

        # mutate entire population to generate "offspring" population
        next_population = mutate(prev_population)
        # compute fitness for each agent of the new population
        next_fitness = evaluate(next_population, params["f"])

        # perform selection on both populations to determine the population for the next iteration
        prev_population = select(
            concatenate((prev_population, next_population)), concatenate((prev_fitness, next_fitness)), n)

    return prev_population, mean_fit


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length' ,type=int, default=1, help= "The dimension of the solution space")
    parser.add_argument("-f", type=str, required=True, help="A function to optimize")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3.,  help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=3.,  help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10,  help='number of mutants for parwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on a standard output " )
    parser.add_argument('--seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main():
    args = parseArguments()
    random.seed(args.seed)
    
    # derive fitness function from command line argument
    f = eval("lambda x: " + args.f)

    params = {
        'n' : args.length,
        'T' : args.T,
        'q' : args.q,
        'N' : args.N,
        'f' : f,
        'verbose': args.verbose,
        'xU': args.xU,
        'xL': args.xL
    }

    # Initialize population
    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    # Run evolutionary algorithm
    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)

    # Determine best solution found so far
    best_x = best_pop[argmin(f(best_pop[:, :args.length]))][:args.length]
    best_fitness = f(best_x)
    print("Best solution:")
    print(f"    x  = {best_x}")
    print(f"  f(x) = {best_fitness}")

    # Plot mean fitness over time
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the objective function")
    plt.xlabel("Generation $t$")
    plt.ylabel("Population mean fitness")
    plt.show()


if __name__ =="__main__" :
    main()