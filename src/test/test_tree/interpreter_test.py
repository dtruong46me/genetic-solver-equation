import unittest
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
path = os.path.abspath(os.path.join(path, ".."))

sys.path.insert(0, path)

from input_handling.parser_tree.nodes import *
from input_handling.parser_tree.interpreter import Interpreter
from input_handling.parser_tree.values import Number

class TestInterpreter(unittest.TestCase):

	def test_numbers(self):
		value = Interpreter().visit(NumberNode(51.2))
		self.assertEqual(value, Number(51.2))

	def test_single_operations(self):
		result = Interpreter().visit(AddNode(NumberNode(27), NumberNode(14)))
		self.assertEqual(result.value, 41)

		result = Interpreter().visit(SubtractNode(NumberNode(27), NumberNode(14)))
		self.assertEqual(result.value, 13)

		result = Interpreter().visit(MultiplyNode(NumberNode(27), NumberNode(14)))
		self.assertEqual(result.value, 378)

		result = Interpreter().visit(DivideNode(NumberNode(27), NumberNode(14)))
		self.assertAlmostEqual(result.value, 1.92857, 5)

		with self.assertRaises(Exception):
			Interpreter().visit(DivideNode(NumberNode(27), NumberNode(0)))
			
	def test_full_expression(self):
		tree = AddNode(
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
		)

		result = Interpreter().visit(tree)
		self.assertAlmostEqual(result.value, -2360.08, 2)
