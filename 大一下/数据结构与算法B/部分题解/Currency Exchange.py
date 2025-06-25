n,m,s,v=input().split()
n,m,s,v=int(n),int(m),int(s)-1,float(v)
e=[]
for i in range(m):
    a,b,c,d,ee,f=input().split()
    a,b,c,d,ee,f=int(a)-1,int(b)-1,float(c),float(d),float(ee),float(f)
    e.append((a,b,c,d))
    e.append((b,a,ee,f))
d=[float('-inf')]*n
d[s]=v
ans=1
for _ in range(n):
    judge=0
    for a,b,c,dd in e:
        if (d[a]-dd)*c>d[b]:
            d[b]=(d[a]-dd)*c
            judge=1
    if not judge:
        ans=0
        break
print('YES') if ans else print('NO')