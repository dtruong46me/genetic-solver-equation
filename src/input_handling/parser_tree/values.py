from dataclasses import dataclass
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)


@dataclass
class Number:
	value: any
	
	def __repr__(self):
		return f"{self.value}"

@dataclass
class List_:
	value1: any
	value2: any
	def __repr__(self) -> str:
		return f"[{self.value1},{self.value2}]"