import findTable as ft

s9 = "The GDP was $66766 billion in 2013"
s10 = "The GDP was $66765 billion in 2013"
s11 = "The GDP was $60000 billion in 2013"
s12 = "The GDP was $66.7 trillion in 2013"
s13 = "The GDP was $66766000000"
s14 = "The GDP was greater than $1 in 2013"
s15 = "The GDP was less than $70000 billion in 2013"
s16 = "The GDP was at least $10000000 billion"
s17 = "The GDP was at most $70000 billion"
s18 = "The GDP is"
s19 = "The GDP in 2013 is"

print(ft.findTable(s9), " Real: True")
print(ft.findTable(s10), " Real: True")
print(ft.findTable(s11), " Real: False")
print(ft.findTable(s12), " Real: True")
print(ft.findTable(s13), " Real: True")
print(ft.findTable(s14), " Real: True")
print(ft.findTable(s15), " Real: True")
print(ft.findTable(s16), " Real: False")
print(ft.findTable(s17), " Real: True")
print(ft.findTable(s18))
print(ft.findTable(s19))
