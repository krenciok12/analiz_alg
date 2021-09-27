import math


def Unique_sum(Multi,h,m):
    M=[]
    for i in range(m):
        M.append(math.inf)

    for el in Multi:
        for k in range(m):
            u = h(str(el[0]).encode('utf-8')+str(k+1).encode('utf-8'))
            M[k] = min(M[k],-math.log(u)/el[1])

    return (m-1)/(sum(M))


def Unique_av(Multi,h,m):
    M=[]
    M2=[]
    for i in range(m):
        M.append(math.inf)
        M2.append(math.inf)

    for el in Multi:
        for k in range(m):
            u = h(str(el[0]).encode('utf-8')+str(k+1).encode('utf-8'))
            u2 = h(str(k+1).encode('utf-8')+str(el[0]).encode('utf-8'))
            M[k] = min(M[k],-math.log(u)/el[1])
            M2[k] = min(M2[k],-math.log(u2))

    return (sum(M2))/(sum(M))
