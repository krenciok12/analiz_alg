
k = 0;

def f(n):
    global k
    s=0
    if n==0:
        return 1
    else:
        for i in range(n):
            k=k+1
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
