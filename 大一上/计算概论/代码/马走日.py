directions=[[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
def dfs(n,m,x,y,ma,step,p):
    if step==n*m:
        p[0]+=1
        return
    for dx,dy in directions:
        if -1<x+dx<n and -1<y+dy<m and ma[x+dx][y+dy]:
            ma[x+dx][y+dy]=0
            dfs(n,m,x+dx,y+dy,ma,step+1,p)
            ma[x+dx][y+dy]=1
case=int(input())
for _ in range(case):
    n,m,x,y=map(int,input().split())
    ma=[[1 for _ in range(m)] for _ in range(n)]
    ma[x][y]=0
    p=[0]
    dfs(n,m,x,y,ma,1,p)
    print(p[0])
