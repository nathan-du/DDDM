import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from querydb import querydb
from dictionaries import getCountries

def parseSentence(sentence):
	sentence = sentence.lower()

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

	regexp_percent = re.compile('(\d+|\d*.\d+)\s*(%|percent)')
	m = regexp_percent.search(sentence)
	percent = None
	if m is not None:
		percent = float(m.group(1))
		sentence = regexp_percent.sub('', sentence)
  
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
	
	if len(countries) > 0 and percent is None:
		rows = []
		for country in countries:
			row = querydb("SELECT * FROM immigrationpercountry WHERE LOWER(country) LIKE '%"+country+"%'")
			rows.extend(row)
		if year is not None and immigrants is not None:
			if year < 2003 or year > 2015:
				return {"truth":None, "reason":"No data for year " + str(year)}
			else:
				for r in rows:
					immigrants_actual = r[(year%2000)-1]
					if immigrants_actual is None:
						continue
					immigrants_actual = float(immigrants_actual)
					if less_result:
						return {"truth":immigrants_actual < immigrants, "reason":wordify([r])}
					elif greater_result:
						return {"truth":immigrants_actual > immigrants, "reason":wordify([r])}
					else:
						return {"truth":immigrants > immigrants_actual*0.98 and immigrants < immigrants_actual*1.02, "reason":wordify([r])}
				return {"truth":False, "reason":wordify(rows)}
		elif immigrants is not None and percent is None:
			for r in rows:
				r_copy = list(r)
				del r_copy[:2]
				for val in r_copy:
					if less_result and val < immigrants:
						return {"truth":True, "reason":wordify([r])}
					elif greater_result and val > immigrants:
						return {"truth":True, "reason":wordify([r])}
					elif immigrants > float(val)*0.98 and immigrants < float(val)*1.02:
						return {"truth":True, "reason":wordify([r])}
				total_immigrants = sum(r_copy)
				if less_result and total_immigrants < immigrants:
					return {"truth":True, "reason":wordify([r])}
				elif greater_result and total_immigrants > immigrants:
					return {"truth":True, "reason":wordify([r])}
				elif immigrants > total_immigrants*0.98 and immigrants < total_immigrants*1.02:
					return {"truth":True, "reason":wordify([r])}
			return {"truth":False, "reason":wordify(rows)}
	elif len(countries) > 0 and percent is not None:
		rows = querydb("SELECT * FROM immigrationpercountry")
		if year is not None:
			if year < 2003 or year > 2015:
				return {"truth":None, "reason":"No data for year " + str(year)}
			else:
				total_immigration_year = 0
				country_rows = []
				for row in rows:
					if row[(year%2000)-1] is None:
						continue
					if row[1].lower() in countries:
						country_rows.append(row)
					total_immigration_year += row[(year%2000)-1]
				for country in country_rows:
					actual_percent = 100*float(country[(year%2000)-1])/float(total_immigration_year)
					if less_result and actual_percent < percent:
						return {"truth":True, "reason":wordify([country])}
					if greater_result and actual_percent > percent:
						return {"truth":True, "reason":wordify([country])}
					if 0.98*actual_percent <= percent <= 1.02*actual_percent:
						return {"truth":True, "reason":wordify([country])}
				return {"truth":False, "reason":wordify(country_rows)}
		else:
			for y in range(2003,2016):
				total_immigration_year = 0
				country_rows = []
				for row in rows:
					if row[(y%2000)-1] is None:
						continue
					if row[1].lower() in countries:
						country_rows.append(row)
					total_immigration_year += row[(y%2000)-1]
				for country in country_rows:
					actual_percent = 100*float(country[(y%2000)-1])/float(total_immigration_year)
					if less_result and actual_percent < percent:
						return {"truth":True, "reason":wordify([country])}
					if greater_result and actual_percent > percent:
						return {"truth":True, "reason":wordify([country])}
					if 0.98*actual_percent <= percent <= 1.02*actual_percent:
						return {"truth":True, "reason":wordify([country])}
			return {"truth":False, "reason":wordify(country_rows)}
	elif len(countries) == 0 and percent is None:
		rows = querydb("SELECT * FROM immigrationpercountry")
		if year is not None and immigrants is not None:
			if year < 2003 or year > 2015:
				return {"truth":None, "reason": "No data for year " + str(year)}
			total_year = 0
			for row in rows:
				immigrants_actual = row[(year%2000)-1]
				if immigrants_actual is None:
					continue
				immigrants_actual = float(immigrants_actual)
				if less_result and immigrants_actual < immigrants:
					return {"truth":True, "reason":wordify([row])}
				if greater_result and immigrants_actual > immigrants:
					return {"truth":True, "reason":wordify([row])}
				if immigrants_actual*0.98 <= immigrants <= 1.02*immigrants_actual:
					return {"truth":True, "reason":wordify([row])}
				total_year += immigrants_actual
			if less_result and total_year < immigrants:
				return {"truth":True, "reason":wordify(rows)}
			if greater_result and total_year > immigrants:
				return {"truth":True, "reason":wordify(rows)}
			return {"truth":immigrants > total_year*0.98 and immigrants < total_year*1.02, "reason":wordify(rows)}

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
						return {"truth":True, "reason":wordify([row])}
					if greater_result and val > immigrants:
						return {"truth":True, "reason":wordify([row])}
					if val*0.98 <= immigrants <= val*1.02:
						return {"truth":True, "reason":wordify([row])}
					total_country += val
				if less_result and total_country < immigrants:
					return {"truth":True, "reason":wordify([row])}
				if greater_result and total_country > immigrants:
					return {"truth":True, "reason":wordify([row])}
				if total_country*0.98 <= immigrants <= total_country*1.02:
					return {"truth":True, "reason":wordify([row])}
				total_immigrants += total_country
			if less_result and total_immigrants < immigrants:
				return {"truth":True, "reason":wordify(rows)}
			if greater_result and total_immigrants > immigrants:
				return {"truth":True, "reason":wordify(rows)}
			return {"truth":total_immigrants*0.98 <= immigrants <= 1.02*total_immigrants, "reason":wordify(rows)}

def wordify(rows):
	explanaition = ""
	for row in rows:
		explanaition += "The immigration for " + row[1]
		for year in range(2003,2016):
			explanaition += " in " + str(year) + " was " + str(row[(year%2000)-1]) 
		explanaition += ".\n"
	return explanaition
