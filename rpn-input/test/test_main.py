
from rpn.ga import *
from rpn.input import *
from rpn.evaluate import *

def main():
    expression = input()
    tokens = tokenize(expression)
    output = reverse_polish_notation(tokens)

    ga_solution = genetic_algorithm(handled_expr=output, min_value=0.2, max_value=10)

    print(ga_solution)

    return

if __name__ == '__main__':
    main()