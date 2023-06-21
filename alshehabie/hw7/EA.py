import numpy as np
import random

def f1(x):
    return x**4 + x**3 - x**2 - x

def f2(x):
    return np.sum(x)

def f3(x):
    n = len(x)
    result = 0
    for j in range(1, n):
        term = 100 * (x[j] + 1 - x[j-1]**2)**2 + (x[j-1] - 1)**2
        result += term
    return result

def initialize_population(N, n, xL, xU):
    population = np.zeros((N, n))
    for i in range(N):
        ri = np.random.uniform(size=n)
        xi = ri * (xU - xL) + xL
        population[i] = xi
    return population

def evaluate_fitness(population, func):
    fitness = np.zeros(population.shape[0])
    for i in range(population.shape[0]):
        fitness[i] = func(population[i])
    return fitness

def mutation(population, F, bounds):
    N, n = population.shape
    mutated_population = np.zeros_like(population)

    for i in range(N):
        indices = [idx for idx in range(N) if idx != i]
        a, b, c = np.random.choice(indices, 3, replace=False)
        mutant = population[a] + F * (population[b] - population[c])
        mutated_population[i] = np.clip(mutant, bounds[:, 0], bounds[:, 1])

    return mutated_population

def pairwise_comparison(population, offspring, q, fitness_func):
    wins = [0] * len(population)

    for i in range(len(population)):
        opponents = random.sample(list(population) + list(offspring), q)
        for opponent in opponents:
            if fitness_func(opponent) > fitness_func(population[i]):
                wins[i] += 1

    return wins

def select_parents(population, wins, N):
    sorted_indices = sorted(range(len(wins)), key=lambda k: wins[k], reverse=True)
    selected_parents = [population[i] for i in sorted_indices[:N]]

    return selected_parents

# Parameters
N = 100  # Population size
n = 30  # Number of variables
xL = -30  # Lower bound of variable x
xU = 30  # Upper bound of variable x
F = 0.5  # Mutation scaling factor
q = 5  # Number of opponents for pairwise comparison
max_generations = 100

bounds = np.array([[xL, xU]])

# Initialization
population = initialize_population(N, n, xL, xU)
fitness = evaluate_fitness(population, f3)

# Evolutionary Loop
for generation in range(max_generations):
    mutated_population = mutation(population, F, bounds)

    # Pairwise comparison
    wins = pairwise_comparison(population, mutated_population, q, f3)

    # Selection
    selected_parents = select_parents(population, wins, N)

    population = np.array(selected_parents)
    fitness = evaluate_fitness(population, f3)

# Best individual and fitness
best_index = np.argmin(fitness)
best_individual = population[best_index]
best_fitness = fitness[best_index]

print("Best Individual:", best_individual)
print("Best Fitness:", best_fitness)