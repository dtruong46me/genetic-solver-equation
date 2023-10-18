from tokens import TokenType
from nodes import *

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self):
		raise Exception("Invalid syntax")
	
	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	def parse(self):
		if self.current_token == None:
			return None

		result = self.expr()

		if self.current_token != None:
			self.raise_error()

		return result

	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
			if self.current_token.type == TokenType.PLUS:
				self.advance()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.MINUS:
				self.advance()
				result = SubtractNode(result, self.term())
			#===============================================#
			# elif self.current_token.type == TokenType.FUNC:
			# 	self.advance()
			# 	result = FuncNode(result)
			#===============================================#
		return result

	def term(self):
		result = self.powered()

		while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
			if self.current_token.type == TokenType.MULTIPLY:
				self.advance()
				result = MultiplyNode(result, self.powered())
			elif self.current_token.type == TokenType.DIVIDE:
				self.advance()
				result = DivideNode(result, self.powered())
			#=================================================#
			# elif self.current_token.type == TokenType.FUNC:
			# 	self.advance()
			# 	result = FuncNode(result)
			#=================================================#
		return result

	def powered(self):
		result = self.loga()

		while self.current_token != None and self.current_token.type == TokenType.POWER:

			self.advance()
			result = PowerNode(result, self.loga())
		
		return result

	#===================================#
	#Testing code#
	def loga(self):
		result = self.factor()

		while self.current_token != None and self.current_token.type == TokenType.LOG:
			self.advance()
			result = LogNode(result, self.factor())
		return result
	#End of testing#
	#===================================#


	def factor(self):
		token = self.current_token

		if token.type == TokenType.LPAREN:
			self.advance()
			result = self.expr()

			if self.current_token.type != TokenType.RPAREN:
				self.raise_error()
			
			self.advance()
			return result

		elif token.type == TokenType.NUMBER:
			self.advance()
			return NumberNode(token.value)

		elif token.type == TokenType.E_CONST:
			self.advance()
			return EConstNode(token.value)
		
		elif token.type == TokenType.PLUS:
			self.advance()
			return PlusNode(self.factor())
		
		elif token.type == TokenType.MINUS:
			self.advance()
			return MinusNode(self.factor())

		elif token.type == TokenType.ABS:
			self.advance()
			return AbsoluteValueNode(self.factor())
		
		elif token.type == TokenType.SIN:
			self.advance()
			return SinNode(self.factor())
	
		elif token.type == TokenType.COS:
			self.advance()
			return CosNode(self.factor())
		
		elif token.type == TokenType.TAN:
			self.advance()
			return TanNode(self.factor())
		
		elif token.type == TokenType.COT:
			self.advance()
			return CotNode(self.factor())
		
		elif token.type == TokenType.EXP:
			self.advance()
			return ExpNode(self.factor())
		
		elif token.type == TokenType.LN:
			self.advance()
			return LnNode(self.factor())
		# elif token.type == TokenType.LOG:
		# 	self.advance()
		# 	return LogNode(token, self.factor())

		# elif token.type == TokenType.ABS:
		# 	self.advance()
		# 	if token.type == TokenType.LPAREN:
		# 		self.advance()
		# 		result = self.expr()

		# 		if self.current_token.type != TokenType.RPAREN:
		# 			self.raise_error()
		# 		self.advance()
		# 		return AbsoluteValueNode(result)
		# 	else:
		# 		self.raise_error()

		
		self.raise_error()

"""sin(x+ 5 - (cos(5 * 7^3)))"""