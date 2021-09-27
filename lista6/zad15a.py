import random

k = 0;

def f(n):
    global k
    k+=1
    s=0
    if n<2:
        return 1
    else:
        for i in range(1,n+1):
            if random.randint(0,1)==0:
                s+=f(i)
        return s

n = int(input())
K = []
for i in range(100000):
    f(n)
    K.append(k)
    k=0

print(sum(K)/100000)
#print(k)
