'''
This class is meant to be used in `Add To Instapaper.py`

This class provides methods to read in authorization information from an external file which should be
	.gitignored in order to not show up in public git repos. This is by no means meant to be a secure
	storage method, but it's a way to privately store your auth codes while still using a public repo
'''
class AuthCodes:
	# upon object creation, auth-codes.txt is read into object
	def __init__(self):
		try:
			with open('auth-codes.txt','r') as authfile:
				self.username=authfile.readline()
				self.password=authfile.readline()
			authfile.close
		# If import fails, establish data from user input
		except:
			print('An error occured opening the required authorization file')
			self.username = input('What is your username/email?')
			self.password = input('What is your password?')

	# Internal method for removing the descriptor text before the actual code
	def _stripID(self,text):
		equals = False
		code = ''
		for index in range(len(text)):
			if text[index] == '=' and not equals == True:
				equals = True
			elif equals == True and not text[index] == '=':
				code += text[index]
		return code.rstrip()
	
	def _stripCode(self,text):
		equals = False
		name = ''
		for index in range(len(text)):
			if not text[index] == '=' and not equals == True:
				name += text[index]
			elif text[index] == '=' and not equals == True:
				equals = True
			elif not text[index] == '=' and equals == True:
				break
		return name

	# If you want to use one method and parse theh values on your own, you can use this method
	def authlist(self):
		return [self._stripID(self.username), self._stripID(self.password)]
	def codelist(self):
		return [self._stripCode(self.username), self._stripCode(self.password)]
	def username(self):
		return str(self._stripID(self.username))
	def password(self):
		return str(self._stripID(self.password))