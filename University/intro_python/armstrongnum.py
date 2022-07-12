n =int(input('enter: '))
sum1 = 0
n = str(n)
for i in range(0,len(n)):
	a = int(n[i])**len(n)
	sum1 = sum1 + a
if sum1 == int(n):
	print('it is okay')
else:
	print('it is not okay')