from hll import HyperLogLog
import random
import numpy
import matplotlib.pyplot as plt

def h1(s):
        res="{:063b}".format(abs(hash(s)))
        res=(res[:37])
        return res

n = 1000

al = int(input())
nazwa_pliku = input()

alfa={16:0.673, 32:0.697, 64:0.709}

outF = open(nazwa_pliku, "w")

with open("tekst2.txt") as fp:
    L=fp.readlines()
    L=[i[:len(i)-1] for i in L]


t = []

for i in range(10000):
    random.shuffle(L)
    tab = L[:n]
    new = HyperLogLog(tab,h1,alfa[al],al)/n
    t.append(new)
    outF.write(str(new))
    outF.write("\n")


print(numpy.var(t))
print(numpy.mean(t))
