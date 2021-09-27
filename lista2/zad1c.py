from minCount import MinCount
import random
import numpy
import math

n = 10000
k=400

with open("tekst2.txt") as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]
    #print(max((hash(i)) for i in L))


def h1(s):
    return abs(hash(s))%math.pow(2,32);

t = []
#for k in range(10,401,10):
p=0
for i in range(100):
    random.shuffle(L)
    tab = L[:n]
    s=MinCount(tab,h1,k,pow(2,32))/n
    if abs(s-1)<0.1:
        p+=1
t.append(p)


print(t)
