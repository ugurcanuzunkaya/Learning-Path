a = [3, 6, 10, 8]
i, j, ssum, standardsum = 0, 0, 0, 0
while i < len(a):
    ssum = ssum + a[i]
    i += 1
mean = ssum / len(a)
while j < len(a):
    standardsum = standardsum + (a[j]-mean)**2
    j += 1
standarddev = (standardsum/(len(a)-1))**0.5
print(standarddev, "of array a")
