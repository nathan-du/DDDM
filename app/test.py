import findTable as ft


s1 = "The unemployment rate was 4.8%"
s2 = "The unemployment rate was 8.2% in 2012"
s3 = "Unemployment rate was 5.3 percent"
s4 = "Unemployment was 90%"
s5 = "The unemployment rate was greater than 4% in 2012"
s6 = "The unemployment rate was less than 4% in 2012"
s7 = "The unemployment rate was at least 5%"
s8 = "The unemployment rate was at most 6%"

#print(ft.findTable(s1), " - Real: True")
#print(ft.findTable(s2), " - Real: True")
#print(ft.findTable(s3), " - Real: True")
#print(ft.findTable(s4), " - Real: False")
#print(ft.findTable(s5), " - Real: True")
#print(ft.findTable(s6), " - Real: False")
#print(ft.findTable(s7), " - Real: True")
#print(ft.findTable(s8), " - Real: True")

s9 = "The GDP was $66766 billion in 2013"
s10 = "The GDP was $66765 billion in 2013"
s11 = "The GDP was $60000 billion in 2013"
s12 = "The GDP was $66.7 trillion in 2013"
s13 = "The GDP was $66766000000000"
s14 = "The GDP was greater than $1 in 2013"
s15 = "The GDP was less than $70000 billion in 2013"
s16 = "The GDP was at least $1"
s17 = "The GDP was at most $70000 billion"

print(ft.findTable(s9), " Real: True")
print(ft.findTable(s10), " Real: True")
print(ft.findTable(s11), " Real: False")
print(ft.findTable(s12), " Real: True")
#print(ft.findTable(s13), " Real: True")
print(ft.findTable(s14), " Real: True")
print(ft.findTable(s15), " Real: True")
#print(ft.findTable(s16), " Real: True")
print(ft.findTable(s17), " Real: True")


