from nltk.tokenize import RegexpTokenizer
import presidentialelections as pe
import unemploymentrate as ur
import immigrationpercountry as ipc
import gdpperyear as gdp

def findTable(sentence):

	# Word lists for deciding which table to look at
	elections_words = ['trump', 'hillary', 'president', 'election', 'vote']
	unemployment_words = ['unemployment', 'unemployed', 'out-of-work']
	immigration_words = ['mexico', 'immigration', 'immigrant', 'immigrants']
	gdp_words = ['gdp', 'gross', 'domestic', 'product']

	# Tokenize input sentence into words
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence.lower())

	# Initialize table frequencies
	table_finder = [0, 0, 0, 0]
	for word in sentence_tokens:
		if word in elections_words:
			table_finder[0] += 1
		if word in unemployment_words:
			table_finder[1] += 1
		if word in immigration_words:
			table_finder[2] += 1
		if word in gdp_words:
			table_finder[3] += 1


	# Majority vote to find best matching table
	pos = table_finder.index(max(table_finder))

	if pos == 0:
		return pe.parseSentence(sentence.lower())
	if pos == 1:
		return ur.parseSentence(sentence.lower())
	if pos == 2:
		return ipc.parseSentence(sentence.lower())
	if pos == 3:
		return gdp.parseSentence(sentence.lower())

	return None
