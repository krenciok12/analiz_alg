import queue
import time

def the_same(x,n):
    for i in range(1,n):
        if x[i]!=x[0]:
            return False
    return True



n = int(input())
tab_x = [[]]
for i in range(n):
    tmp = []
    for it in tab_x:
        for i in range(n+1):
            tmp.append(it + [i])
    tab_x=tmp

mx = 0
k = 0
naj = []
start = time.time()
for x in tab_x:
    X = queue.Queue()
    K = queue.Queue()
    X.put(x)
    K.put([])
    Res = []

    while not X.empty():
        x1 = X.get()
        k1 = K.get()

        if (the_same(x1,n)):
            Res.append([x,k1])
            k+=1
            continue;
        x2 = []
        x2.extend(x1)
        k2 = []
        k2.extend(k1)
        if (x1[0]==x1[n-1]):
            x2[0] = (x2[0] + 1) % (n+1)
            k2.append((0,x2))
            X.put(x2)
            K.put(k2)

        for i in range(1,n):
            x2 = []
            x2.extend(x1)
            k2 = []
            k2.extend(k1)
            if (x1[i]!=x1[i-1]):
                x2[i] = x2[i-1]
                k2.append((i,x2))
                X.put(x2)
                K.put(k2)


    l = len(Res[len(Res)-1][1])
    if l>mx:
        mx = l
        naj = Res[len(Res)-1]
    #print(x, l)
    #print(mx)

end = time.time()
print(end-start)
print(naj)
print(k)
print(mx)
#for it in Res:
    #print(it[0],len(it[1]))
