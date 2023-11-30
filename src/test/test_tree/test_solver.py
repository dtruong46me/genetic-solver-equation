import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from main.solver import *

def main():
    input_eqt = input()
    solver = Solver(equation=input_eqt, min_range=-10, max_range=10)

    result = solver.solve()
    print(result)
    print(result[0][-1])
    print(result[3])

if __name__ == '__main__':
    main()
 