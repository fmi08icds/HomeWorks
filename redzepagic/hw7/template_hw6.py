from numpy import random, mean
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import math
import heapq
import numpy as np
from random import sample

def initialise(N,n,x_l, x_u) :
    """
        Her the initial population is created and returned
    """
    all_x = []
    all_eta = []

    for i in range(N):
        r_x = random.uniform(0, 1, n)
        r_eta = random.uniform(0, 1, n)

        x = r_x * (x_u - x_l) + x_l
        all_x.append(x)
        
        eta = r_eta * (x_u - x_l) + x_l
        all_eta.append(eta)

    return list(zip(all_x, all_eta))


def evaluate(pop, f) :
    """
        Here the fitness function, which should be minimized is applied to the population
        It returns the fitnesses of each agent
    """
    fitnesses = []

    for p in pop:
        fitnesses.append(f(p[0]))

    return fitnesses


def mutate(pop) :
    """
        Here the new population is calculated, by randomly creating variations in the old population
        It returns the new population
    """

    n = len(pop[0][0]) # get the dimension of the solution space here.
    N = len(pop) # the population size
    new_pop = []
    tau = 1/(math.sqrt(2 * math.sqrt(n)))
    tau_prime = 1/(math.sqrt(2*n)) 

    for i in range(N):
        x = pop[i][0]
        eta = pop[i][1]
        x_new = []
        eta_new = []
        gaus1 = random.normal()
        gaus2 = random.normal()
        gaus3 = random.normal()

        for j in range(n):
            x_new.append(x[j] + eta[j]*gaus1)
            eta_new.append(eta[j]*math.exp(tau_prime*gaus2 + tau*gaus3))
        
        new_pop.append((np.array(x_new), np.array(eta_new)))

    return new_pop


def select(pop, fitnesses, N, q=10) :
    """
        Here the fittest agents are selected by randomly comparing their fitness to other agents
        It returns the fittest agents

    """
    win_arr = []

    for i in range(len(fitnesses)):
        fit = fitnesses[i]
        opponents = sample(fitnesses, q)
        wins = 0
        for fit_op in opponents:
            if fit <= fit_op:
                wins += 1
        win_arr.append(wins)
    
    biggest_indexes = heapq.nlargest(N, range(len(win_arr)), key=lambda i: win_arr[i])

    selected_pop = []

    for i in biggest_indexes:
        selected_pop.append(pop[i])
               
    return selected_pop


def dea(params: dict):

    """
        This is the evolutionary algorithm; which follows all the steps and calls the other functions in the right order until a number of iterations is reached
        1. Initiate
        2. Mutate
        3. Evaluate
        4. Select

        It returns the fittest population in the last iteration and the mean fitness
    """
    T = params["T"] # get the coresponding parameter from the params dict.
    prev_pop = params["init_pop"]
    t = 0
    mean_fit = [mean(evaluate(prev_pop,params['f']))]

    while t < T:
        ## write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        pop_new = mutate(prev_pop)

        pop_all = prev_pop + pop_new
        fitnesses = evaluate(pop_all, params["f"])

        prev_pop = select(pop_all, fitnesses, params["N"])
        
        m = mean(evaluate(prev_pop, params["f"]))
        mean_fit += [m]
        print(f"Mean fitness {t} : " ,m)

        t +=1
    return prev_pop, mean_fit



def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length' ,type=int, default=1, help= "The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generation of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-2.,  help='Lower bound of the the solution space')
    parser.add_argument('-xU', type=float, default=2.,  help='Upper bound of the the solution space')
    parser.add_argument('-q', type=int, default=10,  help='number of mutants for parwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on a standard output " )
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def main() :
    args = parseArguments()
    f = lambda x: x**4 + x**3 - x**2 - x # Here you will define your obejective function
    f.__doc__ = "x**4 + x**3 - x**2 - x"
    #f = lambda x: sum(x**2)
    #f.__doc__ = "sum(x**2)"
    #f = lambda x: sum(100*((x[i+1] - x[i]**2)**2)+(x[i]-1)**2 for i in range(len(x)-1))
    #f.__doc__ = "sum(100*(x[i+1] - x[i]**2)+(x[i]-1)**2 for i in range(len(x)-1))"

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



if __name__ =="__main__" :
    main()
