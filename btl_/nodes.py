from dataclasses import dataclass

@dataclass
class NumberNode:
	value: any

	def __repr__(self):
		return f"{self.value}"

@dataclass
class AddNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}+{self.node_b})"

@dataclass
class SubtractNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}/{self.node_b})"
	
@dataclass
class PowerNode:
	node_a: any
	node_b: any

	def __repr__(self):
		return f"({self.node_a}^{self.node_b})"
	
@dataclass
class PlusNode:
	node: any

	def __repr__(self):
		return f"(+{self.node})"
	
@dataclass
class MinusNode:
	node: any

	def __repr__(self):
		return f"(-{self.node})"

@dataclass
class FuncNode:
	node: any

	def __repr__(self):
		return f"({self.node})"
	
@dataclass
class AbsoluteValueNode:
	node: any

	def __repr__(self):
		return f"abs({self.node})"
	
@dataclass
class SinNode:
	node: any

	def __repr__(self):
		return f"sin({self.node})"

@dataclass
class CosNode:
	node: any

	def __repr__(self):
		return f"cos({self.node})"

@dataclass
class TanNode:
	node: any

	def __repr__(self):
		return f"tan({self.node})"
	
@dataclass
class CotNode:
	node: any

	def __repr__(self):
		return f"cot({self.node})"
@dataclass
class ExpNode:
	node: any

	def __repr__(self):
		return f"exp({self.node})"

@dataclass
class EConstNode:
	node: any

	def __repr__(self):
		return f"{self.node}"
	
@dataclass
class LogNode:
	node_a: any
	node_b: any
	
	def __repr__(self):
		return f"log({self.node_a}, {self.node_b})"

@dataclass
class LnNode:
	node: any

	def __repr__(self) -> str:
		return f"ln({self.node})"