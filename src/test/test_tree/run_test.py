import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
path = os.path.abspath(os.path.join(path, ".."))
sys.path.insert(0, path)

from input_handling.parser_tree.lexer import Lexer
from input_handling.parser_tree.parser_ import Parser
from input_handling.parser_tree.interpreter import Interpreter
from input_handling.parser_tree.utils import *

while True:
    text = Utils.text_handle(input(">Enter the expression: "))
    print(text)
    try:
        if text == "":
            print("End of testing")
            break
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree: continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)
        print(type(value.value))
    except Exception as e:
        print(e)



