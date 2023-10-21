from enum import Enum
from dataclasses import dataclass
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

class TokenType(Enum):
	NUMBER    = 0
	PLUS      = 1
	MINUS     = 2
	MULTIPLY  = 3
	DIVIDE    = 4
	POWER     = 5
	LPAREN    = 6
	RPAREN    = 7
	VARIABLE  = 8
	FUNC      = 9
	ABS 	  = 10
	SIN 	  = 11
	COS       = 12
	TAN       = 13
	COT       = 14
	LOG       = 15
	LN        = 16
	EXP       = 17
	E_CONST   = 18
	PI        = 19
	COMMA     = 20
	SQRT      = 21
	FACT      = 22
	ARCSIN    = 23
	ARCCOS    = 24
	ARCTAN    = 25
	ARCCOT    = 26
	NROOT     = 27
	
@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")
