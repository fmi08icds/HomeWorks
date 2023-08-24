from numpy import random, mean, std
from math import sqrt, exp
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N, n, x_l, x_u):
    """
        Initialise population with random values in the range of [x_l, x_u]
        Initialise the standard deviation of all_x
    """
    all_x = random.uniform(low=x_l, high=x_u, size=(N, n))
    eta = std(all_x, axis=0)
    all_eta = [eta] * N

    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
        evaluate the fitness of each individual of the population with the selected function of the three possible functions
    """
    fitnesses = []
    for x, eta in pop:
        fitness = f(x)
        fitnesses.append(fitness)
    return fitnesses


def mutate(pop):
    """
        Mutate the population with the formula for objective variables and strategy parameters seen on slide 14
    """
    n = len(pop[0][0])  # get the dimension of the solution space here.
    N = len(pop)  # the population size
    new_pop = []
    tau = (sqrt(2*sqrt(n)))**-1
    tau_prime = (sqrt(2*n))**-1

    for i in range(N):
        individual = pop[i][0]
        eta = pop[i][1]
        m_individual = individual + eta * random.random() # be careful here, it's a normal distribution not uniform.
        m_eta = eta * exp(tau_prime*random.random() + tau*random.random()) # the same problem here normal instead of uniform dist.
        new_pop.append((m_individual, m_eta))

    return new_pop


def select(pop, fitnesses, N, q=10):
    """
        select the individuals with the highest fitnesses compared to q other random individuals
    """
    selected_pop = []
    fitnesses_ranking = [0] * len(pop)
    for i in range(0, len(pop)):
        fitnessess_indices = random.choice(
            len(fitnesses), size=q) # be careful here, we want to draw q individuals uniformly at random without replacement. consider using np.random.sample instead
        for fi in fitnessess_indices:
            if abs(fitnesses[i]) < abs(fitnesses[fi]):
                fitnesses_ranking[i] += 1
    top_indices = sorted(range(len(fitnesses_ranking)),
                         key=lambda i: fitnesses_ranking[i], reverse=True)[:N]
    selected_pop = [pop[i] for i in top_indices]

    return selected_pop


def dea(params):
    """
        Runs the Differential Evolution Algorithm for T generations.
        Contains the processing steps of mutation, evaluation and selection.
        Returning the final population and its mean fitness.
    """

    T = params['T']  # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [mean(evaluate(prev_pop, params['f']))]
    while t < T:
        # write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        new_pop = mutate(prev_pop)
        prev_fit = evaluate(prev_pop, params['f'])
        new_fit = evaluate(new_pop, params['f'])
        prev_pop = select(prev_pop+new_pop, prev_fit+new_fit, params['N'])
        m = mean(evaluate(prev_pop, params['f']))
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)

        t += 1
    return prev_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1,
                        help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50,
                        help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3.,
                        help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=3.,
                        help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10,
                        help='number of mutants for parwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False,
                        help="Print the mean fitness evolution on a standard output ")
    parser.add_argument('-seed', type=int, default=None,
                        help="Seed for the initial population")
    return parser.parse_args()


def main():
    args = parseArguments()

    if args.length == 1 and args.xL == -2 and args.xU == 2:
        print('Function 1')
        def f(x): return x**4 + x**3 - x**2 - x
        f.__doc__ = 'Function 1 [ x**4 + x**3 - x**2 - x ]'
    elif args.length == 30 and args.xL == -100 and args.xU == 100:
        print('Function 2')
        def f(x): return sum(x**2)
        f.__doc__ = 'Function 2 [ sum(x**2) ]'
    elif args.length == 2 and args.xL == -30 and args.xU == 30:
        print('Function 3')
        def f(x): return sum(100*(x[1:]-x[:-1]**2)**2 + (x[:-1]-1)**2)
        f.__doc__ = 'Function 3 [ sum(100*(x[1:]-x[:-1]**2)**2 + (x[:-1]-1)**2) ]'
    else:
        print('NONE')

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
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function "+f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()


if __name__ == "__main__":
    main()
