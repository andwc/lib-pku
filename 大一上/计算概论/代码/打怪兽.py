ncase=int(input())
for _ in range(ncase):
    t=[]
    x=[]
    n,m,b=map(int,input().split())
    for i in range(n):
        ti,xi=map(int,input().split())
        t.append(ti)
        x.append(xi)
    ts=sorted(t)
    t0=-1
    xue=0
    for i in ts:
        if i!=t0:
            t0=i
            for j in range(m):
                xue = 0
                index=0
                for k in range(n):
                    if t[k] == i:
                        if xue<=x[k]:
                            xue = x[k]
                            index=k
                b-=xue
                x[index]=0
            #print(t0,b)
            if b<=0:
                break
    if b<=0:
        print(t0)
    else:
        print('alive')