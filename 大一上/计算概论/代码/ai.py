di=[(1,0),(0,1),(-1,0),(0,-1)]
from sys import setrecursionlimit
setrecursionlimit(10000)
m,n=map(int,input().split())
ma=[]
for i in range(m):
    ma.append(list(map(int,input().split())))
dp=[[0 for i in range(n)]for j in range(m)]
def dfs(x,y):
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<m and 0<=ny<n and ma[x][y]<ma[nx][ny]:
            if dp[nx][ny]>=dp[x][y]+1:
                continue
            else:
                dp[nx][ny]=dp[x][y]+1
            dfs(nx,ny)
for i in range(m):
    for j in range(n):
        if not dp[i][j]:
            dfs(i,j)
ans=0
for i in dp:
    ans=max(ans,max(i))
    #print(i)
print(ans+1)