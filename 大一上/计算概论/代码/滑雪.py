di=[(1,0),(0,1),(-1,0),(0,-1)]
from sys import setrecursionlimit
setrecursionlimit(10000)
m,n=map(int,input().split())
ma=[]
for i in range(m):
    ma.append(list(map(int,input().split())))
dp=[[0 for i in range(n)]for j in range(m)]
def dfs(x,y):
    if dp[x][y]:
        return dp[x][y]
    l=1
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and ma[x][y]<ma[nx][ny]:
            ll=dfs(nx,ny)+1
            l=max(l,ll)
    dp[x][y]=l
    return l
for i in range(m):
    for j in range(n):
        dfs(i,j)
ans=0
for i in dp:
    ans=max(ans,max(i))
print(ans)