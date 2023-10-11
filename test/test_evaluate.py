import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from main.input import *
from main.evaluate import *

def main():

    test_case = "log((x+1), 2)-16^(x^2+1)"

    output = reverse_polish_notation(tokens=tokenize(test_case))

    result = evaluate(output=output, x_value=5)

    print(output)
    print(result)

    return

if __name__ == '__main__':
    main()