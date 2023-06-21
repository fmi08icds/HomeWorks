from numpy import random, mean
import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from dataclasses import dataclass
from itertools import compress
import logging

logging.basicConfig(level=logging.INFO)


@dataclass
class Population:
    xl: int  # lower bound of the solution space
    xu: int  # upper bound of the solution space
    N: int  # population size
    n: int  # dim of the solution space
    agents: list  # list of parent-agents
    offsprings: list  # list of agent-offsprings
    generation: int = 0  # generation number


@dataclass
class Agent:
    x: float  # x values of the solution
    eta: float  # mutation rate
    fitness: float  # y value of the objective function


def initialise(N, n, x_l, x_u):
    """
    Initializes a population of N individuals, each with n dimensions, where each dimension is a random value between x_l and x_u.

    Args:
    - N: int, the population size
    - n: int, the dimension of the solution space
    - x_l: float, the lower bound of the solution space
    - x_u: float, the upper bound of the solution space

    Returns:
    - A list of tuples, where each tuple represents an individual in the population. The first element of the tuple is a list of n random values between x_l and x_u, and the second element is None.
    """
    assert (N >= 4)
    "N must be greater than or equal to 4"

    all_x: list = [
        [np.random.uniform(0, 1)*(x_u-x_l)+x_l for i in range(n)] for j in range(N)]
    all_eta = [np.random.uniform(0, 1)*(x_u-x_l)+x_l for i in range(N)]

    return Population(xl=x_l,
                      xu=x_u,
                      N=N,
                      n=n,
                      agents=[Agent(x=all_x[i], eta=all_eta[i], fitness=None)
                              for i in range(N)],
                      offsprings=[],
                      generation=0)


def evaluate(pop: Population, f):
    """
    Evaluates the fitness of each agent in the population using the given objective function.

    Args:
    - pop: Population, the population to evaluate
    - f: function, the objective function to evaluate the fitness of each agent

    Returns:
    - None
    """
    
    logging = None
    try:
        for agent in pop.agents+pop.offsprings:
            logging = agent.x
            agent.fitness = f.__call__(agent.x)
    except Exception as e:
        print(
            f'could not evaluate the fitness of the population for {logging} and function {f.__doc__}')
    return [agent.fitness for agent in pop.agents]


def mutate(pop: Population) -> None:
    """
    2003_Book_AdvancesInEvolutionaryComputin p.48-49 for implementation details
    """

    # increment the generation number / times the population has been mutated
    pop.generation += 1

    # strategy parameter constants for each agent
    tau = np.sqrt(2*np.sqrt(pop.n))**-1
    tau_prime = np.sqrt(2*pop.n)**-1

    for agent in pop.agents:
        # the update step is described in 2003_Book_AdvancesInEvolutionaryComputin @ page 48
        pop.offsprings.append(Agent(agent.x + agent.eta*np.random.normal(0, 1, pop.n),
                                    agent.eta *
                                    np.exp(tau_prime*np.random.normal(0, 1,
                                           1) + tau*np.random.normal(0, 1, pop.n)),
                                    fitness=None))

    pass


def select(pop: Population, q=10):
    """
     Conduct pairwise comparison over the union of parents and offspring.
     For each individual, q opponents are chosen at random from all the parents and offspring.
     For each comparison, if the individual's fitness is not smaller than the opponent's, it receives a "win."
     The individual with the most wins is selected for the next generation.
    """

    all_agents = pop.agents + pop.offsprings
    wins = [0]*len(all_agents)
    for pos, agent in enumerate(all_agents):
        
        # choose all but the current agent as opponents
        pos_mask = [True]*len(all_agents)
        pos_mask[pos] = False
        opponents = random.choice(list(compress(all_agents,pos_mask)), q)
        
        ## crucial step!!! => or <= depends on the objective function
        ## and if one wants to minimize or maximize it.
        ## now this is a minimization problem, so we want to select the
        ## agents with the lowest fitness
        wins[pos] = np.sum([agent.fitness <= opponent.fitness for opponent in opponents])

    # select the best N agents from the union of the parents and offsprings
    # argsort returns the indices that would sort an array
    # [::-1] reverses the array, so the highest win-count is first
    # [:pop.N] selects the first N agents, so the best N agents are selected
    pop.agents = [all_agents[i] for i in np.argsort(wins)[::-1][:pop.N]]
    
    # finally, reset offsprings to empty list
    pop.offsprings = [] 
    pass



def dea(params):

    """
    Evolutionary Algorithm implementation.

    Parameters:
    -----------
    params : dict
        A dictionary containing the following parameters:
        - T : int
            Number of generations of the EA.
        - N : int
            Population size.
        - n : int
            Dimension of the solution space.
        - xL : float
            Lower bound of the solution space.
        - xU : float
            Upper bound of the solution space.
        - q : int
            Number of mutants for pairwise comparison.
        - verbose : bool
            Whether to print the mean fitness evolution on a standard output.
        - seed : int
            Seed for the initial population.
        - f : function
            Polynom to evaluate. Should be vectorized since input x is a vector.

    Returns:
    --------
    init_pop : Population
        The final population after T generations.
    mean_fit : list of float
        The mean fitness of the population at each generation.
    best_agent : float
        The best agent found by the EA after T steps.
    best_walk : list of float
        The fitness of the best agent at each generation.
    """

    # initialise the population
    init_pop = initialise(params['N'], params['n'], params['xL'], params['xU'])
    
    # start the process
    T = params['T']  
    t = 0
    mean_fit = []
    best_walk = []
    while t < T:

        # 1. mutate
        mutate(init_pop)
        # 2. evaluate
        m = mean(evaluate(init_pop, params['f']))
        # 3. select
        select(init_pop, params['q'])
        t += 1
        
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)
        
        # for plotting purposes
        best_walk.append(min(init_pop.agents, key=lambda agent: agent.fitness).fitness)

        if params['verbose']:
            print(f"Generation {init_pop.generation}: mean fitness = {mean_fit[-1]}, best fitness = {best_walk[-1]}")
    
    # since they are ordered by fitness, the best solution is the first one
    best_agent = min(init_pop.agents, key=lambda agent: agent.fitness)

    return init_pop, mean_fit, best_agent, best_walk


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
    parser.add_argument('-f', default=None,
                        help="polynom to evaluate")
    return parser.parse_args()

@np.vectorize
def target_function1(x):
    """ 
    function 1
    """
    ## theoretical global minimum is 0.6404
    return (x**4 + x**3 - x**2 - x)


# autmatically vectorized because of np.sum...
def target_function2(x):
    """ 
    function 2
    """
    # theoretical minimum is n*x_l = 30*-100 = -3000
    return np.abs(np.sum(x))

def target_function3(x):
    """ 
    function 3
    """
    # theoretical minimum is 0
    y = 0
    for i in (range(len(x)-1)):
        y += 100*((x[i+1]-x[i]**2)**2) + (x[i]-1)**2
    return y

def test_dea_with_target_function1():
    params = {
        'n': 1,
        'T': 250,
        'q': 25,
        'N': 200,
        'f': target_function1,
        'verbose': True,
        'xU': 3.,
        'xL': -3.
    }
    return dea(params)


def test_dea_with_target_function2():
    params = {
        'n': 30,
        'T': 750,
        'q': 10,
        'N': 150,
        'f': target_function2,
        'verbose': True,
        'xU': 50.,
        'xL': -50.
    }
    return dea(params)

def test_dea_with_target_function3():
    params = {
        'n': 30,
        'T': 1000,
        'q': 25,
        'N': 150,
        'f': target_function3,
        'verbose': True,
        'xU': 1.5,
        'xL': -1.5
    }
    return dea(params)



def main():
    best_pop, mean_fitnesses1, best_agent1, best_walk1 = test_dea_with_target_function1()
    best_pop, mean_fitnesses2, best_agent2, best_walk2 = test_dea_with_target_function2()

    best_pop, mean_fitnesses3, best_agent3, best_walk3 = test_dea_with_target_function3()

    args = parseArguments()
    
    print(f'f1 Solution: {best_agent1.x} with fitness {best_agent1.fitness}')
    print(f'f2 Solution: {best_agent2.x} with fitness {best_agent2.fitness}')
    print(f'f3 Solution: {best_agent3.x} with fitness {best_agent3.fitness}')


    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    axs[0].plot(mean_fitnesses1, label="mean fitness", color ='black')
    axs[0].plot(best_walk1, label="best agent", color="red")
    axs[0].set_title(f"Optimization of {target_function1.__doc__}")
    axs[0].set_xlabel("Generation(t)")
    axs[0].set_ylabel("fitness")
    axs[0].legend()

    axs[1].plot(mean_fitnesses2, label="mean fitness", color ='black')
    axs[1].plot(best_walk2, label="best agent", color="red")
    axs[1].set_title(f"Optimization of {target_function2.__doc__}")
    axs[1].set_xlabel("Generation(t)")
    axs[1].set_ylabel("fitness")
    axs[1].legend()

    axs[2].plot(mean_fitnesses3, label="mean fitness", color ='black')
    axs[2].plot(best_walk3, label="best agent", color="red")
    axs[2].set_title(f"Optimization of {target_function3.__doc__}")
    axs[2].set_xlabel("Generation(t)")
    axs[2].set_ylabel("fitness")
    axs[2].legend()

    plt.tight_layout()
    plt.show()
    plt.savefig("./results.png")


if __name__ == "__main__":
    main()
