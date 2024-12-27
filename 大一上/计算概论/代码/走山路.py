import heapq
directions=[[1,0],[0,1],[-1,0],[0,-1]]
m, n, p = map(int, input().split())
ditu = []
for i in range(m):
    ditu.append(list(map(str, input().split())))
for _ in range(p):
    sx, sy, ex, ey = map(int, input().split())
    tl=[[float('inf')]*n for _ in range(m)]
    tl[sx][sy]=0
    queue = []
    if ditu[sx][sy]=='#' or ditu[ex][ey]=='#':
        print('NO')
        continue
    heapq.heappush(queue,(0,sx, sy))
    while queue:
        t, x, y= heapq.heappop(queue)
        if x==ex and y==ey:
            print(t)
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and ditu[nx][ny] != '#':
                tili=tl[x][y]+abs(int(ditu[nx][ny])-int(ditu[x][y]))
                if tili<tl[nx][ny]:
                    tl[nx][ny]=tili
                    heapq.heappush(queue,(tl[nx][ny],nx, ny))
    else:
        print('NO')