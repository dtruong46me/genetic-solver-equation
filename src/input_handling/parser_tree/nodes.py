from dataclasses import dataclass
from typing import Any
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

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
class SqrtNode:
	node: any

	def __repr__(self):
		return f"sqrt({self.node})"
	
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
class PiNode:
	node: any

	def __repr__(self):
		return f"{self.node}"

@dataclass
class CommaNode:
	node_a: any
	node_b: any

	def __reduce__(self):
		return f"{self.node_a}, {self.node_b}"

@dataclass
class LogNode:
	node: any
	def __repr__(self):
		return f"log({self.node})"

@dataclass
class FactNode:
	node: any
	def __repr__(self):
		return f"factorial({self.node})"

@dataclass
class LnNode:
	node: any

	def __repr__(self):
		return f"ln({self.node})"

@dataclass
class ArcSinNode:
	node: any

	def __repr__(self):
		return f"Arcsin({self.node})"
	
@dataclass
class ArcCosNode:
	node: any

	def __repr__(self):
		return f"Arccos({self.node})"
	
@dataclass
class ArcTanNode:
	node: any

	def __repr__(self):
		return f"Arctan({self.node})"
	
@dataclass
class ArcCotNode:
	node: any

	def __repr__(self):
		return f"Arccot({self.node})"
	
@dataclass
class NrootNode:
	node: any

	def __repr__(self):
		return f"Nroot({self.node})"