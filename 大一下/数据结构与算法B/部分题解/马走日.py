# pylint: skip-file
t=int(input())
di=[(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
def ri(x,y,cnt):
    global ma,n,m,ans
    if cnt==n*m:
        ans+=1
        return
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and ma[nx][ny]:
            ma[nx][ny]=0
            ri(nx,ny,cnt+1)
            ma[nx][ny]=1
    return
for _ in range(t):
    n,m,x,y=map(int,input().split())
    ans=0
    ma=[[1 for j in range(m)] for i in range(n)]
    ma[x][y]=0
    ri(x,y,1)
    print(ans)