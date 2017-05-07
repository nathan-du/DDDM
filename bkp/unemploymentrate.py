import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re
from querydb import querydb

def parseSentence(sentence):
	regexp_year = re.compile('(in|year)\s(\d{4})')
	n = regexp_year.search(sentence)
	if n is not None:
		year_string = n.group()
		w = year_string.split(' ')
		year = int(w[1])
		# Replace it with empty string
		sentence = regexp_year.sub('', sentence)

	# Regular expression	
	regexp_percentages = re.compile('(\d*.)?\d+(%|\s*percent)?')
	m = regexp_percentages.search(sentence)	
	if m is not None:
		number_string = m.group()
		unemployment = float(number_string.split('%')[0])


	# Create key words
	greater = ['greater', 'more', 'at least']
	less = ['less', 'no more', 'at most']

	less_list = list(map(lambda x: x in sentence.lower(), less))
	less_result = True in less_list
	greater_list = list(map(lambda x : x in sentence.lower(), greater))
	greater_result = True in greater_list

	if m is not None and n is not None:
		query = "SELECT * FROM unemploymentrate WHERE YEAR="+str(year)
		result = querydb(query)
		if len(result) > 0:
			unemployment_truth = result[0][1]
			# Check if we caught any key word
			if less_result:
				return {"truth":unemployment_truth < unemployment, "reason":wordify(result)}
			if greater_result:
				return {"truth":unemployment_truth > unemployment, "reason":wordify(result)}
			if unemployment > float(0.98 * unemployment_truth) and unemployment < float(1.02*unemployment_truth):
				return {"truth":True, "reason":wordify(result)}
			else:
				return {"truth":False, "reason":wordify(result)}
		return {"truth":None, "reason": "There is no data for that year."}
			

	elif n is None:
		query_less = "SELECT * FROM unemploymentrate WHERE UNEMPLOYMENT_RATE < " + str(unemployment)
		query_greater = "SELECT * FROM unemploymentrate WHERE UNEMPLOYMENT_RATE > " + str(unemployment)
		query = "SELECT * FROM unemploymentrate WHERE UNEMPLOYMENT_RATE BETWEEN " + str(unemployment*0.98) + " AND " + str(unemployment*1.02)	
		if less_result:
			result = querydb(query_less)
		elif greater_result:
			result = querydb(query_greater)
		else:
			result = querydb(query)
		if len(result) > 0:
			return {"truth":True, "reason":wordify(result)}
		else:
			return {"truth":False, "reason":"No year has the specified unemployment rate"}

def wordify(rows):
	explanaition = ""
	for row in rows:
		explanaition += "The unemployment rate for " + str(row[0]) + " was " + str(row[1]) + ".\n"
	return explanaition


