from minCount import MinCount
import random
import numpy
import math

n = int(input())
powt = int(input())
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
for i in range(100):
    random.shuffle(L)
    tab = L[:n-powt]
    tab = tab + tab[:powt]
    t.append(MinCount(tab,h1,k,pow(2,32)))

t.sort()
print(numpy.var(t))
print(numpy.mean(t))
