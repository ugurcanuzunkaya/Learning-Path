num = int(input("Enter an integer: "))
pwr = 2
root = 0
found = False
while pwr < 6:
    while abs(root ** pwr) <= abs(num):
        if root ** pwr == num:
            print(str(root) + "**" + str(pwr) + " = " + str(num))
            found = True
        root += 1
    pwr += 1
    root = 0

if not found:
    print("No pair of integers, 'root' and 'pwr', exists such that 0 < pwr < 6 and root**pwr = " + str(num))



