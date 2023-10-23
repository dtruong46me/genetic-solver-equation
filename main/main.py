import os
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from input_handling.core.utils import *
from input_handling.core.interpreter import Interpreter
from input_handling.core.parser_ import Parser
from input_handling.core.lexer import Lexer
import numpy as np
from random import random, randint, sample

equation = input('>Enter the equation: ') 
if equation == '':
    print('Can not calculate empty equations')
    exit(0)
    
mutation_rate = 0.2
elite = True
elite_group = 8
if elite_group % 2 != 0:
    print("elitism_group must be an even number")
    exit(0)
tournament_group = 20

population = 500
if population % 2 != 0:
    print("Population must be an even number")
    exit(0)

gen_num = 0
current_gen = []
next_gen = []
fitness_lst = []
distance_from_target = 10
genome_length = 32
iterations = 1000
counter = 0


# selecting the best offspring from a group of tournament_group
def tournament_selection():
    random_offsprings = sample(range(len(current_gen)), tournament_group)
    offsprings_fitness = [fitness_lst[g] for g in random_offsprings]
    return current_gen[random_offsprings[np.argmax(offsprings_fitness)]]


# cross overing some of the genes by a random cut
def cross_over(genome_1, genome_2):
    random_slice = randint(10, 20)
    genome_1_out = genome_1[:random_slice] + genome_2[random_slice:]
    genome_2_out = genome_2[:random_slice] + genome_1[random_slice:]
    return genome_1_out, genome_2_out

# mutating a random bit of a given genome by a crossing rate
def mutate(genome):
    genome = list(genome)
    for g in range(len(genome)):
        if random() < mutation_rate:
            genome[g] = str((int(genome[g]) + 1) % 2)
    return "".join(genome)

# transfer the best x offsprings of the previous generation to the next, x = elitism_group
def elite_func():
    global fitness_lst, current_gen, next_gen
    best_offsprings = np.argsort(fitness_lst)[-elite_group:]
    indx = elite_group - 1
    for i in best_offsprings:
        if len(next_gen) < elite_group:
            next_gen.append(current_gen[i])
        else:
            indx -= 1
            next_gen[indx] = current_gen[i]
            next_gen[population - elite_group + indx] = mutate(current_gen[i])
    for p in range(elite_group - 1):
        for g in range(p + 1, elite_group):
            try:
                if abs(binary32_to_float(next_gen[p]) - binary32_to_float(next_gen[g])) < 0.05:
                    next_gen[g] = create_rand_genome()
            except OverflowError:
                pass


# evaluating the fitness/accuracy of a given genome
def fitness_evaluate(genome):
    global counter
    counter += 1
    input_num = binary32_to_float(genome)
    splited_eq = equation.replace('x', format(input_num, '.5f')).split('=')
    left_side, right_side = splited_eq[0].strip(), splited_eq[1].strip()
    
    lexer = Lexer(left_side)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    
    try:
        distance = abs(value.value  - float(right_side))
        if distance > distance_from_target or input_num > 1e4 or input_num < -1e4:
            return 0
    except Exception:
        return 0

    return 1 / (distance + 1e-10)


# creating a new generation
def create_new_gen():
    global current_gen, next_gen
    if not elite:
        if len(next_gen) == 0:
            for pop in range(int(population / 2)):
                offspring_1, offspring_2 = cross_over(
                    tournament_selection(), tournament_selection())
                offspring_1, offspring_2 = mutate(
                    offspring_1), mutate(offspring_2)
                next_gen.append(offspring_1)
                next_gen.append(offspring_2)
        else:
            for pop in range(int(population / 2)):
                offspring_1, offspring_2 = cross_over(
                    tournament_selection(), tournament_selection())
                offspring_1, offspring_2 = mutate(
                    offspring_1), mutate(offspring_2)
                next_gen[pop * 2] = offspring_1
                next_gen[pop * 2 + 1] = offspring_2
    else:
        # elitism function
        elite_func()
        if len(next_gen) == elite_group:
            for pop in range(int(elite_group/2), int(population / 2)):
                offspring_1, offspring_2 = cross_over(
                    tournament_selection(), tournament_selection())
                offspring_1, offspring_2 = mutate(
                    offspring_1), mutate(offspring_2)
                next_gen.append(offspring_1)
                next_gen.append(offspring_2)
        else:
            for pop in range(elite_group, int(population / 2)):
                offspring_1, offspring_2 = cross_over(
                    tournament_selection(), tournament_selection())
                offspring_1, offspring_2 = mutate(
                    offspring_1), mutate(offspring_2)
                next_gen[pop * 2 - elite_group] = offspring_1
                next_gen[pop * 2 + 1 - elite_group] = offspring_2

    current_gen = next_gen.copy()


# updating the fitness
def fitness_update():
    if len(fitness_lst) == 0:
        for pop in range(population):
            fitness_lst.append(fitness_evaluate(current_gen[pop]))
    else:
        for pop in range(population):
            fitness_lst[pop] = fitness_evaluate(current_gen[pop])


# creating generation 0 with random offsprings
def init_gen_0():
    for pop in range(population):
        current_gen.append(create_rand_genome())


# create random genome of length: genome_length=32
def create_rand_genome():
    out = ''
    for g in range(genome_length):
        rand_num = randint(0, 1)
        out += str(rand_num)
    return out


def binary32_to_float(binary_str):
    sign_bit = int(binary_str[0])
    exponent_bits = binary_str[1:9]
    fraction_bits = binary_str[9:]

    exponent = int(exponent_bits, 2) - 127
    fraction = 1 + sum(int(bit) * 2**(-i)
                       for i, bit in enumerate(fraction_bits, start=1))

    value = (-1) ** sign_bit * 2 ** exponent * fraction
    return value


if __name__ == '__main__':
    init_gen_0()
    fitness_update()
    
    create_new_gen()
    for i in range(iterations):
        fitness_update()
        print(list(map(binary32_to_float, [current_gen[g] for g in np.argsort(fitness_lst)[-1:]]))[0])
        create_new_gen()
