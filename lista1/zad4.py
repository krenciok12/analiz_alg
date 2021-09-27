from scen_III import sym_n_u
import math

n = int(input())
u = int(input())



logu = math.ceil(math.log(u,2))
result=0
for i in range(10000):
    s=sym_n_u(n,u)
    if (s/logu<=1):
        result+=1
print("P= ",result/10000)
