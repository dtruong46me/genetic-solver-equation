import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from main.input import *

def main():

    test_case1 = "(x+1)^2"
    test_case2 = "sin(x^2+1)^2"
    test_case3 = "log((x+1), 2)-16^(x^2+1)"

    tokens1 = tokenize(test_case1)
    tokens2 = tokenize(test_case2)
    tokens3 = tokenize(test_case3)

    output1 = reverse_polish_notation(tokens1)
    output2 = reverse_polish_notation(tokens2)
    output3 = reverse_polish_notation(tokens3)

    print(output1)
    print(output2)
    print(output3)


if __name__ == '__main__':
    main()