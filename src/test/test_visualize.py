import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from main.solver import Solver
from main.visualize import Visualize

def main():
    # Handle the equation here
    equation = "x^2 - 5*x -8"

    solver = Solver(equation=equation, min_range=-7, max_range=7)
    x_result, y_result, fitness, execution_time=solver.solve()
    Visualize.plot_result(x_result, y_result)

if __name__ == '__main__':
    main()