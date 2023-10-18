from nodes import *
from values import Number
import math

CONST = {"e": math.e}
class Interpreter:
	def __init__(self):
		pass

	def visit(self, node):
		method_name = f'visit_{type(node).__name__}'
		method = getattr(self, method_name)
		return method(node)
		
	def visit_NumberNode(self, node):
		return Number(node.value)
	
	def visit_EConstNode(self,node):
		return Number(math.e)
	
	def visit_AddNode(self, node):
		return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

	def visit_SubtractNode(self, node):
		return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

	def visit_MultiplyNode(self, node):
		return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

	def visit_DivideNode(self, node):
		try:
			return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
		except:
			raise Exception("Runtime math error")
		
	def visit_PlusNode(self, node):
		return self.visit(node.node)
	
	def visit_MinusNode(self, node):
		return Number(-self.visit(node.node).value)

	def visit_PowerNode(self, node):
		base = self.visit(node.node_a).value
		pow = self.visit(node.node_b).value
		if int(pow) - pow != 0:
			if int(1/pow) - 1/pow == 0:
				if (1/pow) % 2 != 0:
					if base < 0:
						return Number(-((-base)**pow))
					else:
						return Number(base**pow)
				else:
					if base < 0:
						raise Exception("Runtime math error")
					else:
						return Number(base**pow)
						
			else:
				if base < 0:
					raise Exception("Runtime math error")
				else:
					return Number(base**pow)
		else:
			return Number(base ** pow)
		
	def visit_AbsoluteValueNode(self, node):
		check_num = self.visit(node.node).value

		if (check_num < 0):
			return Number(check_num*(-1))
		else:
			return Number(check_num)
		
	def visit_SinNode(self,node):
		val = self.visit(node.node).value
		return Number(math.sin(val))
	
	def visit_CosNode(self,node):
		val = self.visit(node.node).value
		return Number(math.sin((math.pi/2) - val))
	
	def visit_TanNode(self,node):
		val = self.visit(node.node).value
		return Number(math.tan(val))
	
	def visit_CotNode(self,node):
		val = self.visit(node.node).value
		return Number(1 / math.tan(val))
	
	def visit_ExpNode(self,node):
		val = self.visit(node.node).value
		return Number(math.exp(val))
	
	def visit_LnNode(self,node):
		val = self.visit(node.node).value
		return Number(math.log(val))

	def visit_LogNode(self,node):
		base = self.visit(node.node_a).value
		val = self.visit(node.node_b).value
		return Number(math.log(val) / math.log(base))
