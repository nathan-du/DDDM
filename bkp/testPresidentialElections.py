from findTable import findTable

s1 = "Hillary got 5000000 votes in 2016"
s2 = "Hillary got 50000000 popular votes in 2012"
s3 = "Obama got 350 electoral votes"
s4 = "Someone got 63000000 votes in 2016"
s5 = "Someone got 2 votes in 2013"
s6 = "Trump lost in 2016"
s7 = "Hillary lost"
s8 = "Hillary obtained less votes than Trump"
s9 = "Hillary won in 2016"
s10 = "Obama won in 2015"
s11 = "Trump got more than 50000000 votes"
s12 = "Trump got more electoral votes than Obama"
s13 = "Trump beat Hillary"

print(findTable(s1), " REAL: FALSE, case 0")
print(findTable(s2), " REAL: None, case 0")
print(findTable(s3), " REAL: FALSE, case 1")
print(findTable(s4), " REAL: TRUE, case 2")
print(findTable(s5), " REAL: None, case 2")
print(findTable(s6), " REAL: FALSE, case 3")
print(findTable(s7), " REAL: TRUE, case 4")
print(findTable(s8), " REAL: TRUE, case 5")
print(findTable(s9), " REAL: FALSE, case 6")
print(findTable(s10), " REAL: None, case 6")
print(findTable(s11), " REAL: TRUE, case 7")
print(findTable(s12), " REAL: FALSE, case 8")
print(findTable(s13), " REAL: TRUE, case 8")

