from unique_sum import Unique_av
import math
import matplotlib.pyplot as plt
import random
from zlib import crc32

def h2(b):
    return float(crc32(b) & 0xffffffff) / math.pow(2,32)

def h1(s):
    res="{:063b}".format(abs(hash(s)))
    #res=int(res[:32],2)
    return int(res[:32],2)/(math.pow(2,32));

n=1000
n2=100
m=100
a=3
b=10

ZM=[]
RES=[]
SUM=[]
k=0
for i in range(1,n+1):
    m1=[]
    s=0
    for j in range(i):
        r = random.randint(a,b)
        m1.append([k,r])
        s+=+r
        k+=1

    ZM.append(m1)
    SUM.append(s)

k=1
K=[]
for i in range(n):
    RES.append(Unique_av(ZM[i],h1,m)*(i+1)/SUM[i])
    K.append(k)
    k+=1


s=[1 for i in range(1000)]
#plt.scatter(K,RES,s=s)
plt.bar(K,RES)
plt.show()
