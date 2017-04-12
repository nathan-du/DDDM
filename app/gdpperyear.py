import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re

def parseSentence(sentence):

	# Regular expression	
	regexp_integers = re.compile('\d+')
	m = regexp.search(sentence)
	number_string = m.group()
	number = int(number_string)

	regexp_year = re.compile('')
	m = regexp.search(sentence)
	year_string = m.group()
	w = year_string.split(' ')
	year = int(w[1])
	# Replace it with empty string
	sentence_new = regexp_year.sub('', sentence)


	# Read Database csv file
	df = pd.read_csv('./gdpperyear.csv')
	
	# Tokenize input sentence
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence_new)

	row = df[df[col].str.contains(val)]
	
	val = int(row[query_result[pos][1]])
	if number > int(0.98 * val) and number < int(1.02*val):
		return True
	else:
		return False
