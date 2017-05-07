from nltk.tokenize import RegexpTokenizer
import presidentialelections as pe
import unemploymentrate as ur
import immigrationpercountry as ipc
import gdpperyear as gdp
from dictionaries import getData

def findTable(sentence):

	# Word lists for deciding which table to look at
	elections_words = ['president', 'election', 'elections', 'vote', 'votes', 'popular', 'electoral']
	presidents = getData('presidents')
	for pres in presidents:
		elements = pres.split(' ')
		for elem in elements:
			elections_words.append(elem.lower())
	unemployment_words = ['unemployment', 'unemployed', 'out-of-work', 'jobless', 'out of work']
	countries = getData('countries')
	immigration_words = ['immigration', 'immigrant', 'immigrated', 'immigrants']
	immigration_words += countries
	gdp_words = ['gdp', 'gross', 'domestic', 'product', 'economy']

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
	if max(table_finder) == 0:
		return {'truth': None, 'reason': "No data matching your input"}
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
