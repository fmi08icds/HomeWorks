from numpy import random, array, mean, exp, zeros, column_stack, argsort, concatenate
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

def initialise(N, n, x_l, x_u):
    """
    generate initial population of individuals with N individuals with values (x_i,eta_i)

    Parameters:
    N (int): number of individuals of population
    n (int): dimension of solution space
    x_l (float): lower bound of solution space
    x_u (float): upper bound of solution space

    Returns: initial population as an array for the individuals
    """
    all_x = random.uniform(0,1,(N, n)) * (x_u - x_l) + x_l # values of x_i randomly generated in range [x_l, x_u]
    all_eta = random.uniform(0,1,(N, n)) * (x_u - x_l) + x_l # same range
    return array(list(zip(all_x, all_eta))) #returns list of tuples for initial population


def evaluate(pop, f):
    """
    - evaluates fitness for each individual in population
    - applies objective function to  xi values
    - fitness values stored in array

    Parameters:
    pop (np.array): Array with individuals with shape (N,2,n)
    f (function): objective function that should be minimized (defined in main)

    Returns: array with fitness values for each individual
    """

    fitnesses = array([f(ind[0]) for ind in pop])
    return fitnesses


def mutate(pop): # for mutation operation on the population
    """
    Applys mutation to population
    - generate one offspring (x′_i, η′_i) for each parent (xi, ηi) with mutation formulas from slides
    - mutation is applied to each component of xi and ηi using random values drawn from a normal distribution
    - calculation of mutation parameters tau, tau_prime based on the dimension of the solution space n
    - new population new_pop as array

    Parameters:
    pop (np.array): Array with shape (N,2,n)

    Return: array with new mutated population
    """

    n = len(pop[0][0])
    N = len(pop)
    new_pop = zeros(pop.shape)

    tau = ((2 * ((2 * n) ** 0.5)) ** 0.5) ** -1
    tau_prime = ((2 * n) ** 0.5) ** -1

    for i in range(N):
        parent = pop[i]

        ## COMMENTS: wrong here, random.normal() should be called for each n. please check the algo description here is N_j
        offspring_x = parent[0] + parent[1] * random.normal() # x + eta * random.normal()
        offspring_eta = parent[1] * exp(tau_prime * random.normal() + tau * random.normal())
        offspring = (offspring_x, offspring_eta)
        new_pop[i]= offspring

    return new_pop


def select(pop, fitnesses, N, q=10): # selection step
    """
    - pairwise comparisons between parent (xi, ηi) and offspring (x′i, η′i) to find winners based on fitness
    - For each individual i, q opponents are randomly chosen, and if the individual's fitness is smaller than the opponent's fitness, it receives a "win." -> smaller because we want to minimize
    - selection of N individuals from the combined population of parents and offspring who have the most wins
    - selected individuals form the next generation returned as array

    Parameters:
    pop (np.array): Array with shape (N,2,n), here two populations concatenated
    fitnesses (np.array): fitnessess of all individuums
    N (int): length of one of the poulations
    q (int): number of opponents (default = 10)

    Returns: array with selected individuums for next generation
    """

    best_wins = zeros(len(fitnesses))

    for i in range(N*2):
        opponents = random.choice(N*2, size=q, replace=False) ## COMMENTS: good

        wins = 0
        for opponent in opponents:
            if fitnesses[opponent] >= fitnesses[i]:
                wins += 1
        best_wins[i] = wins ## COMMENTS: Good

    selected_pop = pop[argsort(best_wins)][N:]


    return selected_pop


def dea(params): # differential evolutionary algorithm
    """
    - performs Differential Evolutionary Algorithm (DEA)

    Parameters:
    params (dict): dictionary containing the parameters for DEA

    Returns: tuple containing final population and mean fitness values
    """

    T = params["T"]
    prev_pop = params["init_pop"]
    t = 0
    mean_fit = [mean(evaluate(prev_pop, params['f']))]

    while t < T:
        #per iteration  mutation, evaluation of fitness, and selection

        mutated_pop = mutate(prev_pop) # mutate population
        both_pops = concatenate((prev_pop, mutated_pop), axis=0)

        fitnesses = evaluate(both_pops, params['f'])
        #selected_pop = select(both_pops, evaluate(both_pops, params['f']), len(prev_pop))
        selected_pop = select(both_pops, fitnesses, len(prev_pop))
        prev_pop = selected_pop # update population with the selected individuals

        m = mean(evaluate(prev_pop, params['f']))

        mean_fit += [m] # mean fitness of population

        print(f"Mean fitness {t} : ", m)

        t += 1

    return prev_pop, mean_fit


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1, help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generations of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3., help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=3., help='Upper bound of the solution space')
    parser.add_argument('-q', type=int, default=10, help='Number of mutants for pairwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on standard output")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")

    args = parser.parse_args()
    args.verbose = True  # Enable verbose mode

    return args #parser.parse_args()

def main():
    args = parseArguments()

    # f = lambda x: sum(x**2)  # Define your objective
    # f.__doc__ = "sum(x**2)"
    # python hw7_dea.py -n 30 -xL -100 -xU 100

    # f = lambda x: x**4 + x**3 - x**2 - x
    # f.__doc__ = "x**4 + x**3 - x**2 - x"
    #python hw7_dea.py -n 1 -xL -2 -xU 2

    f = lambda x: sum(100 * (x[j+1] - x[j]**2)**2 + (x[j] - 1)**2 for j in range(len(x)-1))
    f.__doc__ = "Rosenbrock Function"
    #python hw7_dea.py -n 2 -xL -30 -xU 30


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
    plt.title("Optimization of the function " +f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()

if __name__ =="__main__" :
    main()
