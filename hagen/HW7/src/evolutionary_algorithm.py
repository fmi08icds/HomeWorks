import numpy as np #imported whole package so I can use arrays and other methods
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


def initialise(N,n,x_l, x_u) :
    """
        Creates initial population of N individuals. Each individual X_i is a tuple of x_i and eta_i.
        x_i are the start inputs in the optimization function.
        eta_i are normally-distributed random values, which correspond to step size
        Both, x_i and eta_i, are generated using a random value from a uniform distribution (0,1).

        Parameters:
        N (int): size of population
        n (int): dimension of solution space (NxN)
        x_l (float): lower bound of solution space
        x_u (float): upper bound of solution space

        Returns:
        (np.array): population as 3D-Array (float), where 1. dimension is the individual, the 2. dimension is x or eta 
        and the 3. dimension is the solution space

    """
    all_x = np.random.uniform(0,1, (N,n)) * (x_u-x_l) + x_l
    all_eta = np.random.uniform(0,1, (N,n)) * (x_u-x_l) + x_l

    return np.array(list(zip(all_x, all_eta)))


def evaluate(pop, f) :
    """
        Returns fitnesses for all individuals in the population.
        When using gradient descent, fitness equals to f(x) and should be minimized.
        
        Parameters: 
        pop (np.array): 3D-Array (float)
        f (function): Defined in main

        Returns:
        (np.array): 1D-Array of f(x) for all solutions for a specific x in pop
    """

    # x-value is at first position in tuple
    return np.array([f(individual[0]) for individual in pop])


def mutate(pop) :
    """
        Creates new population by generating a child for each individual in the old population pop.
        Each child is a mutation of its parent, where the mutation is created using random values  from a normal distribution.
        tau and tau_prime are additional parameters for the mutation and are based on the soluation space dimension.

        Parameters:
        pop (np.array): 3D-Array (float)

        Returns:
        new_pop (np.array): 3D-Array (float)
    """

    n = len(pop[0][0]) # get the dimension of the solution space here.
    N = len(pop) # the population size
    
    # initialise population in correct space with zeros:
    new_pop = np.zeros(N*2*n).reshape(pop.shape)
    
    tau = np.sqrt( 2 * np.sqrt(n) ) ** (-1) #
    tau_prime = np.sqrt(2*n) ** (-1) #

    for i in range(N) :
        # own implementation of the mutation operator:
        parent = pop[i]

        new_x = parent[0] + parent[1] * np.random.normal(0,1)
        new_eta = parent[1] * np.exp( tau_prime * np.random.normal(0,1) + tau * np.random.normal(0,1) )
        child = (new_x, new_eta)
        
        new_pop[i] = child

    return new_pop


def select(pop, fitnesses, N, q=10) :
    """
        Performs fights between x_i, which can be of the parent or child population.
        q opponents are randomly chosen for each individual to fight with. A win equals to a lower function value, so the fitness value should be lower.
        In the end, the best N individuals are chosen as the new population and returned.

        Parameters:
        pop (np.array): 3D-Array (float)
        fitnesses (np.array): 1D-Array of f(x) for all solutions for a specific x in pop
        N (int): size of population
        q (int): number of opponents chosen for fight

        Returns:
        selected_pop (np.array): 3D-Array (float)
    """

    # initialise result array, index = individual
    total_wins = np.zeros(len(fitnesses))
    
    for i in range(2*N): #(later called with two populations)
        # choose q random opponents (indexes in pop)
        opponents = np.random.randint(2*N, size = q)
        wins = 0


        for opponent in opponents:
            if fitnesses[i] < fitnesses[opponent]:
                wins += 1
            elif fitnesses[i] == fitnesses[opponent]:  # if tie, choose random winner
                if np.random.choice(a=[False, True]):
                    wins += 1
        total_wins[i] = wins
    
    # argsort returns the (original) indices of the sorted array
    ascending = np.argsort(total_wins)
    
    # turn order around, so best individuals (most wins) come first
    descending = ascending[::-1]

    # Choose only the first N individuals
    selected_pop = pop[descending][:N]
    return selected_pop


def dea(params):

    """
        Main evolutionary algorithm, where all stages come together: 1. Mutate, 2. Evaluate, 3. Select 4. Update
        (Initialisation is below, in the main function).

        Paramaters:
        params (str): parsed input arguments
        
        Returns:
        prev_pop (np.array): 3D-Array (float) for the last population
        mean_fit (float): mean fitness
    """

    T = params['T'] # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = 0
    mean_fit = [np.mean(evaluate(prev_pop,params['f']))]
    while t < T:
        # 1. mutate
        mutated_pop = mutate(prev_pop)
        both_pops = np.concatenate((prev_pop, mutated_pop), axis=0)

        # 2. evaluate
        fitnesses = evaluate(both_pops, params['f'])

        # 3. select
        selected_pop = select(both_pops, fitnesses, len(prev_pop))

        # 4. update population with selected
        prev_pop = selected_pop
        
        # 5. Calculate mean fitness
        m = np.mean(evaluate(prev_pop, params['f']))
        mean_fit += [m]
        print(f"Mean fitness {t} : " ,m)

        t +=1
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

    # First function 
    # Terminal: python evolutionary_algorithm.py -n 1 -xL -2 -xU 2
    #f = lambda x: x**4 + x**3 - x**2 - x
    #f.__doc__ = "x**4 + x**3 - x**2 - x"
    
    # Second function
    # Terminal: python evolutionary_algorithm.py -n 30 -xL -100 -xU 100
    #f = lambda x: sum(x**2)  # Define your objective
    #f.__doc__ = "sum(x**2)"

    # Third function
    # Terminal: python evolutionary_algorithm.py -n 2 -xL -30 -xU 30
    f = lambda x: sum(100 * (x[j+1] - x[j]**2)**2 + (x[j] - 1)**2 for j in range(len(x)-1))
    f.__doc__ = "Rosenbrock Function"

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
    plt.title("Optimization of the function "+f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()



if __name__ =="__main__" :
    main()
