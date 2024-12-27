n=int(input())
ma=[]
for _ in range(n):
    ma.append(list(map(int,input().split())))
ceng=n//2+n%2
ans=0
for c in range(ceng):
    s=ma[c][c]
    x,y=c,c
    while x<n-c-1:
        x+=1
        s+=ma[x][y]
    while y<n-c-1:
        y+=1
        s+=ma[x][y]
    while c<x:
        x-=1
        s+=ma[x][y]
    while c+1<y:
        y-=1
        s+=ma[x][y]
    ans=max(ans,s)
print(ans)