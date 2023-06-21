import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

def initialise(N, n, x_l, x_u):
    """
    Initialize the population.

    Parameters:
    - N: Population size
    - n: Dimension of the solution space
    - x_l: Lower bound of the solution space
    - x_u: Upper bound of the solution space

    Returns:
    - List of tuples representing the initial population
    """
    all_x = np.random.uniform(x_l, x_u, size=(N, n))
    all_eta = np.zeros(N)  # Placeholder for fitness values

    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
    Evaluate the fitness of the population.

    Parameters:
    - pop: List of tuples representing the population
    - f: Objective function

    Returns:
    - List of fitness values for the population
    """
    fitnesses = [f(x) for x, _ in pop]
    return fitnesses


def mutate(pop):
    """
    Perform mutation on the population.

    Parameters:
    - pop: List of tuples representing the population

    Returns:
    - New population after mutation
    """
    n = len(pop[0][0])  # Dimension of the solution space
    N = len(pop)  # Population size
    new_pop = []

    for i in range(N):
        x, _ = pop[i]
        tau = 1.0 / np.sqrt(2 * n)
        tau_prime = 1.0 / np.sqrt(2 * np.sqrt(n))
        x_mutated = x + tau * np.random.normal(size=n) + tau_prime * np.random.normal(size=n)
        new_pop.append((x_mutated, None))

    return new_pop


def select(pop, fitnesses, N, q=10):
    """
    Select individuals from the population.

    Parameters:
    - pop: List of tuples representing the population
    - fitnesses: List of fitness values for the population
    - N: Population size
    - q: Number of mutants for pairwise comparison

    Returns:
    - Selected population
    """
    selected_pop = []

    for i in range(N):
        idx = np.random.choice(N, q, replace=False)  # Select q distinct indices
        idx = np.append(idx, i)  # Add the current individual index
        best_idx = np.argmax(np.array(fitnesses)[idx])  # Index of the best individual
        selected_pop.append(pop[best_idx])

    return selected_pop


def dea(params):
    """
    Differential Evolution Algorithm.

    Parameters:
    - params: Dictionary containing algorithm parameters

    Returns:
    - Best population found
    - List of mean fitness values over generations
    """
    T = params['T']  # Number of generations
    prev_pop = params['init_pop']

    t = 0
    mean_fit = [np.mean(evaluate(prev_pop, params['f']))]
    while t < T:
        prev_pop = mutate(prev_pop)
        fitnesses = evaluate(prev_pop, params['f'])
        prev_pop = select(prev_pop, fitnesses, params['N'], params['q'])
        m = np.mean(fitnesses)
        mean_fit.append(m)
        print(f"Mean fitness {t}: {m}")
        t += 1

    return prev_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1, help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generations of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3.0, help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=3.0, help='Upper bound of the solution space')
    parser.add_argument('-q', type=int, default=10, help='Number of mutants for pairwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on standard output")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main():
    args = parseArguments()
    f1 = lambda x: x**4 + x**3 - x**2 - x
    f2 = lambda x: np.asarray([x_i**2 for x_i in x]).sum()
    f3 = lambda x: np.asarray([100*(x[i+1]-x[i]**2)**2 + (x[i]-1)**2 for i in range(len(x)-1)]).sum()

    # Choose the desired objective function
    f = f1  # Change this to f2 or f3 to use a different function

    params = {
        'n': args.length,
        'T': args.T,
        'q': args.q,
        'N': args.N,
        'f': f,
        'verbose': args.verbose,
        'xU': args.xU,
        'xL': args.xL
    }

    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population: ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function")
    plt.xlabel("Generation (t)")
    plt.ylabel("Population mean fitness")
    plt.show()


if __name__ == "__main__":
    main()
