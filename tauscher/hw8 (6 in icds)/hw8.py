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
        DE generates new parameter
        vectors by adding the weighted difference between two population vectors to a
        third vector. Let this operation be called mutation. 
        If the
        trial vector yields a lower cost function value than the target vector, the trial vector
        replaces the target vector in the following generation. The last step is called selection.

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
        Conduct pairwis e comparison over the union of parents (Xi,17i) and off-
        spring (X/ ,17/), Vi E {1, .. . ,p, } . For each individual, q opponents are
        chosen uniformly at random from all the parents and offsprin g. For each
        comparison, if the individual's fitness is no sma ller than the opponent's ,
        it receives a "win."

    """

    # select the best N agents from the union of the parents and offsprings

    # conduct pairwise comparison against q opponents
    # if the individual's fitness is no smaller than the opponent's, it receives a "win"
    all_agents = pop.agents + pop.offsprings
    wins = [0]*len(all_agents)
    for pos, agent in enumerate(all_agents):
        pos_mask = [True]*len(all_agents)
        pos_mask[pos] = False
        opponents = random.choice(list(compress(all_agents,pos_mask)), q)
        ## crucial step!!! => or <= depends on the objective function
        ## and if one wants to minimize or maximize it.
        ## now this is a minimization problem, so we want to select the
        ## agents with the lowest fitness
        wins[pos] = np.sum([agent.fitness <= opponent.fitness for opponent in opponents])

    # select the best N agents from the union of the parents and offsprings
    pop.agents = [all_agents[i] for i in np.argsort(wins)[::-1][:pop.N]]
    pop.offsprings = [] # reset offsprings to empty list
    pass


def dea(params):
    """
        Your docstr here
    """

    T = params['T']  # get the coresponding parameter from the params dict.
    # initialise the population
    init_pop = initialise(params['N'], params['n'], params['xL'], params['xU'])

    t = 0
    mean_fit = []
    best_walk = []
    while t < T:
        # write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select

        # 1. mutate
        mutate(init_pop)
        # 2. evaluate
        m = mean(evaluate(init_pop, params['f']))
        # 3. select
        select(init_pop, params['q'])
        t += 1
        
        mean_fit += [m]
        print(f"Mean fitness {t} : ", m)
        
        # plotting purposes
        best_walk.append(init_pop.agents[0].fitness)
        if params['verbose']:
            print(f"Generation {t}: mean fitness = {mean_fit[-1]}")
    
    # since they are ordered by fitness, the best solution is the first one
    best_agent = init_pop.agents[0].x
#    best_agent = min(pop.offsprings + pop.agents, key=lambda agent: agent.fitness)

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


@np.vectorize
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
        'T': 50,
        'q': 10,
        'N': 100,
        'f': target_function1,
        'verbose': False,
        'xU': 3.,
        'xL': -3.
    }
    return dea(params)


def test_dea_with_target_function2():
    params = {
        'n': 30,
        'T': 150,
        'q': 25,
        'N': 100,
        'f': target_function2,
        'verbose': True,
        'xU': 50.,
        'xL': -50.
    }
    return dea(params)

def test_dea_with_target_function3():
    params = {
        'n': 30,
        'T': 150,
        'q': 25,
        'N': 100,
        'f': target_function3,
        'verbose': True,
        'xU': 1.5,
        'xL': -1.5
    }
    return dea(params)



def main():
    best_pop, mean_fitnesses1, best_agent, best_walk = test_dea_with_target_function1()
    best_pop, mean_fitnesses2, best_agent, best_walk = test_dea_with_target_function2()

    best_pop, mean_fitnesses3, best_agent, best_walk = test_dea_with_target_function3()

    args = parseArguments()
    

    
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    axs[0].plot(mean_fitnesses1, "o-")
    axs[0].set_title("Optimization of the function "+target_function1.__doc__)
    axs[0].set_xlabel("Generation(t)")
    axs[0].set_ylabel("Population mean fitness")

    axs[1].plot(mean_fitnesses2, "o-")
    axs[1].set_title("Optimization of the function "+target_function2.__doc__)
    axs[1].set_xlabel("Generation(t)")
    axs[1].set_ylabel("Population mean fitness")

    axs[2].plot(mean_fitnesses3, "o-")
    axs[2].set_title("Optimization of the function "+target_function3.__doc__)
    axs[2].set_xlabel("Generation(t)")
    axs[2].set_ylabel("Population mean fitness")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
