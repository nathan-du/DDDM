import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from querydb import querydb
from dictionaries import getCountries

def parseSentence(sentence):
  	# Parse year
	regexp_year = re.compile('(in|year)\s(\d{4})')
	m = regexp_year.search(sentence)
	if m is not None:
		year_string = m.group()
		w = year_string.split(' ')
		year = int(w[1])
		# Replace it with empty string
		sentence = regexp_year.sub('', sentence)
  
	regexp_immigrants = re.compile('\d+\s*(people|immigrants|new)')
	m = regexp_immigrants.search(sentence)
	if m is not None:
		immigrants_string = m.group()
		w = immigrants_string.split(' ')
		immigrants = int(w[0])
		# Replace it with empty string
		sentence = regexp_immigrants.sub('', sentence)

	# Tokenize input sentence
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence)
	stop = set(stopwords.words('english'))
	tokens_selected = [x for x in sentence_tokens if x.lower() not in stop]
	
	print(tokens_selected)
	countries = getCountries(tokens_selected)
	print(countries)	
	if len(countries) > 0:
		rows = []
		for country in countries:
			row = querydb("SELECT * FROM immigrationpercountry WHERE LOWER(Country)= "+country)
			rows.extend(row)
		print(rows)
