from scen_II import sym_n
import numpy
from collections import Counter
import matplotlib.pyplot as plt
import math

n = int(input('Podaj n: '))

tab = []

for i in range(10000):
    s=sym_n(n)
    tab.append(s)

list = sorted(Counter(tab).items())

x=[]
y=[]

for it in list:
    x.append(it[0])
    y.append(it[1])

plt.bar(x,y)
plt.show()
