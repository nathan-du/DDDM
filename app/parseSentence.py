import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re

def parseSentence(sentence):
	# Set up filter to find input words
	# 0: query at database
	# 1: compare result
	filter_words = {'Trump' : ['NAME', 1], 'Ford' : ['NAME',1], 'votes' : ['POPULAR_VOTE', 0], 'year': ['YEAR', 0]}

	# Regular expression	
	regexp = re.compile('\d+')
	m = regexp.search(sentence)
	number_string = m.group()
	number = int(number_string)

	# Read Database csv file
	df = pd.read_csv('./presidentialelections.csv')
	
	# Tokenize input sentence
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence)

	# Filter input words
	query_result = []
	for word in sentence_tokens:
		if word in filter_words.keys():
			result = filter_words[word]
			result_combined = [word, result[0], result[1]]
			query_result.append(result_combined)
	
	row = None
	pos = 0
	# Compare result with our data
	for element in query_result:
		pos += 1
		if element[2] == 1:
			val = element[0]
			col = element[1] 
			row = df[df[col].str.contains(val)]
			break
		elif element[2] == 0:
			val = number
			col = element[1]	
	
	val = int(row[query_result[pos][1]])
	if number > int(0.98 * val) and number < int(1.02*val):
		return True
	else:
		return False
