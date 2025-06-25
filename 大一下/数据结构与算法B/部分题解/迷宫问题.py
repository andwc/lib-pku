from collections import deque
di=[(1,0),(-1,0),(0,1),(0,-1)]
n,m=map(int,input().split())
ma=[]
for i in range(n):
    ma.append(list(map(int,input().split())))
visited=set()
q=deque()
q.append((0,0))
visited.add((0,0))
step=-1
while q:
    step+=1
    for i in range(len(q)):
        x,y=q.popleft()
        if x==n-1 and y==m-1:
            print(step)
            exit()
        for dx,dy in di:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not ma[nx][ny] and (nx,ny) not in visited:
                q.append((nx,ny))
                visited.add((nx,ny))
print(-1)