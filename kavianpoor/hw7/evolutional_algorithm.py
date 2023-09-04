import numpy as np
from matplotlib import pyplot as plt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, SUPPRESS

class Population:
    def __init__(self, size, dim, bounds):
        self.size = size
        self.dim = dim
        self.individuals = np.random.uniform(bounds[0], bounds[1], (self.size, self.dim))
        self.fitness = np.zeros(self.size)
        self.eta = np.random.uniform(bounds[0], bounds[1], (self.size, self.dim))
        self.sigma = np.zeros(self.size)

    def initialise(self, function):
        self.fitness = function(self.individuals)

    def evaluate(self, function):
        self.fitness = function(self.individuals)

    def mutate(self):
        self.individuals += self.eta * np.random.normal(0, 1, (self.size, self.dim))

    def select(self):
        best_individuals = self.individuals[np.argsort(self.fitness)[:self.size // 2]]
        worst_individuals = self.individuals[np.argsort(self.fitness)[self.size // 2:]]
        self.individuals = np.concatenate((best_individuals, best_individuals + np.random.normal(0, 1, (self.size // 2, self.dim))))
        self.eta = np.concatenate((self.eta[:self.size // 2], np.abs(self.eta[self.size // 2:] + np.random.normal(0, 1, (self.size // 2, self.dim)))))

def dea(function, bounds, dim=2, size=50, max_iter=1000):
    population = Population(size, dim, bounds)
    population.initialise(function)
    best_fitness = []
    for _ in range(max_iter):
        population.mutate()
        population.evaluate(function)
        population.select()
        best_fitness.append(np.min(population.fitness))
    return best_fitness

def parseArguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter, argument_default=SUPPRESS)
    parser.add_argument("-n", '--length', type=int, default=3, help="Dimension of the solution space")
    parser.add_argument('-T', type=int, default=50, help='Number of generations of the DEA')
    parser.add_argument('-N', type=int, default=100, help='Population size')
    parser.add_argument('-xL', type=float, default=-3., help='Lower bound of the solution space')
    parser.add_argument('-xU', type=float, default=3., help='Upper bound of the solution space')
    parser.add_argument('--verbose', action="store_true", default=False,
                        help="Print the mean fitness evolution on standard output ")
    parser.add_argument('-seed', type=int, default=None, help="Seed for the initial population")
    return parser.parse_args()

def target_function1(X):
    return np.sum(X**2, axis=1)

def target_function2(X):
    return np.abs(X).sum(axis=1) + np.prod(np.abs(X), axis=1)

def target_function3(X):
    return np.sum(np.floor(X), axis=1)

def main():
    args = parseArguments()
    np.random.seed(args.seed)
    bounds = (args.xL, args.xU)

    functions = [target_function1, target_function2, target_function3]

    for function in functions:
        best_fitness = dea(function, bounds, dim=args.length, size=args.N, max_iter=args.T)
        plt.plot(best_fitness)
        plt.title("Fitness Evolution for Target Function: " + function.__name__)
        plt.xlabel('Generations')
        plt.ylabel('Best Fitness')
        plt.show()

if __name__ == "__main__":
    main()

