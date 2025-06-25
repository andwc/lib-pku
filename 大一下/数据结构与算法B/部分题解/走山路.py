import heapq
di=[(0,1),(1,0),(-1,0),(0,-1)]
r,c,p=map(int,input().split())
ma=[]
for i in range(r):
    ma.append(list(input().split()))
for _ in range(p):
    sx,sy,ex,ey=map(int,input().split())
    if ma[sx][sy]=='#' or ma[ex][ey]=='#':
        print("NO")
        continue
    q=[]
    heapq.heappush(q,(0,sx,sy))
    visited=[[float('inf')]*c for _ in range(r)]
    visited[sx][sy]=0
    while q:
        s,x,y=heapq.heappop(q)
        if x==ex and y==ey:
            print(s)
            break
        for dx,dy in di:
            nx,ny=x+dx,y+dy
            if 0<=nx<r and 0<=ny<c and ma[nx][ny]!='#':
                tl=s+abs(int(ma[nx][ny])-int(ma[x][y]))
                if tl<visited[nx][ny]:
                    visited[nx][ny]=tl
                    heapq.heappush(q,(tl,nx,ny))
    else:
        print("NO")