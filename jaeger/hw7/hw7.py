from numpy import random, mean, sqrt, exp, argsort, sum, abs, vectorize
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS
from itertools import compress


def initialise(N, n, xL, xU):
    """
    Initialize the population for the Differential Evolution Algorithm.

    Args:
        N (int): Population size.
        n (int): Dimension of the solution space.
        xL (float): Lower bound of the solution space.
        xU (float): Upper bound of the solution space.

    Returns:
        dict: Initial population dictionary containing agent information.
    """
    all_x = [[random.uniform(0, 1) * (xU - xL) + xL for _ in range(n)] for _ in range(N)]
    all_eta = [random.uniform(0, 1) * (xU - xL) + xL for _ in range(N)]

    agents = []

    for i in range(N):
        agent_dict = {
            "x": all_x[i],
            "eta": all_eta[i],
            "fitness": None
        }
        agents.append(agent_dict)

    population_dict = {
        "n": n,
        "N": N,
        "x_l": xL,
        "x_u": xU,
        "offsprings": [],
        "generation": 0,
        "agents": agents
    }

    return population_dict


def evaluate(pop, f):
    """
    Evaluate the fitness of each agent in the population using the given function.

    Args:
        pop (dict): Population dictionary containing agent information.
        f (function): Fitness function to evaluate.

    Returns:
        list: List of fitness values for each agent in the population.
    """
    for agent in pop["agents"] + pop["offsprings"]:
        agent["fitness"] = f(agent["x"])
    return [agent["fitness"] for agent in pop["agents"]]


def mutate(pop):
    """
    Mutate the population for the next generation.

    Args:
        pop (dict): Population dictionary containing agent information.

    Returns:
        dict: Updated population dictionary after mutation.
    """
    pop["generation"] += 1
    tau = sqrt(2 * sqrt(pop["n"])) ** -1
    tau_prime = sqrt(2 * pop["n"]) ** -1

    for agent in pop["agents"]:
        agent_dict = {
            "x": agent["x"] + agent["eta"] * random.normal(0, 1, pop["n"]),
            "eta": agent["eta"] * exp(tau_prime * random.normal(0, 1, 1) + tau * random.normal(0, 1, pop["n"])),
            "fitness": None
        }

        pop["offsprings"].append(agent_dict)

    return pop


def select(pop, q=10):
    """
    Select the fittest agents for the next generation.

    Args:
        pop (dict): Population dictionary containing agent information.
        q (int, optional): Number of mutants for pairwise comparison. Defaults to 10.

    Returns:
        dict: Updated population dictionary after selection.
    """
    all_agents = pop["agents"] + pop["offsprings"]
    wins = [0] * len(all_agents)
    for pos, agent in enumerate(all_agents):
        pos_mask = [True] * len(all_agents)
        pos_mask[pos] = False
        opponents = random.choice(list(compress(all_agents, pos_mask)), q)
        wins[pos] = sum([agent["fitness"] <= opponent["fitness"] for opponent in opponents])

    pop["agents"] = [all_agents[i] for i in argsort(wins)[::-1][:pop["N"]]]
    pop["offsprings"] = []
    return pop


def dea(params):
    """
    Perform Differential Evolution Algorithm.

    Args:
        params (dict): Parameters for the algorithm.

    Returns:
        tuple: Tuple containing the final population, mean fitness values, best agent, and best fitness values.
    """
    T = params['T']  # Get the corresponding parameter from the params dict.
    init_pop = initialise(params['N'], params['n'], params['xL'], params['xU'])

    t = 0
    mean_fit = []
    best_walk = []
    while t < T:
        # Write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        mutate(init_pop)
        m = mean(evaluate(init_pop, params['f']))
        select(init_pop, params['q'])
        t += 1

        mean_fit.append(m)
        print(f"Mean fitness {t}: {m}")

        # Plotting purposes
        best_walk.append(init_pop["agents"][0]["fitness"])
        if params['verbose']:
            print(f"Generation {t}: mean fitness = {mean_fit[-1]}")

    # Since they are ordered by fitness, the best solution is the first one
    best_agent = init_pop["agents"][0]["x"]

    return init_pop, mean_fit, best_agent, best_walk


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=1, help="The dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generations of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3., help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=3., help='Upper bound of the solution space')
    parser.add_argument('-q', type=int, default=10, help='Number of mutants for pairwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False, help="Print the mean fitness evolution on a standard output")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    parser.add_argument('-f', default=None, help="Polynomial to evaluate")
    return parser.parse_args()


@vectorize
def target_function1(x):
    """
    Target function 1.

    Args:
        x (float): Input value.

    Returns:
        float: Function output.
    """
    return (x ** 4 + x ** 3 - x ** 2 - x)


@vectorize
def target_function2(x):
    """
    Target function 2.

    Args:
        x (float): Input value.

    Returns:
        float: Function output.
    """
    return abs(sum(x))


def target_function3(x):
    """
    Target function 3.

    Args:
        x (array-like): Input values.

    Returns:
        float: Function output.
    """
    y = 0
    for i in range(len(x) - 1):
        y += 100 * ((x[i + 1] - x[i] ** 2) ** 2) + (x[i] - 1) ** 2
    return y


def test_target_function1():
    """
    Test DEA with target function 1.

    Returns:
        tuple: Tuple containing the final population, mean fitness values, best agent, and best fitness values.
    """
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


def test_target_function2():
    """
    Test DEA with target function 2.

    Returns:
        tuple: Tuple containing the final population, mean fitness values, best agent, and best fitness values.
    """
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


def test_target_function3():
    """
    Test DEA with target function 3.

    Returns:
        tuple: Tuple containing the final population, mean fitness values, best agent, and best fitness values.
    """
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
    best_pop, mean_fitness1, best_agent, best_walk = test_target_function1()
    best_pop, mean_fitness2, best_agent, best_walk = test_target_function2()

    best_pop, mean_fitness3, best_agent, best_walk = test_target_function3()

    args = parseArguments()

    fig, axs = plt.subplots(3, 1, figsize=(8, 12))
    axs[0].plot(mean_fitness1, "o-")
    axs[0].set_title("Optimization of the function " + target_function1.__doc__)
    axs[0].set_xlabel("Generation(t)")
    axs[0].set_ylabel("Population mean fitness")

    axs[1].plot(mean_fitness2, "o-")
    axs[1].set_title("Optimization of the function " + target_function2.__doc__)
    axs[1].set_xlabel("Generation(t)")
    axs[1].set_ylabel("Population mean fitness")

    axs[2].plot(mean_fitness3, "o-")
    axs[2].set_title("Optimization of the function " + target_function3.__doc__)
    axs[2].set_xlabel("Generation(t)")
    axs[2].set_ylabel("Population mean fitness")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
