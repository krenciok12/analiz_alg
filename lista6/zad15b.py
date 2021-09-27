import random

k = 0;

def f(tab):
    global k
    k+=1
    s=0
    n=len(tab)
    if n==1:
        return
    else:
        for i in range(1,n+1):
            if random.randint(0,1)==0:
                t = random.sample(tab,i)
                f(t)
        return

n = int(input())
K = []
for i in range(100000):
    f(range(1,n+1))
    K.append(k)
    k=0

print(sum(K)/100000)
#print(k)
