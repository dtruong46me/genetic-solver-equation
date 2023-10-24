
import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from rpn.input import *
from rpn.evaluate import *

def main():
    expression = input()
    tokens = tokenize(expression)
    output = reverse_polish_notation(tokens)

    result = evaluate(output=output, x_value=2)

    print(tokens)
    print(output)
    print(result)
    return

if __name__ == '__main__':
    main()