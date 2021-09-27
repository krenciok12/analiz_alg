from formuly import Nakamoto_an
from formuly import Grunspan_an
import matplotlib.pyplot as plt

alfa = float(input("wprowadz alfa: "))

nak=[]
gru=[]
Q = []
q=0.01
for i in range(40):
    n=1
    s1=Nakamoto_an(n,q*(i+1))
    while s1>alfa:
        n+=1
        s1=Nakamoto_an(n,q*(i+1))
    nak.append(n)
    Q.append(q*(i+1))

for i in range(40):
    n=1
    s1=Grunspan_an(n,q*(i+1))
    while s1>alfa:
        n+=1
        s1=Grunspan_an(n,q*(i+1))
    gru.append(n)


plt.plot(Q,nak,'r')
plt.plot(Q,gru,'b')

plt.show()
