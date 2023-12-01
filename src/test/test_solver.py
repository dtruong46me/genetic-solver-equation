import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from main.solver import *

def main():
    input_eqt = "x^2 - 5*x + 6"
    solver = Solver(equation=input_eqt, min_range=-10, max_range=10)

    result = solver.solve()

    print("\n==================")
    print(f"Solution: {result[0][-1]:.6f}")
    print(f"Execution time: {result[3]}")
    print("==================\n")


if __name__ == '__main__':
    main()
 