from dataclasses import dataclass

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