import nltk
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
#import sklearn.naive_bayes
#from sklearn.neighbors import KNeighborsClassifier

#EDIT THIS TO READ THE TERMS FROM A FILE
#print("Opening Files...")
with open('./datafiles/electionwords.txt') as f:
	dicElections = [line.strip() for line in f]
with open('./datafiles/economywords.txt') as f:
	dicEconomy = [line.strip() for line in f]
with open('./datafiles/immigration.txt') as f:
	dicImmigration = [line.strip() for line in f]

#READ TEST SET
economyTest = open('./testfiles/economytest.txt').read()
electionsTest = open('./testfiles/electiontest.txt').read()
immigrationTest = open('./testfiles/immigrationtest.txt').read()

#EDIT THIS TO READ A BIG FILE ABOUT EACH TOPIC
print("Reading Files...")
dataEconomyTraining = open('./Economy.TXT').read()
dataElectionsTraining = open('./Election.TXT').read()
dataImmigrationTraining = open('./Immigration.TXT').read()

#TOKENIZE DATA AND REMOVE PUNCTUATION
print("Tokenizing Files...")
tokenizer = RegexpTokenizer(r'\w+')
economyAllTokens = tokenizer.tokenize(dataEconomyTraining)
electionsAllTokens = tokenizer.tokenize(dataElectionsTraining)
immigrationAllTokens = tokenizer.tokenize(dataImmigrationTraining)

#TOKENIZE TEST DATA AND REMOVE PUNCTUATION
economyTestTokens = tokenizer.tokenize(economyTest)
electionsTestTokens = tokenizer.tokenize(electionsTest)
immigrationTestTokens = tokenizer.tokenize(immigrationTest)

#REMOVE STOPWORDS FROM FILES
print("Removing StopWords...")
stop = set(stopwords.words('english'))
stop.add('\xc2')
economySelected = [x for x in economyAllTokens if x.lower() not in stop]
electionsSelected = [x for x in electionsAllTokens if x.lower() not in stop]
immigrationSelected = [x for x in immigrationAllTokens if x.lower() not in stop]

#REMOVE STOPWORDS FROM TEST FILES
economyTestSelected = [x for x in economyTestTokens if x.lower() not in stop]
electionsTestSelected = [x for x in electionsTestTokens if x.lower() not in stop]
immigrationTestSelected = [x for x in immigrationTestTokens if x.lower() not in stop]

# Filter out the dictionary words
# ECONOMY
print("Finding Dictionary Words...")
economyWordsInEconomy = [x for x in economySelected if x.lower() in dicEconomy]
immigrationWordsInEconomy = [x for x in economySelected if x.lower() in dicImmigration]
electionsWordsInEconomy = [x for x in economySelected if x.lower() in dicElections]

economyWordsInImmigration = [x for x in immigrationSelected if x.lower() in dicEconomy]
immigrationWordsInImmigration = [x for x in immigrationSelected if x.lower() in dicImmigration]
electionsWordsInImmigration = [x for x in immigrationSelected if x.lower() in dicElections]

economyWordsInElections = [x for x in electionsSelected if x.lower() in dicEconomy]
immigrationWordsInElections = [x for x in electionsSelected if x.lower() in dicImmigration]
electionsWordsInElections = [x for x in electionsSelected if x.lower() in dicElections]


#TEST SET DICTIONARY COMPARISON
testEconomyInEconomy = [x for x in economyTestSelected if x.lower() in dicEconomy]
testEconomyInElections = [x for x in economyTestSelected if x.lower() in dicElections]
testEconomyInImmigration = [x for x in economyTestSelected if x.lower() in dicImmigration]

testElectionsInEconomy = [x for x in electionsTestSelected if x.lower() in dicEconomy]
testElectionsInElections = [x for x in electionsTestSelected if x.lower() in dicElections]
testElectionsInImmigration = [x for x in electionsTestSelected if x.lower() in dicImmigration]

testImmigrationInEconomy = [x for x in immigrationTestSelected if x.lower() in dicEconomy]
testImmigrationInElections = [x for x in immigrationTestSelected if x.lower() in dicElections]
testImmigrationInImmigration = [x for x in immigrationTestSelected if x.lower() in dicImmigration]


print("\n\n\n-------------------------------------------------------")
#Build training set
print("\nFor each dictionary, the percentage in which those words appear in each of the files: ") 
categories = ["Economy", "Immigration", "Elections"]
economyPercent = [round(float(100*len(economyWordsInEconomy))/len(economySelected), 4), round(float(100*len(immigrationWordsInEconomy))/len(economySelected), 4), round(float(100*len(electionsWordsInEconomy))/len(economySelected), 4)]
immigrationPercent = [round(float(100*len(economyWordsInImmigration))/len(immigrationSelected), 4), round(float(100*len(immigrationWordsInImmigration))/len(immigrationSelected), 4), round(float(100*len(electionsWordsInImmigration))/len(immigrationSelected), 4)]
electionsPercent = [round(float(100*len(economyWordsInElections))/len(electionsSelected), 4), round(float(100*len(immigrationWordsInElections))/len(electionsSelected), 4), round(float(100*len(electionsWordsInElections))/len(electionsSelected), 4)]

#STORE PERCENTAGES IN A MATRIX
data = [economyPercent, immigrationPercent, electionsPercent]

#PRINT MATRIX
row_format = "{:>20}" * (len(categories) + 1)
print(row_format.format("", *categories))
for category, row in zip(categories, data):
	print(row_format.format(category, *row))

totalEconomy = len(economyWordsInEconomy) + len(immigrationWordsInEconomy) + len(electionsWordsInEconomy)
totalImmigration = len(economyWordsInImmigration) + len(immigrationWordsInImmigration) + len(electionsWordsInImmigration)
totalElections = len(economyWordsInElections) + len(immigrationWordsInElections) + len(electionsWordsInElections)

#print("TOTALS")
#print(totalEconomy, totalImmigration, totalElections)
economyNormalized = [round(float(100*len(economyWordsInEconomy)) / totalEconomy, 4), round(float(100*len(immigrationWordsInEconomy)) / totalEconomy, 4), round(float(100*len(electionsWordsInEconomy)) / totalEconomy, 4)]
immigrationNormalized = [round(float(100*len(economyWordsInImmigration)) / totalImmigration, 4), round(float(100*len(immigrationWordsInImmigration)) / totalImmigration, 4), round(float(100*len(electionsWordsInImmigration)) / totalImmigration, 4)]
electionsNormalized = [round(float(100*len(economyWordsInElections)) / totalElections, 4), round(float(100*len(immigrationWordsInElections)) / totalElections, 4), round(float(100*len(electionsWordsInElections)) / totalElections, 4)]
normalizedData = [economyNormalized, immigrationNormalized, electionsNormalized]


#PRINT NORMALIZED MATRIX
print("\n\nNormalized values: ")
print(row_format.format("", *categories))
for category, row in zip(categories, normalizedData):
	print(row_format.format(category, *row))

# Labels: Economy (0), Immigration (1), Elections(2)
x = [economyNormalized, immigrationNormalized, electionsNormalized]
y = [0, 1, 2]

valuesEconomy = [len(testEconomyInEconomy), len(testEconomyInImmigration), len(testEconomyInElections)]
valuesElections = [len(testElectionsInEconomy), len(testElectionsInImmigration), len(testElectionsInElections)]
valuesImmigration = [len(testImmigrationInEconomy), len(testImmigrationInImmigration), len(testImmigrationInElections)]
values = [valuesEconomy, valuesImmigration, valuesElections]

print("\n\nMatching words in the test files: ")
print(row_format.format("", *categories))
for category, row in zip(categories, values):
	print(row_format.format(category+" Test:", *row))


print("\n\nReal class: Economy. Prediction: " + ("Economy", "Elections", "Immigration")[valuesEconomy.index(max(valuesEconomy))])
print("Real class: Elections. Prediction: " + ("Economy", "Elections", "Immigration")[valuesElections.index(max(valuesElections))])
print("Real class: Immigration. Prediction: " + ("Economy", "Elections", "Immigration")[valuesImmigration.index(max(valuesImmigration))])
print("\n---------------------------------------------------------")
print("\n\n\n\n")


#knn = KNeighborsClassifier(n_neighbors = 1)
#knn.fit(x, y)

