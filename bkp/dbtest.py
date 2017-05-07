from querydb import querydb

print(querydb("SELECT * FROM presidentialelections WHERE YEAR=2016"))
print(querydb("SELECT * FROM presidentialelections WHERE NAME='Donald Trump'"))
