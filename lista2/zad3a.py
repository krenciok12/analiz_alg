import math
from minCount import MinCount
import random
import numpy
import math
import matplotlib.pyplot as plt


def Chernoff(n, alfa):
    return math.sqrt(-3/n*math.log(alfa/2,math.e))

def Czebyszew(n,k,alfa):
    return math.sqrt(n*(n-k+1)/(k-2)/alfa)

nazwa_pliku = input()

n=10000
alfa=0.005

with open(nazwa_pliku) as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]

x=[]
tab=[]
alf=[]

for i in range(n):
    for j in range(10):
        x.append(i+1)
        res=float(L[(i*10)+j])
        tab.append(res)
        alf.append(abs(res/(i+1)-1))

alf.sort()
aa=alf[int(n*10*(1-alfa))]
print(Czebyszew(n,400,alfa))

s=[1 for i in range(n*10)]
plt.scatter(x,tab,s=s)
#plt.plot(range(n),[(1-aa)*i for i in range(1,n+1)],'y')
#plt.plot(range(n),[(1+aa)*i for i in range(1,n+1)],'y')
plt.plot(range(400,n),[i-Czebyszew(i,400,alfa) for i in range(400,n)],'r')
plt.plot(range(400,n),[i+Czebyszew(i,400,alfa) for i in range(400,n)],'r')
#plt.plot(range(400,n),[(1-Chernoff(i,alfa))*i for i in range(400,n)],'g')
#plt.plot(range(400,n),[(1+Chernoff(i,alfa))*i for i in range(400,n)],'g')
plt.show()
