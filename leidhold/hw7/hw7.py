from numpy import random, mean
from itertools import chain
import random
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
import inspect

def initialise(N, n, x_l, x_u):
    """
    This function initializes the population for the DEA algorithm.

    Args:
        N: The number of individuals in the population
        n: The number of dimensions for each individual
        x_l: The lower bound of the individual's values
        x_u: The upper bound of the individual's values

    Returns:
        A list of tuples representing the initial population, where each tuple contains an individual's x and eta values.

    """
    all_x = np.random.rand(N, n) * (x_u - x_l) + x_l
    all_eta = np.random.rand(N, n) * (x_u - x_l) + x_l

    pop = list(zip(all_x, all_eta))

    return pop

def evaluate(pop, f):
    """
    This function is applying a function on the objective x value for
    evaluating the individual's fitness in the population. This is implementing the natural selection.

    Args:
        pop: The population list with individual tupels
        f: The fitness function

    Returns:
        A list with fitness values

    """

    fitnesses = [f(x[0])[0] for x in pop]

    return fitnesses

def mutate(pop):
    """
    Mutate is performing a mutation on the individuals of the population.
    The mutated x and eta values are calculated through random changes according tau and tau_prime
    and the previous values for x and eta.

    Args:
        pop: The population of individuals

    Returns:
        new_pop: A new population list with mutated values.

    """

    n = len(pop[0][0])
    N = len(pop)
    new_pop = []
    tau = (np.sqrt(2 * np.sqrt(n)) **(-1))
    tau_prime = (np.sqrt(2 * n)** (-1))


    for i in range(N):
        x, eta= pop[i]
        mutated_x = x + eta * np.random.standard_normal() # COMMENTS: N_J also vary with j so standard_normal should be called n-times
        mutated_eta = eta * np.exp(tau_prime * np.random.standard_normal() + tau * np.random.standard_normal(n))
        new_pop.append((mutated_x, mutated_eta))

    return new_pop


def select(pop, N, q=10):
    """
    The selection function is iterating over the population out of previous and offspring individuals.
    For each individual a random sample of aspirants is calculated. The best individuals based on the
    number of wins against the chosen aspirants are selected.

    Args:
        pop: The union population as list including previous and offspring population and fitness
        N: The number of individuals in the population
        q: The number of aspirants to randomly choose for each individual


    Returns:
        A list of the selected individuals from the population

    """
    selected_pop=[]

    bestfits = {}
    for i in range(len(pop)):
        elem = pop[i]
        aspirants = random.sample(pop, q)
        best = sum([elem[1] < aspirant[1] for aspirant in aspirants]) # COMMENTS: GOOD
        bestfits[i] = best

    bestfits_order = sorted(bestfits.items(), key=lambda x: x[1], reverse=True)[:N]

    for bestof, _ in bestfits_order:
        selected_pop.append(pop[bestof][0])

    return selected_pop


def dea(params):
    """
    The Differential Evolutionary Algorithm function implements these 5 steps:
        1. Generate the initial population of N individuals or agents Pt
        2. Evaluate the Fitness of each individual
        3. Mutate the population Pt to generate a new population P0t
        4. Select N individual from Pt ∪ P0t proportianally to their fitnesses.
            The selected individuals will reproduce to the next generation and form a new population Pt+1.
        5. Stop if the halting criterion is satisfied; otherwise, t = t + 1 and go to step 2.

    Args:
        params: A dictionary containing the DEA parameters like Generation Steps 'T'  or initial values 'init_pop'

    Returns:
        A list containing individuals as the best population and a list of the mean fitness values over the Generation Steps T

    """

    T = params['T']
    prev_pop = params['init_pop']

    t = 0
    prev_fit = evaluate(prev_pop, params['f'])
    mean_fit = [mean(prev_fit)]

    while t < T:
        offspring_pop = mutate(prev_pop)
        offspring_fit = evaluate(offspring_pop, params['f'])
        prev_pop_fit = zip(prev_pop, prev_fit)
        offspring_pop_fit = zip(offspring_pop, offspring_fit)
        union_prev_offspring = list( chain(prev_pop_fit, offspring_pop_fit))
        prev_pop = select(union_prev_offspring, params['N'], params['q'])
        prev_fit = evaluate(prev_pop, params['f'])

        m = mean(prev_fit)
        mean_fit += [m]
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


def main():

    #f = lambda x: x**4 + x**3 - x**2 - x
    #f = lambda x: sum([x**2 for _ in range(30)])
    f = lambda x: sum([ 100 * (x - x**2)**2 + (x-1)**2 for _ in range(2)])

    params = {
        'init_pop': initialise(100, 2, -3.0, 3.0), # Becareful here instead of -3 and 3 it should be args.xL and args.xU
        'T': 50,
        'N': 100,
        'q': 10,
        'f': f
    }

    best_pop, mean_fitnesses = dea(params)
    print("Best population:", best_pop)
    plt.plot(mean_fitnesses, "o-")
    plt.title("Optimization of the function")
    plt.xlabel("Generation (t)")
    plt.ylabel("Population mean fitness")
    plt.show()

if __name__ == "__main__":
    main()
