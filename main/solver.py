import os
import sys
import timeit
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from input_handling.core.utils import *
from input_handling.core.interpreter import Interpreter
from input_handling.core.parser_ import Parser
from input_handling.core.lexer import Lexer
import numpy as np
from random import random, randint, sample

class Genetic_Algorithm:
    def __init__(self, min_range = -1e10, max_range = 1e10):
        self.min_range = min_range
        self.max_range = max_range
        self.equation = input('> Enter the equation: ') 
        if self.equation == '':
            print('Can not calculate empty equations')
            exit(0)
        
        self.mutation_rate = 0.2
        self.elite = True
        self.elite_group = 4
        if self.elite_group % 2 != 0:
            print("elitism_group must be an even number")
            exit(0)
        self.random_group = 8
        
        self.population = 200
        # if self.population % 2 != 0:
        #     print("Population must be an even number")
        #     exit(0)

        self.gen_num = 0
        self.current_gen = []
        self.next_gen = []
        self.fitness = []
        self.distance_from_target = 1000
        self.genome_length = 32
        self.iterations = 1100
        self.counter = 0


        # selecting the best child from a group of random_group
    def random_selection(self):
        random_child = sample(range(len(self.current_gen)), self.random_group)
        child_fitness = [self.fitness[g] for g in random_child]
        
        return self.current_gen[random_child[np.argmax(child_fitness)]]


        # cross overing some of the genes by a random cut
    def cross_over(self, genome_1, genome_2):  
        random_slice = randint(1, self.genome_length - 1)
        genome_1_child = genome_1[:random_slice] + genome_2[random_slice:]
        genome_2_child = genome_2[:random_slice] + genome_1[random_slice:]
            
        return genome_1_child, genome_2_child

        # mutating a random bit of a given genome by a crossing rate
    def mutate(self, genome):
        genome = list(genome)
        for g in range(len(genome)):
            if random() < self.mutation_rate:
                genome[g] = str((int(genome[g]) + 1) % 2)
                
        return "".join(genome)

       # transfer the best x childs of the previous generation to the next, x = elitism_group
    def elite_func(self):
        # global fitness, current_gen, next_gen
        best_childs = np.argsort(self.fitness)[-self.elite_group:]
        indx = self.elite_group - 1
        for i in best_childs:
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
        if len(splited_eq) == 1: 
            left_side = splited_eq[0].strip()
            right_side = '0'
        else:
            left_side, right_side = splited_eq[0].strip(), splited_eq[1].strip()
    
        leftLexer, rightLexer = Lexer(left_side), Lexer(right_side)
        left_tokens, right_tokens = leftLexer.generate_tokens(), rightLexer.generate_tokens()
        left_parser, right_parser = Parser(left_tokens), Parser(right_tokens)
        leftTree, rightTree = left_parser.parse(), right_parser.parse()
        left_interpreter, right_interpreter = Interpreter(), Interpreter()
        left_value, right_value = left_interpreter.visit(leftTree), right_interpreter.visit(rightTree)
          
        distance = abs(left_value.value  - right_value.value)
        
        if  input_num > self.max_range or input_num < self.min_range:
            return 0
        
        return 1/ (1 + distance)
    

    # creating a new generation
    def create_new_gen(self):
        # global current_gen, next_gen
        if not self.elite:           
            if len(self.next_gen) == 0:
                for pop in range(int(self.population / 2)):
                    child_1, child_2 = self.cross_over(self.random_selection(), self.self.random_selection())
                    child_1, child_2 = self.mutate(child_1), self.mutate(child_2)
                    self.next_gen.append(child_1)
                    self.next_gen.append(child_2)
            else:
                for pop in range(int(self.population / 2)):
                    child_1, child_2 = self.cross_over(self.random_selection(), self.random_selection())
                    child_1, child_2 = self.mutate(child_1)
                    self.next_gen[pop * 2] = child_1
                    self.next_gen[pop * 2 + 1] = child_2
        else:
            # elitism function
            self.elite_func()
            if len(self.next_gen) == self.elite_group:
                for pop in range(int(self.elite_group/2), int(self.population / 2)):
                    child_1, child_2 = self.cross_over(
                        self.random_selection(), self.random_selection())
                    child_1, child_2 = self.mutate(
                        child_1), self.mutate(child_2)
                    self.next_gen.append(child_1)
                    self.next_gen.append(child_2)
            else:
                for pop in range(self.elite_group, int(self.population / 2)):
                    child_1, child_2 = self.cross_over(
                        self.random_selection(), self.random_selection())
                    child_1, child_2 = self.mutate(
                        child_1), self.mutate(child_2)
                    self.next_gen[pop * 2 - self.elite_group] = child_1
                    self.next_gen[pop * 2 + 1 - self.elite_group] = child_2

        self.current_gen = self.next_gen.copy()


        # updating the fitness
    def fitness_update(self):
        if len(self.fitness) == 0:
            for pop in range(self.population):
                self.fitness.append(self.fitness_evaluate(self.current_gen[pop]))
        else:
            for pop in range(self.population):
                self.fitness[pop] = self.fitness_evaluate(self.current_gen[pop])


       # creating generation 0 with random childs
    def create_gen_0(self):
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
        self.create_gen_0()
        self.fitness_update()              
        self.create_new_gen()
        startTime = timeit.default_timer()
        while True: # for i in range(self.iterations):
            self.fitness_update()
            best_index = np.argsort(self.fitness)[-1]
            best_binary = self.current_gen[best_index] 
            print('Result: ', self.binary32_to_float(best_binary), '  ', \
                            'Fitness: ', self.fitness[best_index] )
            self.create_new_gen()
            
            if timeit.default_timer() - startTime > 10:
                break
            
            