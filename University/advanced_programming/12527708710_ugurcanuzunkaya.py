def findpi(x,firstterm):
    for i in range(1,x+1):
        firstterm = firstterm + (4*((-1)**(i-1))/((2*i)*(2*i+1)*(2*i+2)))
    return firstterm

print(findpi(15,3))

def factorial(y):
    a = 1
    t = 1
    if y == 0:
        return t
    else:
        while a<=y:
            t = t*a
            a = a + 1
        return t

print(factorial(0))