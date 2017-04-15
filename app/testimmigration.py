from immigrationpercountry import parseSentence as ps

s1 = "Number of immigrants from India in the year 2016 was 10000"
s2 = "Number of immigrants from Gabon in 2003 was 40" 
s3 = "Number of immigrants from Iran was 7230"
s4 = "Number of immigrants from Iran was 1"
s5 = "Total number of immigrants from Iran is 167875"
s6 = "Number of immigrants from Iran in 2003 was more than 6000"
s7 = "Number of immigrants from Iran in 2003 was more than 900000"
s8 = "Number of immigrants from Iran in 2003 was less than 9000000"
s9 = "Number of immigrants from Iran in 2003 was less than 6000"
s10 = "More than 10 people have immigrated from Iran"
s11 = "More than 1000000000 people have immigrated from Iran"
s12 = "Less than 8000 people have immigrated from Iran"
s13 = "Less than 12 people have immigrated from Iran"
s14 = "1252 people immigrated in 2003"
s15 = "0 people immigrated in 2003"
s16 = "703521 people immigrated in 2003"
s17 = "more than 1000 people immigrated in 2003"
s18 = "more than 700000 people immigrated in 2003"
s19 = "more than 1000000 people immigrated in 2003"
s20 = "less than 35 people immigrated in 2003"
s21 = "less than 1000000 people immigrated in 2003"
s22 = "less than 0 people immigrated in 2003"
s23 = "Less than 70 people immigrated"
s24 = "more than 1000 people immigrated"
s25 = "1252 people immigrated"
s26 = "more than 44000 people immigrated"
s27 = "45619 people immigrated"
s28 = "more than 13000000 people immigrated"
s29 = "13534341 people immigrated"
s30 = "15000000 people immigrated"



print(str(1), ps(s1), " - Expected: None")
print(str(2), ps(s2), " - Expected: True")
print(str(3), ps(s3), " - Expected: True")
print(str(4), ps(s4), " - Expected: False")
print(str(5), ps(s5), " - Expected: True")
print(str(6), ps(s6), " - Expected: True")
print(str(7), ps(s7), " - Expected: False")
print(str(8), ps(s8), " - Expected: True")
print(str(9), ps(s9), " - Expected: False")
print(str(10), ps(s10), " - Expected: True")
print(str(11), ps(s11), " - Expected: False")
print(str(12), ps(s12), " - Expected: True")
print(str(13), ps(s13), " - Expected: False")
print(str(14), ps(s14), " - Expected: True")
print(str(15), ps(s15), " - Expected: False")
print(str(16), ps(s16), " - Expected: True")
print(str(17), ps(s17), " - Expected: True")
print(str(18), ps(s18), " - Expected: True")
print(str(19), ps(s19), " - Expected: False")
print(str(20), ps(s20), " - Expected: True")
print(str(21), ps(s21), " - Expected: True")
print(str(22), ps(s22), " - Expected: False")
print(23, ps(s23), " - Expected: True")
print(24, ps(s24), " - Expected: True")
print(25, ps(s25), " - Expected: True")
print(26, ps(s26), " - Expected: True")
print(27, ps(s27), " - Expected: True")
print(28, ps(s28), " - Expected: True")
print(29, ps(s29), " - Expected: True")
print(30, ps(s30), " - Expected: False")
