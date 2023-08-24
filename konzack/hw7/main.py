from numpy import random, mean, array, ndarray, sqrt, zeros, exp, concatenate, sum, argsort, apply_along_axis, stack, column_stack, Inf
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from typing import Callable

def initialise(N: int, d: int, x_l: float, x_u: float):
    """
    Initialise a population for a genetic algorithm
    """
    all_x = random.random((N, d)) * (x_u - x_l) + x_l
    all_eta = random.random((N, d)) * (x_u - x_l) + x_l

    return stack((all_x, all_eta), axis=-1)


def evaluate(pop: ndarray, f: Callable) :
    """
    Evaluate the fitness of a population using an objective function
    """

    return - apply_along_axis(f, 1, pop)


def mutate(pop: ndarray) :
    """
    Mutate the given population with gaussian noise
    """

    N, d, _ = pop.shape
    new_pop = zeros(pop.shape)
    tau = 1 / sqrt(2 * sqrt(d))
    tau_prime = 1 / sqrt(2 * d)

    for i in range(N):
        x = pop[i, :, 0]
        eta = pop[i, :, 1]
        x_prime = x + eta * random.normal(size=d) ##COMMENTS: good
        eta_prime = eta * exp(tau_prime * random.normal() + tau * random.normal()) ##COMMENTS be carefull here, check the algo for the secon normal random variable
        # eta_prime = eta * exp(tau_prime * random.normal() + tau * random.normal(size=d))
        new_pop[i] = column_stack([x_prime, eta_prime])

    return new_pop


def select(pop: ndarray, fitnesses: ndarray, q = 10) :
    """
    Select N new agents proportinate to their fitness values.
    Every agent competes with q enemies. Agents with most wins are selected.
    """
    N = int(pop.shape[0] / 2)

    # Count wins for every agent in tournaments
    wins = zeros(len(fitnesses))
    for i, fitness in enumerate(fitnesses):
        row_sample = random.choice(pop.shape[0], q) ## COMMENTS, wrong replace should be False here.
        opponents = pop[row_sample]
        opponent_fitnesses = evaluate(opponents, f)
        wins[i] = sum(opponent_fitnesses < fitness)

    # Select individuals with the most wins
    sorted_indices = argsort(wins)
    selected_pop = pop[sorted_indices][N:]

    return selected_pop


def dea(params: dict):
    """
    Run a differentiable evolutionary algorithm for T iterations.
    Returns the last generation and its mean fitnesses.
    """

    T = params["T"]
    pop = params["init_pop"]

    t = 0

    mean_fitnesses = [mean(evaluate(pop, params['f']))]
    best_fitness = -Inf
    while t < T:
        # 1. Mutate
        pop_prime = mutate(pop)

        # 2. Evaluate
        parents_and_offspring = concatenate((pop, pop_prime), axis=0)
        fitnesses = evaluate(parents_and_offspring, params["f"])

        # 3. Select
        pop = select(parents_and_offspring, fitnesses)

        m = mean(evaluate(pop, params['f']))
        mean_fitnesses += [m]
        print(f"Mean fitness {t} : ", m)

        t += 1

        # Save the best population
        if m > best_fitness:
            best_fitness = m
        best_pop = pop

    return best_pop, mean_fitnesses



def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length' ,type=int, default=1, help= "The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3.,  help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=3.,  help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10,  help='number of mutants for parwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on a standard output " )
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()

def f0(x: ndarray):
    """ sum(x**2) """
    return sum(x**2)

def f1(x: ndarray):
    """ x**4 + x**3 - x**2 - x; x_l = -2; x_u = 2 """
    return x**4 + x**3 - x**2 - x

def f2(x: ndarray):
    """ sum(x**2); n = 30;  x_l = -100;  x_u = 100 """
    return sum(x**2)

def f3(x: ndarray):
    """ sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2); n = 2; x_l = -30; x_u = 30 """
    return sum(100 * (x[1:] - x[:-1]**2)**2 + (x[:-1] - 1)**2)

if __name__ =="__main__":
    args = parseArguments()
    MODE = 3

    match MODE:
        case 0:
            f = f0
        case 1:
            args.xL = -2
            args.xU = 2
            f = f1
        case 2:
            args.length = 30
            args.xL = -100
            args.xU = 100
            f = f2
        case 3:
            args.length = 2
            args.xL = 30
            args.xU = -30
            f = f3

    params = {
        'n' : args.length,
        'T' : args.T ,
        'q' : args.q,
        'N' : args.N,
        'f' : f,
        'verbose': args.verbose,
        'xU': args.xU,
        'xL': args.xL
    }

    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function " + f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()

    mean_best_pop = mean(best_pop, axis=0)[:, 0]
    mean_best_fitness = mean(evaluate(best_pop, f))
    print(f"Mean x of best population: {mean_best_pop} with fitness {mean_best_fitness}")
