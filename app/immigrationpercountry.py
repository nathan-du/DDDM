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
	year = None
	if m is not None:
		year_string = m.group()
		w = year_string.split(' ')
		year = int(w[1])
		# Replace it with empty string
		sentence = regexp_year.sub('', sentence)
  
	regexp_immigrants = re.compile('\d+')
	m = regexp_immigrants.search(sentence)
	immigrants = None
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
	
	countries = getCountries(tokens_selected)

	greater = ['greater', 'more', 'at least']
	less = ['less', 'no more', 'at most']

	less_list = list(map(lambda x: x in sentence.lower(), less))
	less_result = True in less_list
	greater_list = list(map(lambda x: x in sentence.lower(), greater))
	greater_result = True in greater_list
	
	if len(countries) > 0:
		rows = []
		for country in countries:
			row = querydb("SELECT * FROM immigrationpercountry WHERE LOWER(country) LIKE '%"+country+"%'")
			rows.extend(row)
		if year is not None and immigrants is not None:
			if year < 2003 or year > 2015:
				return None
			else:
				for r in rows:
					immigrants_actual = r[(year%2000)-1]
					if immigrants_actual is None:
						continue
					immigrants_actual = float(immigrants_actual)
					if less_result:
						return immigrants_actual < immigrants
					elif greater_result:
						return immigrants_actual > immigrants
					else:
						return  immigrants > immigrants_actual*0.98 and immigrants < immigrants_actual*1.02
				return False
		elif immigrants is not None:
			for r in rows:
				r_copy = list(r)
				del r_copy[:2]
				for val in r_copy:
					if less_result and val < immigrants:
						return True
					elif greater_result and val > immigrants:
						return True
					elif immigrants > float(val)*0.98 and immigrants < float(val)*1.02:
						return True
				total_immigrants = sum(r_copy)
				if less_result and total_immigrants < immigrants:
					return True
				elif greater_result and total_immigrants > immigrants:
					return True
				elif immigrants > total_immigrants*0.98 and immigrants < total_immigrants*1.02:
					return True
				else:
					return False
	else:
		rows = querydb("SELECT * FROM immigrationpercountry")
		if year is not None and immigrants is not None:
			if year < 2003 or year > 2015:
				return None
			total_year = 0
			for row in rows:
				immigrants_actual = row[(year%2000)-1]
				if immigrants_actual is None:
					continue
				immigrants_actual = float(immigrants_actual)
				if less_result and immigrants_actual < immigrants:
					return True
				if greater_result and immigrants_actual > immigrants:
					return True
				if immigrants_actual*0.98 <= immigrants <= 1.02*immigrants_actual:
					return True
				total_year += immigrants_actual
			if less_result and total_year < immigrants:
				return True
			if greater_result and total_year > immigrants:
				return True
			return immigrants > total_year*0.98 and immigrants < total_year*1.02

		if immigrants is not None:
			total_immigrants = 0
			for row in rows:
				total_country = 0
				row_copy = list(row)
				del row_copy[:2]
				for val in row_copy:
					if val is None:
						continue
					if less_result and val < immigrants:
						return True
					if greater_result and val > immigrants:
						return True
					if val*0.98 <= immigrants <= val*1.02:
						return True
					total_country += val
				if less_result and total_country < immigrants:
					return True
				if greater_result and total_country > immigrants:
					return True
				if total_country*0.98 <= immigrants <= total_country*1.02:
					return True
				total_immigrants += total_country
			if less_result and total_immigrants < immigrants:
				return True
			if greater_result and total_immigrants > immigrants:
				return True
			return total_immigrants*0.98 <= immigrants <= 1.02*total_immigrants 
