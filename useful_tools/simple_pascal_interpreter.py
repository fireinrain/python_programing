# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis

INTEGER,PLUS,EOF = 'INTEGER','PLUS','EOF'

class Token(object):
	"""docstring for Token"""
	def __init__(self, type,value):
		#token type:INTEGER,PLUS,EOF
		self.type = type
		#token value:0,1,2,3,4,5,6,7,8,9,'+' or None
		self.value = value

	def __str__(self):
		return 'Token({type},{value})'.format(
				type=self.type,
				value=repr(self.value)

			)

	def __repr__(self):
		return self.__str__()


class Interpreter(object):
	"""docstring for Interpreter"""
	def __init__(self, text):
		#client string input such as:'3+5'
		self.text = text
		self.pos = 0
		self.current_token = None

	def error(self):
		raise Exception('Error parsing input')

	def get_next_token(self):
		text = self.text

		if self.pos>len(text)-1:
			return Token(EOF,None)

		current_char = text[self.pos]

		if current_char.isdigit():
			token = Token(INTEGER,int(current_char))
			self.pos += 1
			return token
		
		# if current_char.isdigit() and text[self.pos].isdigit():
		# 	multi_char = current_char+text[self.pos]
		# 	token = Token(INTEGER,int(multi_char))
		# 	self.pos += 1
		# 	return token

		if current_char == '+':
			token = Token(PLUS,current_char)
			self.pos += 1
			return token
			
	def eat(self,token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()
	
	def expr(self):
		self.current_token = self.get_next_token()

		left = self.current_token
		self.eat(INTEGER)

		op = self.current_token
		self.eat(PLUS)

		right = self.current_token
		self.eat(INTEGER)

		result = left.value + right.value
		return result

def main():
	while True:
		try:
			text = input('calc> ')
		except EOFError:
			break
		if not text:
			continue
		interpreter = Interpreter(text)
		result =interpreter.expr()
		print(result)

if __name__ == '__main__':
	# main()
	
	

		
		