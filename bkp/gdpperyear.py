import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re
from querydb import querydb

def parseSentence(sentence):

	# Regular expression	
	regexp_integers = re.compile('\d+')
	m = regexp_integers.search(sentence)
	if m is not None:
		number_string = m.group()
		number = int(number_string)

	regexp_year = re.compile('(in|year)\s(\d{4})')
	n = regexp_year.search(sentence)
	if n is not None:
		year_string = n.group()
		w = year_string.split(' ')
		year = "null"
		if len(w) > 1:
			year = int(w[1])
		# Replace it with empty string
		sentence_new = regexp_year.sub('', sentence)

	regexp_gdp = re.compile('\$(\d*.)?\d+\s*([a-zA-Z]+)?')
	m = regexp_gdp.search(sentence)
	if m is not None:
		gdp_string = m.group()
		w = gdp_string.split(' ')
		
		# prevent this condition, no text followed by number. e.g.:"GDP is $5"
		order = "null"
		if len(w) > 1:
			order = w[1]
		gdp = float(w[0].split('$')[1])
		gdp = gdp*{"thousand":0.000001, "million":0.001, "billion":1.0, "trillion":1000}.get(order,0.000000001)
		# Replace it with empty string
		sentence_new = regexp_gdp.sub('', sentence)

	# Create key words
	greater = ['greater', 'more', 'at least']
	less = ['less', 'no more', 'at most']
	
	less_list = list(map(lambda x : x in sentence, less))
	less_result = True in less_list
	greater_list = list(map(lambda x : x in sentence, greater))
	greater_result = True in greater_list
	
	# we got year
	if m is not None and n is not None:
		query = "SELECT * FROM gdpperyear WHERE YEAR="+str(year)
		result = querydb(query)
		if len(result) > 0:
			gdp_value = result[0][1]
			# Check if we caught any key words
			if less_result:
				return {"truth":gdp_value < gdp, "reason":"The real value is $"+str(gdp_value) + " billion."}
			if greater_result:
				return {"truth":gdp_value > gdp, "reason":"The real value is $"+str(gdp_value) + " billion."}
			if gdp > float(0.98 * gdp_value) and gdp < float(1.02 * gdp_value):
				return {"truth":True, "reason":"The real value is $"+str(gdp_value) + " billion."}
			else:
				return {"truth":False, "reason":"The real value is $"+str(gdp_value) + " billion."}
		return {"truth":None, "reason":"There is no data for " + str(year) + "."}
	 
	# we didn't get year
	elif n is None and m is not None:
		if less_result:
			query_less = "SELECT * FROM gdpperyear WHERE \"gdp value\" <" + str(gdp)
			result = querydb(query_less)
		elif greater_result:
			query_greater = "SELECT * FROM gdpperyear WHERE \"gdp value\" >" + str(gdp)
			result = querydb(query_greater)
		else:
			query = "SELECT * FROM gdpperyear WHERE \"gdp value\" BETWEEN " + str(gdp*0.98) + " AND " + str(gdp*1.02)
			result = querydb(query)
		if len(result) > 0:
			return {"truth":True, "reason":result[len(result) - 1]}
		else:
			if less_result:
				return {"truth":False, "reason":"The least value is $1000 billion in 1947."}
			elif greater_result:
				return {"truth":False, "reason":"The greatest value is $74276.4 billion in 2016."}
			else:
				return {"truth":False, "reason":"There is no year which gdp value is $" + str(gdp) + " billion."}
	elif n is not None and m is None:
		query = "SELECT * FROM gdpperyear WHERE YEAR="+str(year)
		result = querydb(query)
		return {"truth":None, "reason":"The real value in " + str(year) + " should be $" + str(result[0][1]) + " billion."}

	else:
		return {"truth":None, "reason":"We don't know"}
