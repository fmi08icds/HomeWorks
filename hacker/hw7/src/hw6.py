import numpy as np
from math import sqrt, exp
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N, n, x_l, x_u):
    """
        Init population of size N with n dimensions.
        Each value x of n is between X_l and x_u
        calculate the standard deviation of all x of the pop 
    """
    all_x = np.random.uniform(low=x_l, high=x_u, size=(N, n))
    eta = np.std(all_x, axis=0)
    all_eta = [eta] * N

    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
        evaluate the fitness of the population pop with the function f
        as all functions in question have the minimum at 0 the fitness is the
        absolute value of f(x)
    """
    fitnesses = []
    for x, _ in pop:
        fitness = abs(f(x))
        fitnesses.append(fitness)
    return fitnesses


def mutate(pop):
    """
        Mutate each individual of the population as detailed in slide 14 of presentation.
    """
    n = len(pop[0][0])  # get the dimension of the solution space here.
    N = len(pop)  # the population size
    new_pop = []
    tau = (sqrt(2*sqrt(n)))**-1
    tau_prime = (sqrt(2*n))**-1

    for i in range(N):
        individual = pop[i][0]
        eta = pop[i][1]
        m_individual = individual + eta * np.random.random()
        m_eta = eta * exp(tau_prime*np.random.random() + tau*np.random.random())
        new_pop.append((m_individual, m_eta))

    return new_pop


def select(pop, fitnesses, N, q=10):
    """
        select the N fittest individuals of the population by comparing it to
        q random individuals in the same population.
    """
    selected_pop = []
    wins = [0] * len(pop)
    for i in range(0, len(pop)):
        q_indices = np.random.choice(len(fitnesses), size=q, replace=False)
        for qi in q_indices:
            if fitnesses[i] < fitnesses[qi]:
                wins[i] += 1

    top_indices = sorted(range(len(wins)), key=lambda i: wins[i], reverse=True)[:N]
    selected_pop = [pop[i] for i in top_indices]

    return selected_pop


def dea(params):
    """
        perform differential evolutionary algorithm (dea) to find the minimum of the given function.
    """

    T = params['T']  # get the corresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [np.mean(evaluate(prev_pop, params['f']))]
    while t < T:
        # write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        # 1. mutate
        new_pop = mutate(prev_pop)
        # 2. union + eval
        union_pop = np.append(new_pop, prev_pop, axis=0)
        eval_fit = evaluate(union_pop, params['f'])
        # 3. select
        new_pop = select(union_pop, eval_fit, params['N'])
        m = np.mean(evaluate(new_pop, params['f']))
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)
        # children pop becomes parent pop
        prev_pop = new_pop
        t += 1
    return new_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1,
                        help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50,
                        help='Number of generation of the DEA')
    parser.add_argument('-f', '--function', type=int, default=1,
                        help="Number of the function to be optimized (1-3)")
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

def func_1(x):
    return x**4 + x**3 - x**2 - x

def func_2(x):
    return sum(x**2)

def func_3(x):
    return sum(100*(x[1:]-x[:-1]**2)**2 + (x[:-1]-1)**2)

def main():
    args = parseArguments()

    if args.function == 1:
        print('Function 1')
        f = func_1
        f.__doc__ = 'Function 1 [ x**4 + x**3 - x**2 - x ]'
    elif args.function == 2:
        print('Function 2')
        f = func_2
        f.__doc__ = 'Function 2 [ sum(x**2) ]'
    elif args.function == 3:
        print('Function 3')
        f = func_3
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