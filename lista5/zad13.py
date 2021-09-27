import queue

def is_independent(i, s , N):
    if (s[i]==0):
        return False
    for it in N[i]:
        if s[it]==1:
            return False

    return True

def is_dominated(i, s , N):
    if (s[i]==1):
        return False
    for it in N[i]:
        if s[it]==1:
            return True
    return False

def can_do_independent(i, s , N):
    if (s[i]==1):
        return False
    for it in N[i]:
        if s[it]==1:
            return False
    return True

def can_do_dominated(i, s , N):
    if (s[i]==0):
        return False
    for it in N[i]:
        if s[it]==1:
            return True
    return False

n = 8
N = [[1,2,6],[0,3,7],[0,3,4],[1,2,5],[2,5,6],[3,4,7],[0,4,7],[1,5,6]]
s = [1,1,1,1,0,0,0,0]
X = queue.Queue()
K = queue.Queue()
X.put(s)
K.put([])
Res = []


while not X.empty():
    s1 = X.get()
    k1 = K.get()
    j=0
    for i in range(n):
        if not (is_independent(i,s1,N) or is_dominated(i,s1,N)):
            break;
        j+=1
    if j==n:
        Res.append([s1,k1])
        continue;

    for i in range(n):
        s2 = []
        s2.extend(s1)
        k2 = []
        k2.extend(k1)
        if can_do_dominated(i,s2,N):
            s2[i] = 0
            k2.append((i,0,s2))
            X.put(s2)
            K.put(k2)
        if can_do_independent(i,s2,N):
            s2[i] = 1
            k2.append((i,1,s2))
            X.put(s2)
            K.put(k2)


l=0
naj = []
b = []
for it in Res:
    if not it[0] in b:
        b.append(it[0])
    if len(it[1])>l:
        naj = it
        l = len(it[1])


print(naj)
print(b)
