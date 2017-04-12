import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re

def parseSentence(sentence):
	# Regular expression	
	regexp_percentages = re.compile('(\d*.)?\d+%')
	m = regexp_percentages.search(sentence)
	if m is not None:
		number_string = m.group()
		number = float(number_string.split('%')[0])

	regexp_year = re.compile('(in|year)\s(\d{4})')
	m = regexp_year.search(sentence)
	if m is not None:
		year_string = m.group()
		w = year_string.split(' ')
		print(w)
		year = int(w[1])
		# Replace it with empty string
		sentence_new = regexp_year.sub('', sentence)


	# Read Database csv file
	df = pd.read_csv('../data/unemploymentrate.csv')

	if year is not None:
		row = df[df['YEAR'] == year]
		unemployment = float(row['UNEMPLOYMENT_RATE'])
	else:
		row = df[df['UNEMPLOYMENT_RATE'] == number]
	

	if number > float(0.98 * unemployment) and number < float(1.02*unemployment):
		return True
	else:
		return False
