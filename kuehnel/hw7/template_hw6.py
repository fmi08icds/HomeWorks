from numpy import random, mean
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import math


def initialise(N, n, x_l, x_u):
    """
    Initialize N−individuals as a pair of real-valued vectors all_x and all_eta.
    all_x has dimension n and contains the individual information
    (like the genetics) and all_eta contains the step sizes.
    :param N: number of individuals
    :param n: dimensionality of an individual
    :param x_l: lower bound for the uniform distribution
    :param x_u: upper bound for the uniform distribution
    :return: list(zip(all_x, all_eta))
    """
    print(N, n, x_l, x_u)
    i_len = (x_u - x_l)
    all_x = [random.uniform(low=0.0,
                            high=1.0,
                            size=n)*i_len + x_l for i in range(N)]
    print(all_x[0:5])
    print(all_x[0][0:5])
    r_unif = random.uniform(low=0.0, high=1.0, size=N)
    all_eta = r_unif*((x_u - x_l) + x_l)

    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
    The fittness function f is to be minimized!
    :param pop: population (list of tuples)
    :param f: fittness function
    :return:
    """
    print(pop)
    fittness_vals = [f(x[0]) for x in pop]
    print("fittness_vals:\n", fittness_vals)
    return fittness_vals


def mutate(pop):
    """
    Mutate the population (x, eta) to (x_prime, eta_prime),
    where x_prime is the mutated individual information (mutated genes)
    and eta_prime is the adapted step-size
    :param pop: (x, eta) un-mutated individuals x and step-sizes eta
    :return: (x', eta') mutated individuals x' and adapted step-sizes eta'
    """

    n = len(pop[0][0])  # get the dimension of the solution space here.
    N = len(pop)  # the population size

    mutated_pop = [pop[j][0] + pop[j][1] * random.normal(size=n) for j in range(N)] ## COMENTS: very good
    tau = 1. / math.sqrt(2*math.sqrt(n))
    tau_prime = 1. / math.sqrt(2*n)
    vals = tau*random.normal(size=N) + tau_prime*random.normal(size=N)
    eta_prime = [pop[j][1] * math.exp(vals[j]) for j in range(N)]

    return list(zip(mutated_pop, eta_prime))


def select(pop, fitnesses, N, q=10):
    """
    Select N individuals from population pop (containing parents and offspring)
    by doing pairwise comparisons of each individual with q randomly selected
    other individuals. Select the ones which won the most pairwise comparisons.
    :param pop: population (containing parents and offspring)
    :param fitnesses: fittness values of all individuals in pop (same order)
    :param N: number of individuals to be selected
    :param q: number of pairwise comparisons
    :return: selected population (size N)
    """
    sz = len(pop)
    victories = [[i, 0] for i in range(sz)]  # List of victories with indices
    for individual in range(sz):
        opponents = random.randint(0, sz, size=q)
        for opp in opponents:
            if fitnesses[individual] < fitnesses[opp]:
                victories[individual][1] += 1
    victories.sort(key=lambda x: x[1], reverse=True)  # sort by victories
    selected_pop = []
    for i in range(N):
        victor_index = victories[i][0]
        selected_pop.append(pop[victor_index])

    return selected_pop


def dea(params):
    """
    Runs an evolutionary algorithm
    :param params: dictionary of parameters
    :return: (prev_pop, mean_fit) optimized population
    and list of mean fittness values obtained during training
    """

    T = params["T"]
    prev_pop = params["init_pop"]

    t = 0
    fittness_vals = evaluate(prev_pop,params['f'])
    mean_fit = [mean(fittness_vals)]
    while t< T:
        # write your code here to implement the DEA. The steps should be
        # 1. mutate
        mutated_pop = mutate(prev_pop)
        # 2. evaluate
        fittness_vals_of_mutated = evaluate(mutated_pop, params['f'])
        m = mean(fittness_vals_of_mutated)
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)
        t += 1
        # 3. select
        pop = prev_pop + mutated_pop
        pop_fittness = fittness_vals + fittness_vals_of_mutated
        prev_pop = select(pop, pop_fittness, params["N"])

    return prev_pop, mean_fit


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


def main():
    args = parseArguments()
    f = lambda x: sum(x**2)
    f.__doc__ = """sum(x**2)"""
    f_1 = lambda x: x**4 + x**3 - x**2 - x
    f_1.__doc__ = """x**4 + x**3 - x**2 - x"""
    # test f_1 with: python template_hw6.py -n 1 -xL -2 -xU 2
    f_2 = lambda x: sum(x)
    f_2.__doc__ = """sum(x)"""
    # test f_2 with: python template_hw6.py -n 30 -xL -100 -xU 100
    f_3 = lambda x: sum([100*(x[j+1] - x[j]**2)**2 + (x[j] - 1)**2
                         for j in range(len(x)-1)])
    f_3.__doc__ = """sum([100*(x[j+1] - x[j]**2)**2 + (x[j] - 1)**2"""
    # test f_3 with: python template_hw6.py -n 30 -xL -30 -xU 30

    params = {
        'n' : args.length,
        'T' : args.T ,
        'q' : args.q,
        'N' : args.N,
        'f' : f_2,
        'verbose': args.verbose,
        'xU': args.xU,
        'xL': args.xL
    }

    params['init_pop'] = initialise(args.N, args.length, args.xL, args.xU)

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function "+f_2.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()


if __name__ =="__main__" :
    main()
