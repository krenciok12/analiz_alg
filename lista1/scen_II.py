import random

def sym_n(n):
    single = False
    result=0
    while not single:
        l=0
        for j in range(n):
            rand = random.randrange(n)
            if (rand == 0):
                l+=1
        if (l == 1):
            single=True
        result+=1

    return result
