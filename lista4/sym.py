import math
import random

def func(n,q):
    p=1-q

    qn=0
    pn=0
    j=0

    for i in range(n):
        if(random.uniform(0,1)<=p):
            pn+=1
        if(random.uniform(0,1)<=q):
            qn+=1
    if pn<=qn:
        return 1

    for i in range(200-n):
        if(random.uniform(0,1)<=p):
            pn+=1
        if(random.uniform(0,1)<=q):
            qn+=1
        if pn==qn:
            return 1
    return 0;
