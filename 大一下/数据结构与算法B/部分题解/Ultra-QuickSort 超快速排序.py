def qs(p):
    if not p:
        return 0
    if len(p)==1:
        return 0
    if len(p)==2:
        if p[0]<p[1]:
            return 0
        else:
            return 1
    x=[]
    d=[]
    size=0
    mid=p[0]
    for i in range(len(p)):
        if p[i]>mid:
            d.append(p[i])
        elif p[i]<mid:
            x.append(p[i])
            size+=(i-len(x)+1)
    return size+qs(x)+qs(d)
while True:
    n=int(input())
    if n==0:
        break
    p=[]
    for i in range(n):
        p.append(int(input()))
    ans=qs(p)
    print(ans)