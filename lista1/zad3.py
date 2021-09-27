from scen_II import sym_n
import numpy

n = int(input('Podaj n: '))
result = 0
tab = []
for i in range(10000):
    s=sym_n(n)
    result+=s
    tab.append(s)

print("E[L]=",numpy.mean(tab))
print("Var[L]=",numpy.var(tab))
