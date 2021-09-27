from scen_III import sym_n_u
import numpy
from collections import Counter
import matplotlib.pyplot as plt

n = int(input('Podaj n: '))
u = int(input('Podaj u: '))

tab = []

for i in range(10000):
    s=sym_n_u(n,u)
    tab.append(s)


list = sorted(Counter(tab).items())

x=[]
y=[]

for it in list:
    x.append(it[0])
    y.append(it[1])

plt.bar(x,y)
plt.show()
