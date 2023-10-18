from tokens import Token, TokenType
import string

WHITESPACE = ' \n\t,'
DIGITS = '0123456789'
LETTER = string.ascii_letters
FUNCTIONS = ["sin", "cos", "tan" , "cot", "exp", "log", "abs", "exp"]
CONSTANTS = ['e', 'pi']

class Lexer:
	def __init__(self, text):
		self.text = iter(text)
		self.advance()

	def advance(self):
		try:
			self.current_char = next(self.text)
		except StopIteration:
			self.current_char = None

	def generate_tokens(self):
		while self.current_char != None:
			if self.current_char in WHITESPACE:
				self.advance()
			elif self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number()
			elif self.current_char in LETTER:
				yield self.generate_function()
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '^':
				self.advance()
				yield Token(TokenType.POWER)
			elif self.current_char == '(':
				self.advance()
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				self.advance()
				yield Token(TokenType.RPAREN)
			else:
				raise Exception(f"Illegal character '{self.current_char}'")

	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()

		while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.':
				decimal_point_count += 1
				if decimal_point_count > 1:
					break
			
			number_str += self.current_char
			self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'

		return Token(TokenType.NUMBER, float(number_str))		
	
	def generate_function(self):
		func_str = self.current_char
		self.advance()
		while self.current_char != None and self.current_char in LETTER:
			func_str += self.current_char
			self.advance()
		if func_str == 'sin':
			return Token(TokenType.SIN, str(func_str))
		elif func_str == 'cos':
			return Token(TokenType.COS, str(func_str))
		elif func_str == 'tan':
			return Token(TokenType.TAN, str(func_str))
		elif func_str == 'cot':
			return Token(TokenType.COT, str(func_str))
		elif func_str == 'log':
			return Token(TokenType.LOG, str(func_str))
		elif func_str == 'ln':
			return Token(TokenType.LN, str(func_str))
		elif func_str == 'abs':
			return Token(TokenType.ABS, str(func_str))
		elif func_str == 'exp':
			return Token(TokenType.EXP, str(func_str))
		elif func_str == "e":
			return Token(TokenType.E_CONST, str(func_str))
		# token_type = TokenType.FUNC if func_str in FUNCTIONS else TokenType.VARIABLE
		else:
			return Token(TokenType.VARIABLE, str(func_str))
		