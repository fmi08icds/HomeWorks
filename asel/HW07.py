""" HW07.py Differential Evolutionary Algorithm tests following functions:

 1. sum(x**2)
 2."Rosenbrock"
 3. x**4 + x**3 - x**2 -x

"""



import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N, n, x_l, x_u):
    """
    Initialize the population

    Parameters:
        N: population size
        n: dimension of the solution space
        x_l: lower bound of the solution space
        x_u: upper bound of the solution space

    Returns:
        init_po: Initial population of shape (N, n)
    """
    init_po = np.random.uniform(x_l, x_u, (N, n))
    all_eta = np.zeros((N, n)) ## COMMENTS: wrong! Please, check the assignment instructions.
    return init_po ## COMMENTS: what about the etas?


def evaluate(pop, func):
    """
    Evaluate the fitness of each individual in the population

    Parameters:
        pop: population of shape (N, n)
        f: Objective function to evaluate the fitness

    Returns:
        result: fitness values for each individual in the population
    """
    result = np.array([func(x) for x in pop])
    return result


def mutate(pop):
    """
    Apply mutation operator to population

    Parameters:
        pop: population of shape (N, n)

    Returns:
        new_pop: new population after mutation of shape (N, n)
"""
    N, n = np.shape(pop)  # Get the shape of pop as a NumPy array
    new_pop = np.zeros_like(pop)
    tau = (np.sqrt(2*np.sqrt(n)))**-1
    tau_prime = (np.sqrt(2*n))**-1

    for i in range(N):
        a, b, c = np.random.choice(N, 3, replace=False) ## COMMENTS: wrong, please check the algorithm in the slides
        eta = np.random.uniform(-tau, tau, n)
        new_pop[i] = pop[a] + tau_prime * (pop[b] - pop[c]) + eta
    return new_pop



def select(pop, fitnesses, N, q=10):
    """
    Select individuals from the population based on fitness

    Parameters:
        pop: population of shape (N, n)
        fitnesses: fitness values for each individual in the population
        N: population size
        q: number of mutants for pairwise comparison

    Returns:
        selected_pop: Selected individuals from the population.
    """
    selected_pop = []
    sorted_indices = np.argsort(fitnesses)
    for i in range(N):
        indices = np.random.choice(sorted_indices[:q], 2, replace=False) ## COMMENTS: wrong implementation
        if fitnesses[indices[0]] > fitnesses[indices[1]]:
            selected_pop.append(pop[indices[0]])
        else:
            selected_pop.append(pop[indices[1]])
    return selected_pop


def dea(params):
    """
    Differential Evolutionary Algorithm (DEA)

    Parameters:
        params: dictionary containing the DEA parameters

    Returns:
        prev_pop, mean_fit: final population and list of mean fitness values over generations
    """
    T = params["T"]
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [np.mean(evaluate(prev_pop, params['f']))]
    while t < T:
        prev_pop = mutate(prev_pop)
        fitnesses = evaluate(prev_pop, params['f'])
        prev_pop = select(prev_pop, fitnesses, params['N'], params['q'])

        m = np.mean(fitnesses)
        mean_fit.append(m)
        if params['verbose']:
            print(f"Mean fitness {t}: ", m)

        t += 1
    return prev_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=30, help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generations of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-100., help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=100., help='Upper bound of the solution space')
    parser.add_argument('-q', type=int, default=10, help='Number of mutants for pairwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False,
                        help="Print the mean fitness evolution on standard output")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args().__dict__

def main():
    args = parseArguments()
    f = lambda x: sum(x ** 2)  # Define your objective function here
    f.__doc__ = "sum(x**2)"

    #f = lambda x: sum(100 * (x[j + 1] - x[j] ** 2) ** 2 + (x[j] - 1) ** 2 for j in range(len(x) - 1))
    #f.__doc__ = "Rosenbrock"

    #f = lambda x: x**4 + x**3 - x**2 - x
    #f.__doc__ = "x**4 + x**3 - x**2 -x"

    params = {
        'n': args['length'],
        'T': args['T'],
        'q': args['q'],
        'N': args['N'],
        'f': f,
        'verbose': args['verbose'],
        'xU': args['xU'],
        'xL': args['xL']
    }

    np.random.seed(args['seed'])
    params['init_pop'] = initialise(args['N'], args['length'], args['xL'], args['xU'])

    best_pop, mean_fitnesses = dea(params)
    print("Best population:", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function " + f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()

if __name__ == "__main__":
    main()
