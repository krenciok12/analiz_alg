import math
import random


def sym_n_u(n,u):
    single = False
    slot = 0

    logu = math.ceil(math.log(u,2))

    while not single:
        k=1
        for i in range (logu):
            slot+=1
            k=k*2
            l=0
            for j in range(n):
                rand = random.randrange(k)
                if (rand == 0):
                    l+=1
            if (l==1):
                single=True
                break
    return slot
