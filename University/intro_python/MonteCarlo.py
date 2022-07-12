import random
import math
import matplotlib.pyplot as plt
import numpy as np

#number of random points
N=1000
#radious of circle x 2=length of one side of the square
r=1.0

hits=[]
miss=[]

def is_in_circle(radious,x,y):
    return math.sqrt(x**2+y**2) < math.sqrt(radious**2)
#Return the next random floating point number in the range [0.0, 1.0).
hit=0
for _ in range(N):
    x= random.uniform(-r,r)
    y = random.uniform(-r,r)

    if is_in_circle(r,x,y):
        hit+=1
        hits.append([x, y])
    else:
        miss.append([x, y])


print("Pi: ", math.pi )
print("Approx:", float( hit/N)* 4 )


fig, ax = plt.subplots()
c1=plt.Circle((0.0,0.0),radius=r,facecolor='black', edgecolor='black',alpha=0.1)
hits,miss=np.array(hits),np.array(miss)
ax.add_artist(c1)
ax.scatter(hits[:,0],hits[:,1],c='r')
ax.scatter(miss[:,0],miss[:,1],c='b')
ax.set_xlim((-r, r))
ax.set_ylim((-r, r))
plt.show()
