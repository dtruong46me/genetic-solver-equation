from solver import Solver

equation = input('> Enter the equation: ') 
min_range = int(input("Enter min range: "))
max_range = int(input("Enter max range: "))

solver = Solver(equation=equation, min_range= min_range, max_range=max_range)
solver.solve()