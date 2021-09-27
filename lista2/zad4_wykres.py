import math
import random
import numpy
import math
import matplotlib.pyplot as plt

nazwa_pliku = input()

n=10000
alfa=[0.05,0.01, 0.005]

with open(nazwa_pliku) as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]

x=[]
tab=[]
alf=[]

for i in range(n):
    x.append(i+1)
    res=float(L[i])
    tab.append(res)
    alf.append(abs(res-1))

alf.sort()
aa=[alf[int(n*(1-a))] for a in alfa]
print(aa)

s=[1 for i in range(n*10)]
plt.scatter(x,tab,s=s)
plt.plot(range(n),[(1-aa[0]) for i in range(1,n+1)],'r')
plt.plot(range(n),[(1+aa[0]) for i in range(1,n+1)],'r')
plt.plot(range(n),[(1-aa[1]) for i in range(1,n+1)],'y')
plt.plot(range(n),[(1+aa[1]) for i in range(1,n+1)],'y')
plt.plot(range(n),[(1-aa[2]) for i in range(1,n+1)],'g')
plt.plot(range(n),[(1+aa[2]) for i in range(1,n+1)],'g')
plt.show()
