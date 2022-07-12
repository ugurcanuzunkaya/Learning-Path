a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
i = 0
if a > b:
    remainder = a
    while remainder >= b:
        remainder -= b
        i = i + 1
else:
    remainder = b
    while remainder >= a:
        remainder -= a
        i = i + 1

print(f"{remainder} is the remainder {str(i)} is the quotient")
