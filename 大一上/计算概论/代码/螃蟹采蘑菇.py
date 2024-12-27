n=int(input())
from collections import deque
di=[(1,0),(0,1),(-1,0),(0,-1)]
ma=[]
sx1,sy1=-1,-1
for i in range(n):
    shuru=list(map(int,input().split()))
    if 9 in shuru:
        ex=i
        ey=shuru.index(9)
        shuru[ey]=0
    if 5 in shuru:
        for j in range(n):
            if shuru[j]==5:
                if sx1!=-1:
                    sx2 = i
                    sy2 = j
                    shuru[sy2]=0
                else:
                    sx1 = i
                    sy1=j
                    shuru[sy1]=0
    ma.append(shuru)
queue=deque()
v=[[1 for _ in range(n)]for _ in range(n)]
queue.append((sx1,sy1,sx2,sy2))
while queue:
    x,y,p,q=queue.popleft()
    if (x==ex and y==ey) or (p==ex and q==ey):
        print('yes')
        exit()
    for dx,dy in di:
        nx,ny,np,nq=x+dx,y+dy,p+dx,q+dy
        if 0<=nx<n and 0<=ny<n and 0<=np<n and 0<=nq<n and not ma[nx][ny] and not ma[np][nq] and v[nx][ny]:
            queue.append((nx,ny,np,nq))
            v[nx][ny]=0
print('no')