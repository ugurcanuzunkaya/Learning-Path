total = 0
s = "1.23,2.4,3.123"

for current_number in s.split(","):
    total += float(current_number)

print(total)


