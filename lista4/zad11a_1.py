from formuly import Nakamoto_an
from formuly import Grunspan_an
from sym import func
import matplotlib.pyplot as plt

n = int(input("wprowadz n: "))


nak=[]
gru=[]
proba=[]
Q = []
q=0.01
for i in range(46):
    nak.append(Nakamoto_an(n,q*(i+1)))
    gru.append(Grunspan_an(n,q*(i+1)))
    k=0
    k=0

    for j in range(10000):
        k+=func(n,q*(i+1))

    proba.append(k/10000)

    Q.append(q*(i+1))

plt.plot(Q,nak,'r')
plt.plot(Q,gru,'b')
plt.plot(Q,proba,'g')

plt.show()
