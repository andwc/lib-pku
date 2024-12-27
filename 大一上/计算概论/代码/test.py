from collections import deque
n=int(input())
ma=[]
for i in range(n):
    shuru=list(map(int,input().split()))
    ma.append(shuru)
queue=deque([(0,1,0,0)])
directions=[(0,1),(1,0)]
visited=set()
step=0
while queue:
    for i in range(len(queue)):
        x, y, xx, yy = queue.popleft()
        if x==n-1 and y==n-1 and xx==n-1 and yy==n-2:
            print(step)
            exit()
        for dx, dy in directions:
            nx, ny, nxx, nyy = x + dx, y + dy, xx + dx, yy + dy
            if 0 <= nx < n and 0 <= ny < n and 0 <= nxx < n and 0 <= nyy < n and ma[nx][ny]!=1 and ma[nxx][nyy]!=1 and (nx, ny, nxx, nyy) not in visited:
                visited.add((nx, ny, nxx, nyy))
                queue.append((nx, ny, nxx, nyy))
        if y==yy+1 and x+1<n  and not ma[x+1][y] and not ma[xx+1][yy]:
            nx=x+1;ny=y-1;nxx=xx;nyy=yy
            if (nx,ny,nxx,nyy) not in visited:
                visited.add((nx, ny, nxx, nyy))
                queue.append((nx, ny, nxx, nyy))
        if x == xx + 1 and y+1<n and not ma[x][y+1] and not ma[xx][yy+1]:
            nx = x -1
            ny = y+1
            nxx = xx
            nyy = yy
            if (nx,ny,nxx,nyy) not in visited:
                visited.add((nx, ny, nxx, nyy))
                queue.append((nx, ny, nxx, nyy))
    step+=1
print(-1)