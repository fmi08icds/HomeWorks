from numpy import random, mean
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import math


def initialise(N, n, x_l, x_u):
    """
    inititalises the population with a uniformed

    Args:
        N [int]: population size
        n [int]: the dimension of the solution space
        x_l [float]: the lower bound of the solution space
        x_u [float]: the upper bound of the solution space

    Returns:
        vector [np.ndarray] pair of real valued vectors (x, eta)
    
    """
    all_x = [0] * N
    for i in range(N):
        all_x[i] = random.uniform(low=0.0, high=1.0, size=n) * (x_u - x_l) + x_l
   
    uniform_eta = random.uniform(low=0.0, high=1.0, size=N)
    all_eta = uniform_eta*((x_u - x_l) + x_l)

    return list(zip(all_x, all_eta))


def evaluate(pop, f):
    """
    evaluates the current population with a objective function f

    Args:
        pop [List] the population list (x, eta)
        f [callable function] the function used for evaluation
    
    Returns:
        result [List] the result of f(pop)
    """
    return [f(x[0]) for x in pop]


def mutate(pop):
    """
    mutate the current population from x, eta to x_prime, eta_prime
    Args:
        pop: [List[Tuple(x, eta)]] individuals x and step-sizes eta
    
    Returns:
        result [List[Tuple[(x', eta')]]] mutated x' and adapted eta'
    """

    n = len(pop[0][0])  # get the dimension of the solution space here.
    N = len(pop)  # the population size

    mutated_pop = []
    for j in range(N):
        mutated_pop.append(pop[j][0] + pop[j][1] * random.normal(size=n))

    tau = (math.sqrt(2*math.sqrt(n)))**-1
    tau_prime = (math.sqrt(2*n))**-1
    vals = tau*random.normal(size=N) + tau_prime*random.normal(size=N)
    eta_prime = []
    for j in range(N):
        eta_prime.append(pop[j][1] * math.exp(vals[j]))

    return list(zip(mutated_pop, eta_prime))


def select(pop, fitnesses, N, q=10) :
    """
    count wins of an individual i for q opponents by min of their fitness
    select the top N wins based on their indices 

    Args:
        pop [List]: the population
        fitnesses [List]: the fitnesses of the population
        N [int]: the target population size
        q [int]: the samples to randomly draw

    Returns:
        selected_pop [List]: the newly selected population 
    """
    selected_pop = []
    population_size = len(pop)
    wins = [[i, 0] for i in range(population_size)]  # List of victories with indices
    for i in range(population_size):
        opponents = random.randint(0, population_size, size=q)
        for o in opponents:
            if fitnesses[i] < fitnesses[o]:
                wins[i][1] += 1



    wins = sorted(wins, key=lambda x: x[1], reverse=True)  # sort by victories
    for i in range(N):
        victor_index = wins[i][0]
        selected_pop.append(pop[victor_index])

    return selected_pop


def dea(params):
    """
    Calculates the differential evolutionary algorithm based on the 
    input parameters

    Args:
        params: the parameter to calculate DEA for

    Returns:
        None
    """

    T = params["T"] # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]

    t = 0
    fitness = evaluate(prev_pop,params['f'])
    mean_fit = [mean(fitness)]
    while t< T:
        # write your code here to implement the DEA. The steps should be
        mutated_pop = mutate(prev_pop)
        mutated_fitness = evaluate(mutated_pop, params['f'])
        m = mean(mutated_fitness)
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)
        t += 1
        # 3. select
        pop = prev_pop + mutated_pop
        pop_fittness = fitness + mutated_fitness
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
    f = lambda x: sum(x**2) # Here you will define your obejective function
    function_string = f"""sum(x**2)"""

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
    plt.title("Optimization of the function "+ function_string)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()



if __name__ =="__main__" :
    main()
