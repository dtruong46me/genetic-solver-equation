from enum import Enum
from dataclasses import dataclass

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
	COMMA     = 19
	SQRT      = 20
	
@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value != None else "")
