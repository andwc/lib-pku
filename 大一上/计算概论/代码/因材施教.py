n,m=map(int,input().split())
p=list(map(int,input().split()))
d=0
p.sort()
cha=[]
cha.append(0)
for i in range(1,n):
    cha.append(p[i]-p[i-1])
cha.sort()
ans=0
for i in range(n-m+1):
    ans+=cha[i]
print(ans)