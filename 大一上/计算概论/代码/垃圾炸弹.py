d=int(input())
n=int(input())
a=[[0 for _ in range(1025)]for _ in range(1025)]
di={}
for _ in range(n):
    shuru=list(map(int,input().split()))
    di[(shuru[0],shuru[1])]=shuru[2]
    a[shuru[0]][shuru[1]]=shuru[2]
for x,y in di.keys():
    for i in range(max(0,x-d),min(1024,x+d)+1):
        for j in range(max(0,y-d),min(1024,y+d)+1):
            if i==x and j==y:
                continue
            a[i][j]+=a[x][y]
s,f=0,0
for i in range(1025):
    s0=max(a[i])
    if s<s0:
        s=s0
        f=a[i].count(s)
    elif s==s0:
        f+=a[i].count(s)
print(f,s)