def MinCount(Multi,h,k,max):
    M = []
    for i in range(k):
        M.append(max)
    for i in Multi:
        t = (h(i))
        if t<M[k-1] and not t in M:
            M[k-1]=t
            M.sort()
    if M[k-1]==max:
        j=k-2
        while M[j]==max:
            j=j-1
        return j+1
    else:
        return (k-1)/M[k-1]*max
