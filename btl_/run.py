from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
while True:
    text = input(">Enter the expression: ")
    if 'x' in text:
        x = float(input(">Enter the value of x: "))
        text = text.replace('x', str(x))
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
    except Exception as e:
        print(e)