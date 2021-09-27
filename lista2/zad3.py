import math
from minCount import MinCount
import random
import numpy
import math
import matplotlib.pyplot as plt



def Chernoff(n, s):
    return math.pow((math.pow(math.e,-s))/(math.pow(1-s,1-s)),n)

def Czebyszew(n,k,a):
    return 1 - ((n*(n-k+1))/(k-2))/math.pow(a,2)

nazwa_pliku = input()


n = 10000
k = 32
l = 10
alfa = 0.01

outF = open(nazwa_pliku, "w")

with open("tekst2.txt") as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]
    #print(max((hash(i)) for i in L))


def h1(s):
    return abs(hash(s))%math.pow(2,32);

t = []
x = []
t_alf = []
for i in range(n):
    for j in range(l):
        random.shuffle(L)
        x.append(i+1)
        tab = L[:i+1]
        new=MinCount(tab,h1,k,pow(2,32))
        t.append(new)
        t_alf.append(abs(new/(i+1)-1))
        outF.write(str(new))
        outF.write("\n")


t_alf.sort()
k=t_alf[int(n*l*(1-alfa))]
print(k)

outF.close()

s=[1 for i in range(n*10)]
plt.scatter(x,t,s=s)
plt.plot(range(n),[i*(1-k) for i in range(n)],'r')
plt.plot(range(n),[i*(1+k) for i in range(n)],'r')
plt.plot(range(n),range(n),'r')
plt.show()
