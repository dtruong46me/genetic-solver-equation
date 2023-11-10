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

class Genetic_Algorithm:
    def __init__(self):
        self.equation = input('>Enter the equation: ') 
        if self.equation == '':
            print('Can not calculate empty equations')
            exit(0)
        
        self.cross_over_rate = 1
        self.mutation_rate = 0.2
        self.elite = True
        self.elite_group = 4
        if self.elite_group % 2 != 0:
            print("elitism_group must be an even number")
            exit(0)
        self.tournament_group = 8
        
        self.population = 200
        if self.population % 2 != 0:
            print("Population must be an even number")
            exit(0)

        self.gen_num = 0
        self.current_gen = []
        self.next_gen = []
        self.fitness_lst = []
        self.distance_from_target = 1000
        self.genome_length = 32
        self.iterations = 1100
        self.counter = 0


        # selecting the best offspring from a group of tournament_group
    def tournament_selection(self):
        random_offsprings = sample(range(len(self.current_gen)), self.tournament_group)
        offsprings_fitness = [self.fitness_lst[g] for g in random_offsprings]
        return self.current_gen[random_offsprings[np.argmax(offsprings_fitness)]]


        # cross overing some of the genes by a random cut
    def cross_over(self, genome_1, genome_2):  
        if random() < self.cross_over_rate:
            random_slice = randint(1, self.genome_length - 1)
            genome_1_out = genome_1[:random_slice] + genome_2[random_slice:]
            genome_2_out = genome_2[:random_slice] + genome_1[random_slice:]
            return genome_1_out, genome_2_out
        else:
            return genome_1, genome_2

        # mutating a random bit of a given genome by a crossing rate
    def mutate(self, genome):
        genome = list(genome)
        for g in range(len(genome)):
            if random() < self.mutation_rate:
                genome[g] = str((int(genome[g]) + 1) % 2)
        return "".join(genome)

       # transfer the best x offsprings of the previous generation to the next, x = elitism_group
    def elite_func(self):
        # global fitness_lst, current_gen, next_gen
        best_offsprings = np.argsort(self.fitness_lst)[-self.elite_group:]
        indx = self.elite_group - 1
        for i in best_offsprings:
            if len(self.next_gen) < self.elite_group:
                self.next_gen.append(self.current_gen[i])
            else:
                indx -= 1
                self.next_gen[indx] = self.current_gen[i]
                self.next_gen[self.population - self.elite_group + indx] = self.mutate(self.current_gen[i])
        for p in range(self.elite_group - 1):
            for g in range(p + 1, self.elite_group):
                try:
                    if abs(self.binary32_to_float(self.next_gen[p]) - self.binary32_to_float(self.next_gen[g])) < 0.05:
                        self.next_gen[g] =self.create_rand_genome()
                except OverflowError:
                       pass


        # evaluating the fitness/accuracy of a given genome
    def fitness_evaluate(self, genome):
        self.counter += 1
        input_num = self.binary32_to_float(genome)
        splited_eq = self.equation.replace('x', format(input_num, '.5f')).split('=')
        left_side, right_side = splited_eq[0].strip(), splited_eq[1].strip()
    
        lexer = Lexer(left_side)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        interpreter = Interpreter()
        value = interpreter.visit(tree)
    
        
        distance = abs(value.value  - float(right_side))
        # if input_num > 1e20 or input_num < -1e20: 
        #     return 0
        # except Exception:
        #     return float("-infinity")

        return 1 / (distance + 1)


    # creating a new generation
    def create_new_gen(self):
        # global current_gen, next_gen
        if not self.elite:           
            if len(self.next_gen) == 0:
                for pop in range(int(self.population / 2)):
                    offspring_1, offspring_2 = self.cross_over(self.tournament_selection(), self.self.tournament_selection())
                    offspring_1, offspring_2 = self.mutate(offspring_1), self.mutate(offspring_2)
                    self.next_gen.append(offspring_1)
                    self.next_gen.append(offspring_2)
            else:
                for pop in range(int(self.population / 2)):
                    offspring_1, offspring_2 = self.cross_over(self.tournament_selection(), self.tournament_selection())
                    offspring_1, offspring_2 = self.mutate(offspring_1)
                    self.next_gen[pop * 2] = offspring_1
                    self.next_gen[pop * 2 + 1] = offspring_2
        else:
            # elitism function
            self.elite_func()
            if len(self.next_gen) == self.elite_group:
                for pop in range(int(self.elite_group/2), int(self.population / 2)):
                    offspring_1, offspring_2 = self.cross_over(
                        self.tournament_selection(), self.tournament_selection())
                    offspring_1, offspring_2 = self.mutate(
                        offspring_1), self.mutate(offspring_2)
                    self.next_gen.append(offspring_1)
                    self.next_gen.append(offspring_2)
            else:
                for pop in range(self.elite_group, int(self.population / 2)):
                    offspring_1, offspring_2 = self.cross_over(
                        self.tournament_selection(), self.tournament_selection())
                    offspring_1, offspring_2 = self.mutate(
                        offspring_1), self.mutate(offspring_2)
                    self.next_gen[pop * 2 - self.elite_group] = offspring_1
                    self.next_gen[pop * 2 + 1 - self.elite_group] = offspring_2

        self.current_gen = self.next_gen.copy()


        # updating the fitness
    def fitness_update(self):
        if len(self.fitness_lst) == 0:
            for pop in range(self.population):
                self.fitness_lst.append(self.fitness_evaluate(self.current_gen[pop]))
        else:
            for pop in range(self.population):
                self.fitness_lst[pop] = self.fitness_evaluate(self.current_gen[pop])


       # creating generation 0 with random offsprings
    def init_gen_0(self):
        for pop in range(self.population):
            self.current_gen.append(self.create_rand_genome())


        # create random genome of length: genome_length=32
    def create_rand_genome(self):
        out = ''
        for g in range(self.genome_length):
            rand_num = randint(0, 1)
            out += str(rand_num)
        return out

    def binary32_to_float(self, binary_str):
        sign_bit = int( binary_str[0])
        exponent_bits = binary_str[1:9]
        fraction_bits = binary_str[9:]
        
        exponent = int(exponent_bits, 2) - 127
        fraction = 1 + sum(int(bit) * 2**(-i)
                               for i, bit in enumerate(fraction_bits, start=1))

        value = (-1) ** sign_bit * 2 ** exponent * fraction
        return value
            
    # solve equation
    def solve(self):
        self.init_gen_0()
        self.fitness_update()              
        self.create_new_gen()
        for i in range(self.iterations):
            self.fitness_update()
            print(list(map(self.binary32_to_float, [self.current_gen[g] for g in np.argsort(self.fitness_lst)[-1:]]))[0])
            self.create_new_gen()
            
    