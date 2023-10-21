import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

from input_handling.core.lexer import Lexer
from input_handling.core.parser_ import Parser
from input_handling.core.interpreter import Interpreter

while True:
	try:
		text = input("calc > ")
		lexer = Lexer(text)
		tokens = lexer.generate_tokens()
		test_tokens = list(tokens)
		print(test_tokens)
		
		# parser = Parser(tokens)
		# tree = parser.parse()
		# print(tree)
		# if not tree: continue
		# interpreter = Interpreter()
		# value = interpreter.visit(tree)
		# print(value)
	except Exception as e:
		print(e)

