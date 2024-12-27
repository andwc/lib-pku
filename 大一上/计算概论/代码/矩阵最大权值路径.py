import copy
def dfs(x,y,visited,he):
    global n,m,ma,zuidazhi,v
    if x==n-1 and y==m-1:
        if zuidazhi<he+ma[-1][-1]:
            zuidazhi=he+ma[-1][-1]
            #print(he+ma[-1][-1])
            v=copy.copy(visited)
        return
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if -1<nx<n and -1<ny<m and (nx,ny) not in visited:
            visited.append((nx,ny))
            dfs(nx,ny,visited,he+ma[x][y])
            visited.remove((nx,ny))
    return
n,m=map(int,input().split())
ma=[]
directions=[(1,0),(0,1),(-1,0),(0,-1)]
zuidazhi=float('-inf')
v=[]
for _ in range(n):
    ma.append(list(map(int,input().split())))
dfs(0,0,[(0,0)],0)
for i,j in v:
    print(i+1,j+1)