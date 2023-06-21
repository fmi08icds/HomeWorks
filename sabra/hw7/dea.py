import numpy as np
from numpy import concatenate
from numpy import random, mean
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N,n,x_l, x_u) :
    """
    Initialize a population of individuals within a given solution space.

    Args:
        N (int): Population size.
        n (int): Dimension of the solution space.
        x_l (float): Lower bound of the solution space
        x_u (float): Upper bound of the solution space

    Returns:
        list: Initial Population of individuals


    """
    all_x = []
    all_eta = []

    for _ in range(N):
        x_i = np.array([random.uniform(0,1) * (x_u - x_l) + x_l for _ in range(n) ])
        eta_i = np.array([ random.uniform(0,1) * (x_u - x_l) + x_l for _ in range(n)])
        all_x.append(x_i)
        all_eta.append(eta_i)

    return list(zip(all_x, all_eta))


def evaluate(pop, f) :
    """
    Evaluate the fitness of each individual in the population.

    Args:
        pop (list): population of individuales
        f (function): Objective function to evaluate

        Returns:
            list: Fitness values for each individual in the population

    """
    fitness_values = []
    for individual in pop:
        xi = individual[0] # Extract the xi from the individual
        fitness = f(xi) # Compute the fitness using the objective function
        fitness_values.append(fitness)
    return fitness_values


def mutate(pop) :
    """
        Mutate the population by introducing random variations to the individuals.

        Args:
            pop (list): Population of individuals

        Returns:
            list: Mutated population

        - The mutate function applies random variations to each individual in the population.
        - The mutation process is performed in the solution space , where each individual
           consists of two components: xi and eta_i.
        - For each individual , the function generates mutated versions xi_prime
          and eta_prime_i by applying random variations using normal distribution samples.
        - The parameters tau and tau_prime control the magnitude of the variations
        - The mutated individaules are then added to the new population , which
          is returned as the result of the mutation process.

    """
    n = len(pop[0][0]) # get the dimension of the solution space here.
    N = len(pop) # the population size
    new_pop = []
    tau = ((2 * ((2 * n) ** 0.5)) ** 0.5) ** -1
    tau_prime = ((2 * n) ** 0.5) ** -1
    for i in range(N):
        xi, eta_i = pop[i]
        xi_prime = []
        eta_prime_i = []

        for j in range(n):
            xi_j = xi[j]
            eta_i_j = eta_i[j]
            xi_prime_j = xi_j + (eta_i_j * np.random.normal(0,1))
            eta_prime_i_j = eta_i_j * np.exp( tau_prime * np.random.normal(0,1) + tau * np.random.normal(0,1))
            xi_prime.append(xi_prime_j)
            eta_prime_i.append(eta_prime_i_j)

        new_pop.append((xi_prime,eta_prime_i))

    return new_pop



def select(pop, fitnesses, N, q=10) :
    """
        Select individuales from the population for reproduction based on
        pairwise comparisons.

        Args:
            pop (list): Population of individuals.
            fitnesses (list): Fitness values corresponding to each inidividal in the population
            N (int): desired number of individuales to select
            q (int):Number of opponents for pairwise comparison.

        Returns:
            list: Selected individuales for the next generation
    """
    selected_pop = []
    num_individuals = len(pop)

    # Perform pairwise comparisons for each individual
    for i in range(num_individuals):
        wins = 0 # counter for the number of wins

        # Randomly select opponents for comparison
        opponents = random.choice(num_individuals, size= q, replace= False)

        # compare the fitness of the individual with each opponent
        for opponent_idx in opponents:
            if fitnesses[i] < fitnesses[opponent_idx]:
                wins += 1

        selected_pop.append((pop[i], fitnesses[i], wins))


    # Sort the individuals based on the number of wins (in descending order)
    selected_pop.sort(key= lambda x: x[2], reverse=True)

    # Select the top N individuals with the most wins
    selected_pop = selected_pop[:N]

    # Extract the selected individuales from the tuples
    selected_pop = [individual[0] for individual in selected_pop]

    return selected_pop


def dea(params):

    """
    Differential Evolution Algorithum (DEA) implementation.

    Args:
        params (dict): Dictionary containing the DEA parameters.

    Returns:
        tuple: Final selected population and the list of mean fitness values.

    The dea function performs the Diiferential Evolution Algorithum (DEA) optimization.
    It takes a set of parameters ('params') specifiying the dimension of the solution space,

    The function initializes the time step ('t') and an empty list ('mean_fit') to store
    the mean fitness values at each generation. Then, it enters a loop that continues until
    't' reaches the specified number of generations ('T').

    Within each iteration , the function applies the DEA steps:
    1) Mutate the previous population ('prev_pop') using the 'mutate' function.
    2) Evaluate the fitness of the mutated population using the objective
       function ('f') and 'evaluate' function
    3) Select individuals from the mutated population based on pairwise comparisons
       using the 'select' function.
    4) Compute and store the mean fitness of the selected population
    5) Increment the time step 't'

    After the loop ends, the function returns the final selected population ('prev_pop')
    and the list of mean fitness values ('mean_fit')

    """

    T = params["T"] # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [mean(evaluate(prev_pop,params['f']))]
    while t< T:
       mutated_pop = mutate(prev_pop)
       parent_offspring_populations = concatenate((prev_pop, mutated_pop), axis=0)
       fitness_values = evaluate(parent_offspring_populations, params['f'])
       selected_pop = select(parent_offspring_populations, fitness_values, len(prev_pop), params['q'])
       prev_pop = selected_pop
       m = mean(evaluate(prev_pop, params['f']))

       mean_fit += [m] # mean fitness of population

       print(f"Mean fitness {t} : ", m)

       t += 1


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


def main() :
    args = parseArguments()
    f = lambda x: np.sum(np.array(x)**2) # Here you will define your obejective function
    f1 = lambda x: np.array(x)**4 + np.array(x)**3 - np.array(x)**2 - np.array(x)
    f2 = lambda x: sum(x**2)
    f3 = lambda x: sum([100 * (x[(j+1)] - x[j]**2)**2 + (x[j] - 1)**2 for j in range(len(x)-1)])

    chosen_function = 'f1'

    if chosen_function == 'f1':
        args.xL = -2
        args.xU = 2
        args.length = 1
        f = f1

    elif chosen_function == 'f2':
        args.xL = -100
        args.xU = 100
        args.length = 30
        f = f2

    elif chosen_function == 'f3':
        args.xL = -30
        args.xU = 30
        args.length = 2
        f= f3



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
    #plt.title("Optimization of the function "+f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()



if __name__ =="__main__" :
    main()
