import math
import random

def Nakamoto_an(n,q):
    p=1-q
    delta = n*q/p

    dt = [1]
    qt = [q/p]
    kt = [1]
    for i in range(1,n):
        dt.append(dt[i-1]*delta)
        kt.append(kt[i-1]*i)
        qt.append(qt[i-1]*q/p)

    return 1- math.pow(math.e,-delta)*sum(dt[i]/kt[i]*(1-qt[n-1-i]) for i in range(0,n) )

def Grunspan_an(n,q):
    p=1-q

    nt = [1]
    kt = [1]
    qt = [1]
    pt = [1]
    for i in range(1,n):
        pt.append(pt[i-1]*p)
        qt.append(qt[i-1]*q)
        kt.append(kt[i-1]*i)
        nt.append(nt[i-1]*(n-1+i))

    pn=pt[n-1]*p
    qn=qt[n-1]*q

    return 1- sum((pn*qt[i]-qn*pt[i])*(nt[i]/kt[i]) for i in range(0,n) )
