import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS


class Population:
    def __init__(self, n, N, x, eta):
        self.n = n
        self.N = N
        self.x = x
        self.eta = eta
        self.fitness = np.reshape(np.apply_along_axis(func1d=f, axis=1, arr=self.x), (N, 1))
        self.tau = np.sqrt(2 * np.sqrt(self.n)) ** -1  # from "Fast Evolutionary Algorithms", page 48
        self.tau_prime = np.sqrt(2 * self.n) ** -1  # from "Fast Evolutionary Algorithms", page 48

    def get_best_x(self):
        return self.x[np.argmin(self.fitness)]

    def get_mutated_population(self, seed, xL, xU):
        """
            Mutation operation - get a slightly different population from an existing one
            stay in the bounds of the solution space
        """
        rng = np.random.default_rng(seed)
        N_j = rng.uniform(0, 1, self.n)

        ## COMMENTS: Please check the description... N_j is not the the same for all x and eta.
        mutated_pop = Population(self.n, self.N,
                                 x=np.clip(self.x + self.eta * N_j, xL, xU),
                                 eta=self.eta * np.exp(self.tau_prime * N_j + self.tau * N_j)
                                 )
        return mutated_pop

    def select(self, mutated_pop, q, seed):
        """
            Selection operation - get best N samples from self and mutated_pop
            Uses a probabilistic selection scheme, that is not entirely elitist.
        """
        rng = np.random.default_rng(seed)
        n = self.n
        N = self.N

        wins = np.zeros(2 * N, dtype=int)  # first N entries: self, second N entries: mutated_pop
        # combine fitness from self and mutated_pop
        all_fitness = np.concatenate((self.fitness, mutated_pop.fitness))
        # for all solutions, compare with q other solutions and promote winner
        for candidate_index in range(2 * N):
            # get q opponent indexes to compare opponent's fitness with current candidate's fitness
            opponent_indexes = rng.integers(0, 2 * N, q)
            for opponent_index in opponent_indexes:
                if all_fitness[candidate_index] <= all_fitness[opponent_index]:
                    wins[candidate_index] += 1 ## GOOD but think of vectorizing it.

        # get best N samples from self and mutated combined and build new population
        x, eta = np.empty((N, n)), np.empty((N, n))
        # get best N samples to put into x and eta
        for i in range(N):
            best_index = np.argmax(wins)
            x[i] = self.x[best_index] if best_index < N else mutated_pop.x[best_index - N]
            eta[i] = self.eta[best_index] if best_index < N else mutated_pop.eta[best_index - N]
            wins[best_index] = 0
        selected_pop = Population(n, N, x, eta)
        return selected_pop


def differential_evolutionary_algorithm(initial_pop, params):
    """
        Differential Evolutionary Algorithm (DEA) as a loop of
            Mutation Operation
            (Crossover Operation) - not present here
            Selection Operation
        until stoppage criterion satisfied (number of generations reached)
    """

    prev_pop = initial_pop
    mean_fitness = []
    best_x = initial_pop.get_best_x()

    t = 0
    while t < params['T']:
        ## Write your code here to implement the DEA. The steps should be 1. mutate, 2. evaluate, 3. select
        # 1. Mutate
        mutated_pop = prev_pop.get_mutated_population(params['seed'], params['xL'], params['xU'])
        # 2. Evaluate
        # Fitness of the population is calculated in constructor internally.
        # 3. Crossover - Not existent
        # 4. Select
        selected_pop = prev_pop.select(mutated_pop, params['q'], params['seed'])

        # Evaluate this run
        m = np.mean(selected_pop.fitness)
        mean_fitness.append(m)
        if params['verbose']:
            print(f"Mean fitness {t} : ", m)

        # Save best solution
        current_best_x = selected_pop.get_best_x()
        best_x = current_best_x if f(current_best_x) < f(best_x) else best_x

        # make deep copy
        prev_pop = Population(selected_pop.n, selected_pop.N, selected_pop.x, selected_pop.eta)
        t += 1
    return prev_pop, mean_fitness, best_x


def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=3, help="Dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generations of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3., help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=3., help='Upper bound of the solution space')
    parser.add_argument('-q', type=int, default=10, help='Number of mutants for pairwise comparison')
    parser.add_argument('--verbose', action="store_true", default=False,
                        help="Print the mean fitness evolution on standard output ")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()


def f(x):
    # First function: Polynomial from ICDS lecture slides
    # """x^4 + x^3 - x^2 - x"""  # n = 1, True global minimum is at x = 0.64039, f(x) = -0.61968
    #return x**4 + x**3 - x**2 - x
    # Second function: Sphere Model
    # """x[0]² + x[1]²"""  # n = 2, True global minimum is at (0, 0), f(x) = 0
    # return x[0]**2 + x[1]**2
    # Third function: Rosenbrocks Generalized Model
    """Generalized Rosenbrock, f5 from book, n=3"""  # n = 3, True global minimum is at f(1,1,1) = 0
    return sum([100 * (x[i+1] - x[i]**2)**2 + (x[i]-1)**2 for i in range(3-1)])
    # """Generalized Rosenbrock, f5 from book, n=30"""  # n = 30, True global minimum is at f(1,...,1) = 0
    # return sum([100 * (x[i+1] - x[i]**2)**2 + (x[i]-1)**2 for i in range(30-1)])


def main():
    args = parseArguments()
    ### COMMENTS ###
    # How do we test the two other functions?
    # In your readme, you only repported the function f5 what about the two first ones?

    params = {'n': args.length, 'T': args.T, 'q': args.q, 'N': args.N, 'f': f, 'verbose': args.verbose, 'xU': args.xU,
              'xL': args.xL, 'seed': args.seed}

    # Create initial population
    rng = np.random.default_rng(params['seed'])
    initial_pop = Population(args.length, args.N,
                             x=rng.uniform(args.xL, args.xU, args.N * args.length).reshape((args.N, args.length)),
                             eta=rng.uniform(args.xL, args.xU, args.N * args.length).reshape((args.N, args.length))
                             )

    # Run differential evolution algorithm to search for minimum of function
    best_pop, mean_fitness, best_x = differential_evolutionary_algorithm(initial_pop, params)

    # Plot results
    # print("Best population : ", best_pop.x)
    print("Best solution over all runs: f(", best_x, ") = ",  f(best_x))
    plt.plot(mean_fitness, "o-")
    plt.title("Optimization of " + params['f'].__doc__)
    plt.xlabel("Generation (t)")
    plt.ylabel("Population mean fitness")
    plt.show()


if __name__ == "__main__":
    main()
