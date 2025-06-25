from collections import deque
q=deque()
di=[(1,0),(-1,0),(0,1),(0,-1)]
n,m=map(int,input().split())
ma=[]
for i in range(n):
    s=input()
    ma.append(s)
    if 'S' in s:
        sx=i
        sy=s.index('S')
    if 'T' in s:
        ex=i
        ey=s.index('T')
q.append((sx,sy))
v=set()
v.add((sx,sy))
step=0
while q:
    step+=1
    for i in range(len(q)):
        x,y=q.popleft()
        if x==ex and y==ey:
            print(step-1)
            exit()
        for dx,dy in di:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and ma[nx][ny]!='*' and (nx,ny) not in v:
                v.add((nx,ny))
                q.append((nx,ny))
print(-1)