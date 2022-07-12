total = 0
s = "1.23,2.4,3.123"
subS = ""
for i in s:
    if i != ",":
        subS = subS + i
    else:
        total += float(subS)
        subS=""
total += float(subS) # For last float number
print(total)


