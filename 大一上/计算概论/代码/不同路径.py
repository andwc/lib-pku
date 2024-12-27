def dfs(x,y):
    global ma,n,m,ans
    if x==n-1 and y==m-1:
        ans+=1
        return
    for dx,dy in directions:
        if -1<x+dx<n and -1<y+dy<m:
            dfs(x+dx,y+dy)

n,m=map(int,input().split())
ma=[[0 for _ in range(m)]for _ in range(n)]
directions=[(1,0),(0,1)]
ans=0
dfs(0,0)
print(ans)