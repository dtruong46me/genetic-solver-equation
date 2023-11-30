import unittest
import math
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
path = os.path.abspath(os.path.join(path, ".."))
sys.path.insert(0, path)

from input_handling.parser_tree.lexer import Lexer
from input_handling.parser_tree.parser_ import Parser
from input_handling.parser_tree.interpreter import Interpreter
from input_handling.parser_tree.utils import Utils

class TestEvaluation(unittest.TestCase):
    def test_evaluation(self):

        # All Variables for Test cases
        x_value = {
            # In Test case 1, x=2.0
            1: 2.0, 
            2: 4, 
            3: 5,
            4: 2.5,
            5: 2,
            6: 2,
            7: 2,
            8: 2,
            9: 3,
            10: 2
        }

        # All text cases
        test_cases = [
            # Test case 1
            ("x+1", x_value[1]+1),

            # Test case 2
            ("x^2 + log((x+1), 10)", x_value[2]**2 + math.log(x_value[2]+1, 10)),

            # Test case 3
            ("(x+1)^2 - 3*x", (x_value[3]+1)**2 - 3*x_value[3]),

            # Test case 4
            ("sin((x+1)^2)", math.sin((x_value[4]+1)**2)),

            # Test case 5
            ("sin(x^2+1) + ln((x+1)^2) - sqrt(16*x)", math.sin(x_value[5]**2+1) + math.log((x_value[5]+1)**2) - math.sqrt(16*x_value[5])),

            # Test case 6
            ("3*x + 2.5*x^2 - 7", 3*x_value[6] + 2.5 * x_value[6] ** 2 - 7),

            # Test case 7
            ("x - -1 + -2", x_value[7] - -1 + -2),

            # Test case 8
            ("x^2 * x - x*x^2", x_value[8]**2 * x_value[8] - x_value[8] * x_value[8]**2),

            # Test case 9
            ("x*(x+1) - (x-2)*x", x_value[9] * (x_value[9] + 1) - (x_value[9] - 2) * x_value[9]),

            # Test case 10
            ("((x+1)^2 - (x-2)^2)/((x+1)^2 + (x-2)^2)", ((x_value[10]+1)**2 - (x_value[10]-2)**2) / ((x_value[10]+1)**2 + (x_value[10]-2)**2))
        ]

        i = 1
        for test_case in test_cases:
            expressions = Utils.text_handle(test_case[0], x_value[i])
            expected_values = test_case[1]
            with self.subTest(expression= expressions, expected_value = expected_values):
                lexer = Lexer(expressions)
                tokens = lexer.generate_tokens()
                parser = Parser(tokens)
                tree = parser.parse()
                interpreter = Interpreter()
                result = interpreter.visit(tree)
 
                print(result.value == expected_values, i)
                
                self.assertAlmostEqual(result.value, expected_values, delta=0.00001)
            i += 1

if __name__ == '__main__':
    unittest.main()