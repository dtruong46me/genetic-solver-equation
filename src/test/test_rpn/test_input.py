
import unittest
import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from rpn.input import *

class TestReversePolishNotation(unittest.TestCase):
    def test_reverse_polish_notation(self):
        test_cases = [
            # Test case 1
            ("x+1", ['x', '1', '+']),

            # Test case 2
            ("x^2 + log(x+1, 10)", ['x', '2', '^', 'x', '1', '+', '10', 'log', '+']),

            # Test case 3
            ("(x+1)^2 - 3*x", ['x', '1', '+', '2', '^', '3', 'x', '*', '-']),

            # Test case 4
            ("sin((x+1)^2)", ['x', '1', '+', '2', '^', 'sin']),

            # Test case 5
            ("sin(x^2+1) + ln((x+1)^2) - sqrt(16*x)", ['x', '2', '^', '1', '+', 'sin', 'x', '1', '+', '2', '^', 'ln', '+', '16', 'x', '*', 'sqrt', '-']),

            # Test case 6
            ("3*x + 2.5*x^2 - 7", ['3', 'x', '*', '2.5', 'x', '2', '^', '*', '+', '7', '-']),

            # Test case 7
            ("x - -1 + -2", ['x', '-1', '-', '-2', '+']),

            # Test case 8
            ("x^2 * x - x*x^2", ['x', '2', '^', 'x', '*', 'x', 'x', '2', '^', '*', '-']),

            # Test case 9
            ("x*(x+1) - (x-2)*x", ['x', 'x', '1', '+', '*', 'x', '2', '-', 'x', '*', '-']),

            # Test case 10
            ("((x+1)^2 - (x-2)^2)/((x+1)^2 + (x-2)^2)", 
            ['x', '1', '+', '2', '^', 'x', '2', '-', '2', '^', '-', 'x', '1', '+', '2', '^', 'x', '2', '-', '2', '^', '+', '/'])
        ]

        for expression, expected_output in test_cases:
            with self.subTest(expression=expression, expected_output=expected_output):
                tokens = tokenize(expression)
                output = reverse_polish_notation(tokens)
                self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()