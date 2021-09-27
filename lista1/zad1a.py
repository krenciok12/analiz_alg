import scen_III
import numpy
import math

n = int(input())
u = int(input())
logu = math.ceil(math.log(u,2))+1
result = 0
result2 = 0
result3 = 0

for i in range(10000):
    s=s1.scen_n_u(n,u)
    result+=s
    #print("wynik ",s)
    l=(int(s/logu) + 1)
    result2+=l
    if (l==1):
        result3+=1


print(result/10000)
print(result2/10000)
print(result3/10000)
