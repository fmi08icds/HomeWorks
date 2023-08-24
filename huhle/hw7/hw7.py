import numpy as np
from numpy import mean
import matplotlib.pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from typing import Callable

def initialise(N: int, n: int, x_l: float, x_u: float):
    """
    Generate initial population for a genetic algorithm
    """
    all_x = np.random.uniform(x_l, x_u, size=(N, n))
    all_eta = np.random.uniform(x_l, x_u, size=(N, n))

    return np.stack((all_x, all_eta), axis=-1)


def evaluate(pop: np.ndarray, f: Callable) -> np.ndarray:
    """
    Evaluate the fitness of the population using an objective function
    """
    return -np.apply_along_axis(f, 1, pop)


def mutate(pop: np.ndarray) -> np.ndarray:
    """
    Mutate the population by adding Gaussian noise
    """

    N, n, _ = pop.shape
    tau = 1 / np.sqrt(2 * np.sqrt(n))
    tau_prime = 1 / np.sqrt(2 * n)

    new_pop = np.zeros(pop.shape)

    for i in range(N):
        x = pop[i, :, 0] # Good
        eta = pop[i, :, 1]

        x_prime = x + eta * np.random.normal() # the random normal number should be drawn for each xj in x. the same applies to the next operation for the last random normal number.
        eta_prime = eta * np.exp(tau_prime * np.random.normal() + tau * np.random.normal())

        new_pop[i] = np.array([[*x_prime, *eta_prime]])

    return new_pop



def select(pop: np.ndarray, fitnesses: np.ndarray, q: int = 10) -> np.ndarray:
    """
    Select new individuals from the population based on their fitness values. Set up tournaments where
    each individual competes against a number of opponents, and the individuals with the most wins are selected.
    """
    N = int(pop.shape[0] / 2) # this could have been an input parameter as well with default value N.
    wins = np.zeros(len(fitnesses))

    for i, fitness in enumerate(fitnesses):
        random_indices = np.random.choice(pop.shape[0], size=q, replace=False)# Good
        opponents = pop[random_indices]
        wins[i] = np.sum(opponents < fitness)

    sorted_indices = np.argsort(wins) #Good but in the three test cases we wre minimising...
    selected_pop = pop[sorted_indices][N:] # Good

    return selected_pop


def dea(params: dict) -> np.ndarray:
    """
    Run a differentiable evolutionary algorithm for T iterations, performing mutation, evaluation,
    and selection steps in a loop. Update the population and collect the mean fitness values meanwhile.
    """
    T = params["T"]
    pop = params["init_pop"]

    t = 0
    mean_fit = [np.mean(evaluate(pop, params['f']))]
    while t < T:
        # 1. mutate
        pop_prime = mutate(pop)

        # 2. evaluate
        parents_and_offspring = np.concatenate((pop, pop_prime), axis=0)
        fitnesses = evaluate(parents_and_offspring, params["f"])

        # 3. select
        pop = select(parents_and_offspring, fitnesses)


        mean_fit.append(mean(evaluate(pop, params['f'])))
        print(f"Mean fitness {t}: {mean_fit}")

        t += 1

    return pop, mean_fit



def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length' ,type=int, default=1, help= "The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3.,  help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=3.,  help='Upper bound of the solution space')
    parser.add_argument('-q', type=int, default=10,  help='Number of mutants for pairwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on standard output")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main():
    args = parseArguments()
    np.random.seed(args.seed)

    # f1:
    f = lambda x: np.sum(x)
    f.__doc__ = "sum(x)"

    # f2:
    # f = lambda x: sum(x**2)
    # f.__doc__ = "sum(x**2)"

    # f3:
    # f = lambda x: x**4 + x**3 - x**2 - x
    # f.__doc__ = "x**4 + x**3 - x**2 - x"

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

    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population:", best_pop)

    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function " + f.__doc__)
    plt.xlabel("Generation (t)")
    plt.ylabel("Population mean fitness")
    # plt.savefig("f1")
    # plt.savefig("f2")
    # plt.savefig("f3")
    plt.show()


if __name__ == "__main__":
    main()
