import sys
shuru=list(map(int,sys.stdin.read().split()))
index=0
case=shuru[index]
index+=1
for _ in range(case):
    m=shuru[index]
    index+=1
    n=shuru[index]
    index+=1
    ma=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            ma[i][j]=shuru[index]
            index+=1
    sx=shuru[index]-1
    index+=1
    sy=shuru[index]-1
    index+=1
    p=shuru[index]
    index+=1
    shui=[]
    for _ in range(p):
        x=shuru[index]-1
        index+=1
        y=shuru[index]-1
        index+=1
        shui.append((x,y))
    shui.sort(key=lambda x:-ma[x[0]][x[1]])
    # input complicated
    di=[[0,1],[1,0],[0,-1],[-1,0]]
    def bfs(xx,yy):
        from collections import deque
        global shui,di,ma,sx,sy
        q=deque()
        visited=set()
        q.append((xx,yy))
        visited.add((xx,yy))
        water=ma[xx][yy]
        while q:
            x,y=q.popleft()
            for dx,dy in di:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and ma[nx][ny]<=water and (nx,ny) not in visited:
                    if nx==sx and ny==sy and ma[nx][ny]<water:
                        return True
                    q.append((nx,ny))
                    visited.add((nx,ny))
                    ma[nx][ny]=water
        return False
    for i in range(p):
        xx,yy=shui[i]
        if bfs(xx,yy):
            print('Yes')
            break
    else:
        print('No')