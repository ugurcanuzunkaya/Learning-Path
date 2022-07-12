def applyToEach(L, f):
  """ Assumes L is a list, f a function
    Mutates L by replacing each element, e, of L by f(e)  """
  for i in range(len(L)):
    L[i] = f(L[i])
def line(x):
  a,b=2,3
  y=a*x +b
  return y

L = [1, -2, 3.33]
print('L :', L)
print(50*"-")
print('Apply abs to each element of L')
applyToEach(L, abs)
print('L : ', L)

print(50*"-")
print('Apply int to each element of L')
applyToEach(L, int)
print('L : ', L)

print(50*"-")
print('Apply line function to each element of L')
applyToEach(L, line)
print('L : ', L)

