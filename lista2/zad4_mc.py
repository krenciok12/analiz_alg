from hll import HyperLogLog
from minCount import MinCount
import random
import numpy
import matplotlib.pyplot as plt

b = int(input())

def h1(s):
    res="{:063b}".format(abs(hash(s)))
    res=int(res[:b],2)
    return res;

n = 1000
k = b

outF = open("4_mc_wyniki.txt", "w")

with open("tekst2.txt") as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]


t = []
x = []
for i in range(10000):
    random.shuffle(L)
    x.append(i+1)
    tab = L[:n]
    new = MinCount(tab,h1,k,pow(2,b))/n
    t.append(new)
    outF.write(str(new))
    outF.write("\n")

plt.bar(x,t)
plt.show()

print(numpy.var(t))
print(numpy.mean(t))
