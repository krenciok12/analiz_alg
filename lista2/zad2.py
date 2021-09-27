from minCount import MinCount
import random
import numpy
import math

n = 10000
k = 400

b = int(input())


with open("tekst2.txt") as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]
    #print(max((hash(i)) for i in L))


def h1(s):
    res="{:063b}".format(abs(hash(s)))
    res=int(res[:b],2)
    return res;

t = []
for i in range(1000):
    random.shuffle(L)
    tab = L[:n]
    t.append(MinCount(tab,h1,k,pow(2,b)))

print(numpy.var(t))
print(numpy.mean(t))
