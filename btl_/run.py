from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
from utils import *

while True:
    text = Utils.text_handle(input(">Enter the expression: "), float(input(">Enter value for x: ")))
    # text = util.text_handle(input_text)
    # if 'x' in text:
    #     x = float(input(">Enter the value of x: "))
    #     text = text.replace('x', str(x))
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
        # print(type(value.value))
    except Exception as e:
        print(e)

"""((2+1)^2 - (2-2)^2)/((2+1)^2 + (2-2)^2)"""

