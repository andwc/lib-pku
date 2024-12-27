from collections import deque
di=[(1,0),(0,1),(-1,0),(0,-1)]
T=int(input())
def keyi(nx,ny):
    global n,m,k
    return 0<=nx<n and 0<=ny<m and ((ma[nx][ny]=='#' and (t+1)%k==0) or ma[nx][ny]!='#')
for _ in range(T):
    n,m,k=map(int,input().split())
    ma=[]
    for i in range(n):
        shuru=input()
        if 'S' in shuru:
            sx=i
            sy=shuru.index('S')
        if 'E' in shuru:
            ex=i
            ey=shuru.index('E')
        ma.append(shuru)
    queue=deque([(sx,sy,0)])
    visited=set()
    visited.add((sx,sy,0))
    v=[[False]*m for _ in range(n)]
    judge=1
    while queue and judge:
        for _ in range(len(queue)):
            (x,y,t)=queue.popleft()
            if x==ex and y==ey:
                print(t)
                judge=0
                break
            for dx,dy in di:
                nx,ny=x+dx,y+dy
                if keyi(nx,ny) and (nx,ny,t+1) not in queue and not v[nx][ny]:
                    if t%k==0 and (nx,ny,t+1-k) in visited:
                        v[nx][ny]=True
                        continue
                    queue.append((nx,ny,t+1))
                    visited.add((nx,ny,t+1))
    if judge:
        print('Oop!')