import unittest
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
path = os.path.abspath(os.path.join(path, ".."))
sys.path.insert(0, path)

from input_handling.parser_tree.tokens import Token, TokenType
from input_handling.parser_tree.parser_ import Parser
from input_handling.parser_tree.nodes import *

class TestParser(unittest.TestCase):

	def test_empty(self):
		tokens = []
		node = Parser(tokens).parse()
		self.assertEqual(node, None)

	def test_numbers(self):
		tokens = [Token(TokenType.NUMBER, 51.2)]
		node = Parser(tokens).parse()
		self.assertEqual(node, NumberNode(51.2))

	def test_single_operations(self):
		tokens = [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.PLUS),
			Token(TokenType.NUMBER, 14),
		]

		node = Parser(tokens).parse()
		self.assertEqual(node, AddNode(NumberNode(27), NumberNode(14)))
		
		tokens = [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.MINUS),
			Token(TokenType.NUMBER, 14),
		]

		node = Parser(tokens).parse()
		self.assertEqual(node, SubtractNode(NumberNode(27), NumberNode(14)))
			
		tokens = [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.MULTIPLY),
			Token(TokenType.NUMBER, 14),
		]

		node = Parser(tokens).parse()
		self.assertEqual(node, MultiplyNode(NumberNode(27), NumberNode(14)))
			
		tokens = [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.DIVIDE),
			Token(TokenType.NUMBER, 14),
		]

		node = Parser(tokens).parse()
		self.assertEqual(node, DivideNode(NumberNode(27), NumberNode(14)))

	def test_full_expression(self):
		tokens = [
			Token(TokenType.NUMBER, 27),
			Token(TokenType.PLUS),
			Token(TokenType.LPAREN),
			Token(TokenType.NUMBER, 43),
			Token(TokenType.DIVIDE),
			Token(TokenType.NUMBER, 36),
			Token(TokenType.MINUS),
			Token(TokenType.NUMBER, 48),
			Token(TokenType.RPAREN),
			Token(TokenType.MULTIPLY),
			Token(TokenType.NUMBER, 51),
		]

		node = Parser(tokens).parse()
		self.assertEqual(node, AddNode(
			NumberNode(27),
			MultiplyNode(
				SubtractNode(
					DivideNode(
						NumberNode(43),
						NumberNode(36)
					),
					NumberNode(48)
				),
				NumberNode(51)
			)
		))
