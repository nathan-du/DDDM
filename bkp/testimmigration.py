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
s31 = "In 2003 0.178% of immigrants came from Afghanistan"
s32 = "In 2003 20% of immigrants came from Afghanistan"
s33 = "In 2003 more than 0% of immigrants cam from India"
s34 = "In 2005 less than 99% of immigrants came from Panama"
s35 = "0.178% of immigrants came from Afghanistan"
s36 = "95% of immigrants came from afghanistan"
s37 = "more than 0% of immigrants came from India"
s38 = "less than 99% of immigrants can from Germany"

print(str(1), ps(s1)["truth"], " - Expected: None")
print(str(2), ps(s2)["truth"], " - Expected: True")
print(str(3), ps(s3)["truth"], " - Expected: True")
print(str(4), ps(s4)["truth"], " - Expected: False")
print(str(5), ps(s5)["truth"], " - Expected: True")
print(str(6), ps(s6)["truth"], " - Expected: True")
print(str(7), ps(s7)["truth"], " - Expected: False")
print(str(8), ps(s8)["truth"], " - Expected: True")
print(str(9), ps(s9)["truth"], " - Expected: False")
print(str(10), ps(s10)["truth"], " - Expected: True")
print(str(11), ps(s11)["truth"], " - Expected: False")
print(str(12), ps(s12)["truth"], " - Expected: True")
print(str(13), ps(s13)["truth"], " - Expected: False")
print(str(14), ps(s14)["truth"], " - Expected: True")
print(str(15), ps(s15)["truth"], " - Expected: False")
print(str(16), ps(s16)["truth"], " - Expected: True")
print(str(17), ps(s17)["truth"], " - Expected: True")
print(str(18), ps(s18)["truth"], " - Expected: True")
print(str(19), ps(s19)["truth"], " - Expected: False")
print(str(20), ps(s20)["truth"], " - Expected: True")
print(str(21), ps(s21)["truth"], " - Expected: True")
print(str(22), ps(s22)["truth"], " - Expected: False")
print(23, ps(s23)["truth"], " - Expected: True")
print(24, ps(s24)["truth"], " - Expected: True")
print(25, ps(s25)["truth"], " - Expected: True")
print(26, ps(s26)["truth"], " - Expected: True")
print(27, ps(s27)["truth"], " - Expected: True")
print(28, ps(s28)["truth"], " - Expected: True")
print(29, ps(s29)["truth"], " - Expected: True")
print(30, ps(s30)["truth"], " - Expected: False")
print(31, ps(s31)["truth"], " - Expected: True")
print(32, ps(s32)["truth"], " - Expected: False")
print(33, ps(s33)["truth"], " - Expected: True")
print(34, ps(s34)["truth"], " - Expected: True")
print(35, ps(s35)["truth"], " - Expected: True")
print(36, ps(s36)["truth"], " - Expected: False")
print(37, ps(s37)["truth"], " - Expected: True")
print(38, ps(s38)["truth"], " - Expected: True")
