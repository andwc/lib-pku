import sys
sys.setrecursionlimit(1000000)
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y,h):
    global n,m,ditu
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if -1<nx<m and -1<ny<n:
            if h>ditu[nx][ny]:
                ditu[nx][ny]=h
                judge[nx][ny]=True
                dfs(nx,ny,ditu[nx][ny])
            elif ditu[nx][ny]==h and not judge[nx][ny]:
                judge[nx][ny]=True
                dfs(nx,ny,ditu[nx][ny])
shuru=list(map(int,sys.stdin.read().split()))
case=shuru[0]
index=0
for _ in range(case):
    m,n=shuru[index+1],shuru[index+2]
    ditu=[[0 for _ in range(n)]for _ in range(m)]
    for ki in range(m):
        for kj in range(n):
            ditu[ki][kj]=shuru[index+ki*n+kj+3]
    i,j=shuru[index+3+n*m],shuru[index+4+m*n]
    i,j=i-1,j-1
    p=shuru[index+5+n*m]
    judge=[[False for _ in range(n)]for _ in range(m)]
    oh=ditu[i][j]
    for k in range(p):
        x,y=shuru[index+6+n*m+2*k],shuru[index+7+m*n+2*k]
        x,y=x-1,y-1
        judge[x][y]=True
        dfs(x,y,ditu[x][y])
    print('Yes' if oh<ditu[i][j] else 'No')
    index+=5+n*m+2*p