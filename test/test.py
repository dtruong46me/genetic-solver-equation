import sys
import os
from main.solving import Genetic_Algorithm
from main.visualize import Visualize

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

solver = Genetic_Algorithm(min_range=-7, max_range=7)
x_result, y_result, fitness, execution_time=solver.solve()
Visualize.plot_result(x_result, y_result, fitness)