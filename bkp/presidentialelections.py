from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from dictionaries import getData
from operator import add
from querydb import querydb

def parseSentence(sentence):
	# Regular expression for catching year
	regexp_year = re.compile('(in|year)\s(\d{4})')
	n = regexp_year.search(sentence)
	if n is not None:
		year_string = n.group()
		w = year_string.split(' ')
		year = int(w[1])
		# Replace it with empty string
		sentence = regexp_year.sub('', sentence)

	# Regexp for catching number of votes
	regexp_integers = re.compile('\d+\s(million)?')
	m = regexp_integers.search(sentence)
	if m is not None:
		votes_string = m.group()
		if "million" in votes_string:
			vot = votes_string.split(' ')
			votes = int(vot[0]+'000000')
		else:
			votes = int(votes_string)
		sentence = regexp_integers.sub('', sentence)

	# Type Of Vote: 0 look for both, 1 electoral, 2 popular
	type_of_vote = 0

	# Regexp for catching the term electoral vote
	regexp_elect_votes = re.compile('electoral\s*votes')
	o = regexp_elect_votes.search(sentence)
	elect_votes = None
	if o is not None:
		type_of_vote = 1
		sentence = regexp_elect_votes.sub('', sentence)
 
	# Regexp for catching the term popular vote
	regexp_popular_votes = re.compile('popular\s*votes')
	p = regexp_popular_votes.search(sentence)
	if p is not None:
		type_of_vote = 2
		sentence = regexp_popular_votes.sub('', sentence)

	if o is None and p is None:
		regexp_votes = re.compile('votes')
		q = regexp_votes.search(sentence)
		type_of_cote = 0
		sentence = regexp_votes.sub('', sentence)

	# Create key words
	greater = ['greater', 'more', 'at least', 'beat', 'won against', 'won', 'elected', 'became president', 'winner']
	less = ['less', 'no more', 'at most', 'was beaten', 'lost against', 'lost', 'not elected', 'loser']

	# 0: No Comparison. 1: Less than. 2: Greater than
	compare = 0
	greater_list = list(map(lambda x : x in sentence.lower(), greater))
	if True in greater_list:
		compare = 2
	less_list = list(map(lambda x : x in sentence.lower(), less))
	if True in less_list:
		compare = 1

	list_of_presidents = getData("presidents")
	list_of_presidents_lower = [x.lower() for x in list_of_presidents]
	#list_of_parties = getData("parties")

	# Tokenize input sentence
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence)

	# Remove stopwords
	stop = set(stopwords.words('english'))
	stop.add('\xc2')
	sentence_selected = [x for x in sentence_tokens if x.lower() not in stop]

	# Filter input words
	pres_list1 = [0 for x in list_of_presidents]
	pres_list2 = [0 for x in list_of_presidents]
	found = False
	word_pos = 0
	# Get first president list
	for word in sentence_selected:
		i = 0
		for pres in list_of_presidents:
			if len(word) > 3 and word.lower() in pres.lower():
				pres_list1[i] += 1
				found = True
			i += 1
		if found and word.lower() not in list_of_presidents_lower:
			break
		word_pos += 1
	# Get second president list
	for word in sentence_selected[word_pos+1:]:
		i = 0
		for pres in list_of_presidents:
			if len(word) > 4 and word.lower() in pres.lower():
				pres_list2[i] += 1
			i += 1


	# Get max appearance of presidents
	val1 = max(pres_list1)
	president1_names = []
	if val1 > 0:
		i = 0
		for pres in pres_list1:
			if pres == val1:
				president1_names.append(list_of_presidents[i])
			i += 1

	val2 = max(pres_list2)
	president2_names = []
	if val2 > 0:
		i = 0
		for pres in pres_list2:
			if pres == val2:
				president2_names.append(list_of_presidents[i])
			i += 1

	case = -1
	# Find in database
	if compare == 0 and len(president1_names) > 0 and len(president2_names) == 0 and n is not None:
		# Case 0: No Comparison and we know NAME and YEAR
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "' AND YEAR=" + str(year)
		case = 0
	elif compare == 0 and len(president1_names) > 0 and len(president2_names) == 0:
		# Case 1: No Comparison and we just know NAME
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "'"
		case = 1
	elif compare == 0 and len(president2_names) == 0 and n is not None:
		# Case 2: No Comparison and we just know YEAR
		query = "SELECT * FROM presidentialelections WHERE YEAR=" + str(year)
		case = 2
	elif compare == 1 and len(president1_names) > 0 and len(president2_names) == 0 and n is not None:
		# Case 3: LESS than, and we know YEAR and just 1 president NAME
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "' AND YEAR='" + str(year) + "'"
		case = 3
	elif compare == 1 and len(president1_names) > 0 and len(president2_names) == 0:
		# Case 4: LESS than, and we know just 1 president NAME
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "'"
		case = 4
	elif compare == 1 and len(president1_names) > 0 and len(president2_names) > 0:
		# Case 5: Less than, and we know 2 president NAMEs
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "'"
		query_2 = "SELECT * FROM presidentialelections WHERE NAME='" + str(president2_names[0]) + "'"
		case = 5
	elif compare == 2 and len(president1_names) > 0 and len(president2_names) == 0 and n is not None:
		# Case 6: MORE than, and we know YEAR and just 1 president NAME
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "' AND YEAR=" + str(year)
		case = 6
	elif compare == 2 and len(president1_names) > 0 and len(president2_names) == 0:
		# Case 7: MORE than, and we know just 1 president NAME
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "'"
		case = 7
	elif compare == 2 and len(president1_names) > 0 and len(president2_names) > 0:
		# Case 8: MORE than, and we know 2 president NAMEs
		query = "SELECT * FROM presidentialelections WHERE NAME='" + str(president1_names[0]) + "'"
		query_2 = "SELECT * FROM presidentialelections WHERE NAME='" + str(president2_names[0]) + "'"
		case = 8


	# Find in database
	result = querydb(query)
	if case == 5 or case == 8:
		result2 = querydb(query_2)
		l2 = len(result2)
		electoral_truth2 = int(result2[0][4])
		popular_truth2 = int(result2[0][5])

	l = len(result)
	if l == 0:
		return {'truth': None, 'reason': 'No data matching your input.'}

	electoral_truth = int(result[0][4])
	popular_truth = int(result[0][5])
	won_truth = False if result[0][6] == 'FALSE' else True
	# Compare truth value with user input
	if case == 0 or case == 1 or case == 2:
		if type_of_vote == 0:
			if votes > int(0.98*electoral_truth) and votes < int(1.02*electoral_truth):
				# Electoral votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			elif votes > int(0.98*popular_truth) and votes < int(1.02*popular_truth):
				# Popular votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
		elif type_of_vote == 1:
			if votes > int(0.98*electoral_truth) and votes < int(1.02*electoral_truth):
				# Electoral votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
		elif type_of_vote == 2:
			if votes > int(0.98*popular_truth) and votes < int(1.02*popular_truth):
				# Popular votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
	elif case == 3 or case == 4:
		if m is None:
			if won_truth == False:
				return {'truth': True, 'reason': wordify(result, None, 1)}
			return {'truth': False, 'reason': wordify(result, None, 2)}
		elif type_of_vote == 0:
			if electoral_truth < votes:
				# Electoral votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			elif popular_truth < votes:
				# Popular votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
		elif type_of_vote == 1:
			if electoral_truth < votes:
				# Electoral votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
		elif type_of_vote == 2:
			if popular_truth < votes:
				# Popular votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
	elif case == 5:
		if type_of_vote == 0:
			if electoral_truth < electoral_truth2:
				# Electoral votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			elif popular_truth < popular_truth2:
				# Popular votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			return {'truth': False, 'reason': wordify(result, result2, 3)}
		elif type_of_vote == 1:
			if electoral_truth < electoral_truth2:
				# Electoral votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			return {'truth': False, 'reason': wordify(result, result2, 3)}
		elif type_of_vote == 2:
			if popular_truth < popular_truth2:
				# Popular votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			return {'truth': False, 'reason': wordify(result, result2, 3)}
	elif case == 6 or case == 7:
		if m is None:
			if won_truth == True:
				return {'truth': True, 'reason': wordify(result, None, 2)}
			return {'truth': False, 'reason': wordify(result, None, 1)}
		elif type_of_vote == 0:
			if electoral_truth > votes:
				# Electoral votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			elif popular_truth > votes:
				# Popular votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
		elif type_of_vote == 1:
			if electoral_truth > votes:
				# Electoral votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
		elif type_of_vote == 2:
			if popular_truth > votes:
				# Popular votes match
				return {'truth': True, 'reason': wordify(result, None, 0)}
			return {'truth': False, 'reason': wordify(result, None, 0)}
	elif case == 8:
		if type_of_vote == 0:
			if electoral_truth > electoral_truth2:
				# Electoral votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			elif popular_truth > popular_truth2:
				# Popular votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			return {'truth': False, 'reason': wordify(result, result2, 3)}
		elif type_of_vote == 1:
			if electoral_truth > electoral_truth2:
				# Electoral votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			return {'truth': False, 'reason': wordify(result, result2, 3)}
		elif type_of_vote == 2:
			if popular_truth > popular_truth2:
				# Popular votes is true
				return {'truth': True, 'reason': wordify(result, result2, 3)}
			return {'truth': False, 'reason': wordify(result, result2, 3)}
	else:
		return {'truth': None, 'reason': 'No data matching your input.'}
		
		

def wordify(rows, rows2, case):
	explanation = ""
	for row in rows:
		if case == 0:
			explanation += row[2] + " obtained " + str(row[4]) + " electoral votes and " + str(row[5]) + " popular votes in " + str(row[1]) + ".\n"
		elif case == 1:
			explanation += row[2] + " lost the elections in the year " + str(row[1]) + ".\n"
		elif case == 2:
			explanation += row[2] + " won the elections in the year " + str(row[1]) + ".\n"
		elif case == 3:
			explanation += row[2] + " obtained " + str(row[4]) + " electoral votes and " + str(row[5]) + " popular votes in " + str(row[1]) + ".\n" 
			for row2 in rows2:
				explanation += row2[2] + " obtained " + str(row2[4]) + " electoral votes and " + str(row2[5]) + " popular votes in " + str(row2[1]) + ".\n"
	return explanation

