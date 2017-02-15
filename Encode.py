#urlEncode method encodes input following url encode rules for characters
#	url is the string you would like to encode
#	apiURL is an optional parameter for a string of the url of a web api, if you want to use one
#	paramNames is an optional list parameter containing the names of the parameters you want to encode
#	paramData is an optional list parameter containing the values for the parameters you want to encode
#		NOTE: indexes of paramNames values and paramData values should match up
def urlEncode(url,apiURL=None,paramNames=None,paramData=None):
	#Establish an initial null output
	output = ''

	#Encode the input url, and then add the expected url parameter before it
	url = _urlCharShift(url)
	url = 'url='+url

	#Logic for parameters
	#	if there are parameters to encode and an apiURL
	if not paramNames == None and not paramData == None and not apiURL == None:
		#start the output with the apiURL, since that doesn't need encoding, and add a ?
		output += apiURL
		output += '?'

		#find length of the paramNames list for iteration
		length = len(paramNames)

		#iterate through the paramNames list and paramData list, encoding paramData values
		for index in range(length):
			paramData[index] = _urlCharShift(paramData[index])
			#choose seperate character encoding sequences if it's the first value or not
			if index < 1:
				output += paramNames[index] + '=' + paramData[index]
			else:
				output += '&' + paramNames[index] + '=' + paramData[index]

		#add & character to end of string, then add the encoded url value, and return output
		output += '&'
		output += url
		return output

	#	if there are not parameters, but there is an apiURL
	elif paramNames == None and not apiURL == None:
		output += apiURL
		output += '?'
		output += url
		return output

	# if there isn't an apiURL but there is paramNames and paramData
	elif apiURL == None and not paramNames == None and not paramData == None:
		#follow steps of first if statement, but skip encoding the apiURL
		length = len(paramNames)
		for index in range(length):
			paramData[index] = _urlCharShift(paramData[index])
			if index < 1:
				output += paramNames[index] + '=' + paramData[index]
			else:
				output += '&' + paramNames[index] + '=' + paramData[index]
		output += url
		return output

	#	if there is just a url
	elif apiURL == None and paramNames == None and paramData == None:
		output += url
		return output
	
	# if there is not a url, but there is all of the other things
	elif url == None and not (apiURL == None and paramNames == None and paramData == None):
		output += apiURL
		output += '?'
		length = len(paramNames)
		for index in range(length):
			paramData[index] = paramData[index].replace(' ','+')
			if index < 1:
				output += paramNames[index] + '=' + paramData[index]
			else:
				output += '&' + paramNames[index] + '=' + paramData[index]
		return output

	#	Handle edge cases
	else:
		print('\n\nAn error occured. Please check your input parameters.')
		return output
	#End logic for parameters

def htmlEncode(text):
	text = str(text)
	text.replace('&','&amp;')
	text.replace('\"','&quot;')
	text.replace('\'','&apos;')
	text.replace('<','&lt;')
	text.replace('>','&gt;')
	text.replace('~','&tilde;')
	return text

#internal method containing character rules for url encoding
def _urlCharShift(text):
	url = str(text)
	url.replace('%','%25')
	url.replace('!','%21')
	url.replace('#','%23')
	url.replace('$','%24')
	url.replace('&','%26')
	url.replace('\'','%27')
	url.replace('(','%28')
	url.replace(')','%29')
	url.replace('*','%2A')
	url.replace('+','%2B')
	url.replace(',','%2C')
	url.replace('/','%2F')
	url.replace(':','%3A')
	url.replace(';','%3B')
	url.replace('=','%3D')
	url.replace('?','%3F')
	url.replace('@','%40')
	url.replace('[','%5B')
	url.replace(']','%5D')
	return url
