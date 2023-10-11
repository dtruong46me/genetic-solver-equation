import random

from evaluate import *

def fitness(x, handled_expr):

    return abs(evaluate(output=handled_expr, x_value=x))

def initialize_population(population_size: int, min_value, max_value) -> list:

    return [random.uniform(min_value, max_value) for _ in range(population_size)]

def crossover(parent1, parent2):
    alpha = random.uniform(0, 1)

    child1 = alpha * parent1 + (1-alpha) * parent2
    child2 = (1-alpha) * parent1 + alpha * parent2

    return child1, child2

def mutation(individual, mutation_rate, min_value, max_value):
    if random.random() < mutation_rate:
        individual += random.uniform(-1, 1)
        individual = max(min_value, min(individual, max_value))

    return individual


def genetic_algorithm(handled_expr: list, population_size=100, min_value=-10, max_value=10, mutation_rate=0.1, generations=50):

    population = initialize_population(population_size, min_value, max_value)

    for generation in range(generations):
        fitness_score = [fitness(x, handled_expr) for x in population]
        
        # Find best individual
        best_fitness_score = min(fitness_score)
        best_individual_index = fitness_score.index(best_fitness_score)
        best_individual = population[best_individual_index]

        # Select parents to crossover (Select 1/2 of population)
        selected_parents = random.sample(population, population_size//2)

        new_population = []

        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_parents, 2)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutation(child1, mutation_rate, min_value, max_value)
            child2 = mutation(child2, mutation_rate, min_value, max_value)

            new_population.extend([child1, child2])
        
        population = new_population

    return best_individual