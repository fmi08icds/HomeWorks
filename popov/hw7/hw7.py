from numpy import random, mean
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

f1 = lambda x : x**4 + x**3 - x**2 -x
f2 = lambda arr : sum([x**2 for x in arr])

def initialise(N,n,x_l, x_u) :
    """
    This function initialises the population for our algorithm 
    
        N (int): Number of individuals
        n (int): Dimension of solution space 
        x_l (float or array of floats): Lower interval bound
        x_u (float or array of floats): Upper interval bound 
        
        Returns: 
            all_x (array): initialised population
            all_eta (array): respective strategy parameters to population
    """
    if n == 1: 
        x_l = [x_l]
        x_u = [x_u]
    # assert n == len(x_l) == len(x_u), f"expected dimension of interval bounds to match dimension given for solution space, got: n = {n}, len(x_l) = {len(x_l)}"
    
    # Convert interval bounds to numpy array for easier computation
    x_l = np.array(x_l)
    x_u = np.array(x_u)
    
    # Create a random number generator object for the uniform distribution and populate array with r_i's and r'_i's 
    rng1 = random.default_rng()
    r = rng1.uniform(0,1,N)
    r_prime = rng1.uniform(0,1,N)
    
    # Initialise x and eta arrays 
    all_x = np.zeros(N)
    all_eta = np.zeros(N)    
    
    # Calculate x_i's and eta_i's by stretching the r, and r_prime arrays to broadcast computation 
    R = r[:, np.newaxis]
    R_prime = r_prime[:, np.newaxis]
    all_x = R * (x_u - x_l) + x_l
    all_eta = R_prime * (x_u - x_l) + x_l
    
    
    # all_x_eta = list(zip(all_x, all_eta))
    

    return all_x, all_eta

def evaluate(pop, f) :
    """
    This function will evaluate a population given a specific function f
    
        pop (array): array of individuals in a population 
        
        Returns: 
            eval_pop (array): evaluated array of population 
    """
    # Initialise array to hold evaluations 
    N, n = np.shape(pop)
    eval_pop = np.zeros(N*n).reshape(N,n)  
    
    # Apply function f to each individual in the population 
    eval_pop = np.apply_along_axis(func1d = f, axis = 1, arr = pop)
    
    return eval_pop

def mutate(pop, strat) :
    """
    Mutate a given population according to algorithm 
        pop (array): array of individuals in a population
        strat (array): array of respective strategy parameters
        
        Returns:
            new_pop (array): mutated population
            new_strat (array): mutated strategy parameters
    """
    # Get dimensions
    N,n = np.shape(pop)
    
    # Define tau values 
    tau = np.sqrt(2*np.sqrt(n))
    tau = 1 / tau 
    tau_prime = np.sqrt(2*n)
    tau_prime = 1 / tau_prime

    # Initialise new empty population for mutations 
    new_pop = np.zeros(N*n).reshape(N,n)
    new_strat = np.zeros(N*n).reshape(N,n)
    
    # Create a random number generator object for the normal distribution vector Normal and single value normal_i 
    rng2 = random.default_rng()
    normal_x_matrix = rng2.normal(0, 1, N*n).reshape(N,n)
    
    normal_eta_vec = rng2.normal(0,1,N)
    normal_eta_vec = normal_eta_vec[:, np.newaxis]
    normal_eta_vec = np.broadcast_to(normal_eta_vec,(N,n))
    normal = rng2.normal(0,1,N)
    normal = normal[:, np.newaxis]
    normal_eta_matrix = np.broadcast_to(normal, (N,n))
    
    
    
    # Mutate according to algorithm (using element-wise multiplication operation)
    all_x_prime = pop + strat * normal_x_matrix
    
    exp_term = (tau_prime * normal_eta_vec) + (tau * normal_eta_matrix)
    all_eta_prime = strat * np.exp(exp_term)
    
    # Rename for readability
    new_pop = all_x_prime
    new_strat = all_eta_prime


    return new_pop, new_strat

def select(pop, new_pop, strat, new_strat, N, f, q=10) :
    """
        Your docstr here
    """
    # Get dimensions
    N,n = np.shape(pop)
    
    # steps 
    # 1. concatenate arrays and add new axis 
    all_pop = np.concatenate((pop,new_pop), axis = 0)
    #all_pop = all_pop[:, np.newaxis]
    
    all_strat = np.concatenate((strat,new_strat), axis = 0)
    #all_strat = all_strat[:, np.newaxis]

    
    # 2. create rng object to select q opponents at random from concatenated array 
    rng3 = random.default_rng()

    # 3. compare each individual using boolean comparison and evaluate function 
    # 4. and count the number of true values 
    count_wins = np.zeros(2*N)
    for i in range(2*N):
        opponents = rng3.choice(all_pop, size=q, replace = False)
        
        current_individual = all_pop[i,np.newaxis]
        boolarr = evaluate(current_individual,f) <= evaluate(opponents,f)
        individual_wins = np.count_nonzero(boolarr)
        count_wins[i] = individual_wins

    
    # 7. stack columns, sort and concatenate
    wins_pop = count_wins.reshape((2*N,1))
    wins_strat = count_wins.reshape((2*N,1))
    # wins_pop = wins_pop[:,np.newaxis]
    to_sort_pop = np.concatenate((all_pop,wins_pop), axis = 1)
    to_sort_strat = np.concatenate((all_strat,wins_strat), axis = 1)
    

    sorted_pop = to_sort_pop[to_sort_pop[:,n].argsort()][::-1]
    sorted_strat = to_sort_strat[to_sort_strat[:,n].argsort()][::-1]
    
    # 9. return selected_pop and selected_strat
    selected_pop = sorted_pop[:N,:2]
    selected_strat = sorted_strat[:N,:2]
    # end. 

    return selected_pop, selected_strat


def dea(params):

    """
        Your docstr here
    """

    T = params["T"] # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]
    prev_strat = params["init_strat"]

    t = 0
    mean_fit = [mean(evaluate(prev_pop,params['f']))]
    while t< T:
        ## write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        new_pop, new_strat = mutate(prev_pop, prev_strat)
        
        # select function already contains evaluation step
        selected_pop, selected_strat = select(prev_pop, new_pop, prev_strat, new_strat, params["N"], params["f"], params["q"])
        prev_pop = selected_pop
        prev_strat = selected_strat
        m = mean(evaluate(prev_pop,params['f']))
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
    f0 = lambda x: sum(x**2) 
    f1 = lambda x : x**4 + x**3 - x**2 -x # Here you will define your obejective function
    f = lambda arr : sum([x**2 for x in arr])

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

    init_pop, init_strat = initialise(args.N, args.length, args.xL, args.xU)
    params['init_pop'] = init_pop
    params['init_strat'] = init_strat

    best_pop, mean_fitnesses = dea(params)
    print("Best population : ", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function "+f.__doc__)
    plt.xlabel("Generation(t)")
    plt.ylabel("Population mean fitness")
    plt.show()



if __name__ =="__main__" :
    main()
