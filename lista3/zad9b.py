from unique_sum import Unique_sum
import math
import matplotlib.pyplot as plt
import random


def h1(s):
    res="{:063b}".format(abs(hash(s)))
    #res=int(res[:32],2)
    return int(res[:32],2)/(math.pow(2,32));

n=1000
n2=100
m=100
a=1
b=5

ZM=[]
RES=[]
SUM=[]
k=0
for i in range(1,n+1):
    m1=[]
    s=0
    for j in range(n2-1):
        r = random.uniform(a,b)
        m1.append([k,r])
        s+=r
        k+=1
    m1.append([k,2000])
    k+=1
    ZM.append(m1)
    SUM.append(s+900)

k=1
K=[]
for i in range(n):
    RES.append(Unique_sum(ZM[i],h1,m)/SUM[i])
    K.append(k)
    k+=1


s=[1 for i in range(n2)]
#plt.scatter(K,RES,s=s)
plt.bar(K,RES)
plt.show()
