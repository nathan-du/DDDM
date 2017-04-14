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
	regexp_integers = re.compile('\d+')
	m = regexp_integers.search(sentence)
	if m is not None:
		votes_string = m.group()
		votes = int(votes_string)

	# Type Of Vote: 0 look for both, 1 electoral, 2 popular
	type_of_vote = 0

	# Regexp for catching the term electoral vote
	regexp_elect_votes = re.compile('electoral\s*vote')
	o = regexp_elect_votes.search(sentence)
	elect_votes = None
	if o is not None:
		type_of_vote = 1
		sentence = regexp_elect_votes.sub('', sentence)
 
	# Regexp for catching the term popular vote
	regexp_votes = re.compile('popular\s*vote')
	p = regexp_votes.search(sentence)
	if p is not None:
		type_of_vote = 2
		sentence = regexp_elect_votes.sub('', sentence)


	list_of_presidents = getData("presidents")
	#list_of_parties = getData("parties")


	# Tokenize input sentence
	tokenizer = RegexpTokenizer(r'\w+')
	sentence_tokens = tokenizer.tokenize(sentence)

	# Remove stopwords
	stop = set(stopwords.words('english'))
	stop.add('\xc2')
	sentence_selected = [x for x in sentence_tokens if x.lower() not in stop]

	# Filter input words
	president_names = []
	main_list = [0 for x in list_of_presidents]
	for word in sentence_selected:
		new_list = list(map(lambda x : 1 if word.lower() in x.lower() else 0, list_of_presidents))
		main_list = list(map(add, main_list, new_list))

	val = max(main_list)
	if val > 0:
		i = 0
		for elem in main_list:
			if elem == val:
				president_names.append(list_of_presidents[i])
			i += 1

	# Find in database
	# Case: we know NAME and YEAR
	if len(president_names) > 0 and year is not None:
		query = "SELECT * FROM presidentialelections WHERE NAME=" + str(president_names[0]) + " AND YEAR=" + str(year)
	elif len(president_names) > 0:
		query = "SELECT * FROM presidentialelections WHERE NAME=" + str(president_names[0])
	elif year is not None:
		query = "SELECT * FROM presidentialelections WHERE YEAR=" + str(year)
	# Find in database
	result = querydb(query)

	l = len(result)
	electoral_truth = int(result[0][4])
	popular_truth = int(result[0][5])
	# Compare truth value with user input
	if type_of_vote == 1: #ELECTORAL
		if votes > int(0.98*electoral_truth) and votes < int(1.02*electoral_truth):
			return True
		else:
			return False
	elif type_of_vote == 2: #POPULAR
		if votes > int(0.98*popular_truth) and votes < int(1.02*popular_truth):
			return True
		else:
			return False
	else: #BOTH
		if (votes > int(0.98*electoral_truth) and votes < int(1.02*electoral_truth) or (votes > int(0.98*populat_truth) and votes < int(1.02*):
			return True
		else:
			return False


	if number > int(0.98 * val) and number < int(1.02*val):
		return True
	else:
		return False



def convertIntoString(data):
	return ""
