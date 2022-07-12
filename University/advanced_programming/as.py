def prime1(x):
    if x == 1:
      return False
    elif x == 2:
      return True
    else:
      for i in range(2,x):
        if x%i == 0:
          return False
      return True

def prime2(y):
  if y == 1:
    return False
  elif y == 2:
    return True
  else:
    for i in range(2,int(y**0.5)+1):
      if y%i == 0:
        return False
    return True


primelist=[]
for i in range(2,1000):
  if prime2(i):
    primelist.append(i)
    print(i, end=",")
print()


def perfect1(q):
  a = 0
  for i in range(1,q):
    if q%i == 0:
      a += i
  if a == q:
    return True
  else:
    return False

def perfect2(w):
  n = (2**(w-1))*((2**w)-1)
  return n

def perfect3(e):
  global u
  n = (2**(e-1))*((2**e)-1)
  if n < ((2**63)-1):
    return n
  else:
    u = False
    return u

perfectnumber1 = int(input("Enter first perfect number:"))
print(perfect1(perfectnumber1))


u = True
for k in primelist:
  if u == True:
    print(perfect3(k))
  
