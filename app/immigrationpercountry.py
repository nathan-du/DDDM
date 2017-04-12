import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re

def parseSentence(sentence):
	# Read Database csv file
	df = pd.read_csv('./immigrationpercountry.csv')
	
	# Set up filter to find input words
	filter_words = list(df['Country'])


	# Regular expression	
	regexp_integers = re.compile('\d+')
	m = regexp.search(sentence)
	number_string = m.group()
	number = int(number_string)

	regexp_year = re.compile('(year)*\s*(in)*\s*(\d{4})')
	m = regexp.search(sentence)
	year_string = m.group()
	w = year_string.split(' ')
	year = int(w[1])
	# Replace it with empty string
	sentence_new = regexp_year.sub('', sentence)


	# Tokenize input sentence
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence_new)

	# Filter input words
	query_result = []
	for word in sentence_tokens:
		if word in filter_words:
			country = word
	
	row = df[df['Country'].str.contains(country)]
	
	val = int(row[year])
	if number > int(0.98 * val) and number < int(1.02*val):
		return True
	else:
		return False
