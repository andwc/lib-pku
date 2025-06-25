r,c=map(int,input().split())
ma=[]
for i in range(r):
    ma.append(list(map(int,input().split())))
dp=[[0 for _ in range(c)]for _ in range(r)]
di=[(0,1),(1,0),(-1,0),(0,-1)]
def dfs(x,y):
    global dp,ma,di,r,c
    if dp[x][y]!=0:
        return dp[x][y]
    ans=1
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and ma[x][y]>ma[nx][ny]:
            ans=max(ans,1+dfs(nx,ny))
    dp[x][y]=ans
    return ans
for i in range(r):
    for j in range(c):
        dfs(i,j)
ans=1
for i in dp:
    ans=max(ans,max(i))
    #print(i)
print(ans)