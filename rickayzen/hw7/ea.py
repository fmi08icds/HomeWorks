import sys

import numpy as np
from numpy import random, mean
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import math
import itertools


def initialise(N, n, x_l, x_u):
    """
        Initialises the population for the evolutionary algorithm
        :param N: the size of the population
        :param n: the size of the vector x
        :param x_l: Lower bound of the generated values
        :param x_u: upper bound of the generated values
        :return: A list of N tuples (x,eta) with  and eta being vectors of length n and every value of x and eta being values between x_l and x_u
    """
    all_x = []
    all_eta = []
    def get_rand_val(l, u): return random.random() * (u - l) + l
    for i in range(N):
        all_x.append([get_rand_val(x_l, x_u) for j in range(n)])
        all_eta.append([get_rand_val(x_l, x_u) for j in range(n)])
    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
        Evaluates the fitness-score by calculating the function f for the elements in the population
    """
    if len(pop[0][0]) == 1:
        return [f(element[0]) for element, eta in pop]
    else:
        return [f(element) for element, eta in pop]



def mutate(pop):
    """
        Generates for each element of the population a mutated value.
    """

    N = len(pop)  # get the dimension of the solution space here.

    if not hasattr(pop[0][0], "len"):
        n = 1
    else:
        n = len(pop[0][0])
    new_pop = []
    tau = math.sqrt(2*math.sqrt(n))**-1  #
    tau_prime = math.sqrt(2*n)**-1  #

    for i in range(N):
        x_i, eta_i = pop[i]
        normal_sample = random.normal()
        x_i_prime = [x_ij + eta_i[index] * random.normal() for index, x_ij in enumerate(x_i)]
        eta_i_prime = [eta_ij * math.exp(tau_prime * normal_sample + tau + random.normal()) for eta_ij in pop[i][1]]
        new_pop.append((x_i_prime, eta_i_prime))
    return new_pop


def select(pop, fitnesses, N, q=10):
    """
        Choses a set of ideal candidates as the new population by comparing each value in pop with q random opponents in pairs. The candidates with the most wins will be chosen.
        :param pop: A zipped list consisting of size N. The elements are tuples of (parent, child) with each being another tuple of (x,eta)
        :param fitnesses: The fitness function which receives a value x as its input. The fitness function should return lower function for better scores
        :param N: The size of the target population. It has to be the same as the parent's and children's population
        :param q: The amount of competitors that each element competes against. Default value is 10
        :returns: The selected, improved population. Consists of a subset of the union of the children's and parent's population
    """
    selected_pop = []
    # wins_pop is a list of tuples (wins, candidate)
    wins_pop = []
    if len(pop) != N:
        raise ValueError(f"you kind of messed up, mate. N has to be the same as the length of the population. N: {N}, length parent: {len(pop)}")
    for i in range(N):
        for j in range(2):
            fitness = fitnesses[i][j]
            wins = 0
            indices = list(itertools.product(range(N),[0,1]))
            indices.remove((i,j))
            # shuffle alters the argument and returns None
            random.shuffle(indices)
            for k in range(q):
                if k >= len(indices):
                    break
                if fitness < fitnesses[indices[k][0]][indices[k][1]]:
                    wins += 1
            wins_pop.append((wins, pop[i][j]))
    selected_pop = sorted(wins_pop, reverse=True)[:N]
    # only select the second column (throw out wins)
    selected_pop = [x for ignore, x in selected_pop]
    return selected_pop


def dea(params):
    """Performs the evolutionary algorithm. It gets parameters as its input and returns the final population as well as the list of the mean fitness of each iteration. Per iteration the mean fitness scores get printed.
    The algorithm works by starting from the initial population init_pop. The populations have the size N and each candidate has the dimention n. Out of these, the children population gets created by applying the mutate function on it.
    The parents and children both get evaluated through the evaluate function which selects f as the fitness function. Finally, the select function selects the N fittest candidates as the new parents population by comparing each candidate with q competitors. This (minus the initialisation step (obviously)) gets repeated T times to get the final population.
    :param params: params is a structure that contains the properties init_pop, N, T, f, q with the characteristics as described above.
    :returns: It returns a tuple consisting of the finally chosen population and the list of mean fitness score per iteration.

    """

    T = params["T"]  # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]
    parents = prev_pop
    t = 0
    mean_fit = [mean(evaluate(prev_pop, params['f']))]
    while t < T:
        ## write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        children = mutate(parents)
        fit_parents = evaluate(parents, params['f'])
        fit_children = evaluate(children, params['f'])
        pop = list(zip(parents, children))
        fitnesses = list(zip(fit_parents, fit_children))
        parents = select(pop, fitnesses, params['N'], params['q'])
        m = mean(evaluate(parents, params['f']))
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)

        t += 1
    return parents, mean_fit


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1, help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3., help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=3., help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10, help='number of mutants for parwise comparison')
    parser.add_argument('-f', type=int, default=1, help='function to be minimised. Accepted values are 1, 2 and 3')
    parser.add_argument('--verbose', action="store_true", default=False,
                        help="Print the mean fitness evolution on a standard output ")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main():
    args = parseArguments()
    if args.f == 1:
        f = lambda x: x**4 + x**3 - x**2 - x  # Here you will define your objective function
        f.__doc__ = "x**4 + x**3 - x**2 -x"
    elif args.f == 2:
        f = lambda x: np.asarray([x_i**2 for x_i in x]).sum()  # Here you will define your objective function
        f.__doc__ = "sum_i^n(x_i²)"
    elif args.f == 3:
        f = lambda x: np.asarray([100*(x[i+1]-x[i]**2)**2 + (x[i]-1)**2 for i in range(len(x)-1)]).sum()  # Here you will define your objective function
        f.__doc__ = "sum_i^n(100(x_(i-1)-x_i^2)+(x_i-1)^2)"
    else:
        raise ValueError(f"Illegal argument f. Optional argument f must be in {1,2,3} but it was {args.f}")
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
    if args.seed is not None:
        random.seed(args.seed)
    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.figure("Everything")
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function " + f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.ylim(0, 1.2*max(mean_fitnesses))

    # plt.figure("Limited to 10000")
    # plt.plot(mean_fitnesses, "o-")
    # plt.title("Optimization of the function " + f.__doc__)
    # plt.xlabel("Generation(t)")
    # plt.ylabel("Population mean fitness")
    # plt.ylim(0, 10000)
    plt.show()


if __name__ == "__main__":
    main()
