from unique_sum import Unique_sum
import math
import matplotlib.pyplot as plt
import random

def h1(s):
    res="{:063b}".format(abs(hash(s)))
    #res=int(res[:32],2)
    return int(res[:32],2)/(math.pow(2,32));

def Czebyszew(m,alfa):
    return math.sqrt(1/(m-2)/alfa)

n=1000
n2=100
m=1000
a=1
b=10
alfa=0.1

ZM=[]
RES=[]
SUM=[]

k=0

czeb=Czebyszew(m,alfa)
print(czeb)

for i in range(1,n+1):
    m1=[]
    s=0
    for j in range(i):
        r = random.uniform(a,b)
        m1.append([k,r])
        s+=+r
        k+=1
    #m1.append([k,900])
    #k+=1
    ZM.append(m1)
    SUM.append(s)

k=1
K=[]
for i in range(n):
    RES.append(Unique_sum(ZM[i],h1,m)/SUM[i])
    K.append(k)
    k+=1

czeb=Czebyszew(m,alfa)

s=[1 for i in range(1000)]
plt.scatter(K,RES,s=s)
plt.plot(K,[1+czeb for i in range(n)],'r')
plt.plot(K,[1-czeb for i in range(n)],'r')
#plt.bar(K,RES)
plt.show()
