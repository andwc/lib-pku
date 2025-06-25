di={(0,1),(1,0),(-1,0),(0,-1)}
from collections import deque
case=int(input())
for _ in range(case):
    r,c=map(int,input().split())
    visited=[[False]*c for _ in range(r)]
    ma=[]
    for i in range(r):
        s=input()
        ma.append(s)
        if 'E' in s:
            ex=i
            ey=s.index('E')
        if 'S' in s:
            sx=i
            sy=s.index('S')
    q=deque()
    visited[sx][sy]=True
    q.append((sx,sy))
    step=0
    judge=1
    while q and judge:
        step+=1
        for _ in range(len(q)):
            if not judge:
                break
            x,y=q.popleft()
            for dx,dy in di:
                nx,ny=x+dx,y+dy
                if nx==ex and ny==ey:
                    print(step)
                    judge=0
                    break
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and not visited[nx][ny] and ma[nx][ny]=='.':
                    visited[nx][ny]=True
                    q.append((nx,ny))
    if judge:
        print('oop!')