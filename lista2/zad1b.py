from minCount import MinCount
import random
import numpy
import math
import matplotlib.pyplot as plt

k = int(input())

with open("tekst2.txt") as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]
    #print(max((hash(i)) for i in L))


def h1(s):
    res="{:063b}".format(abs(hash(s)))
    res=int(res[:32],2)
    return res;

t = []
x = []
for i in range(10000):
    random.shuffle(L)
    x.append(i+1)
    tab = L[:i+1]
    t.append(MinCount(tab,h1,k,pow(2,32))/(i+1))

plt.bar(x,t)
plt.show()

t.sort()
print(numpy.var(t))
print(numpy.mean(t))
