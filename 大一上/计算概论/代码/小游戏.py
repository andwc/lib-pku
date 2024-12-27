from collections import deque
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x1,y1):
    global card,n,m,x2,y2,visited
    queue=deque()
    queue.append((x1,y1))
    step=0
    while queue:
        step+=1
        for _ in range(len(queue)):
            x,y=queue.popleft()
            visited.add((x,y))
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx==x2 and ny==y2:
                    return step
                while 0<=nx<m+2 and 0<=ny<n+2 and (nx,ny) not in visited and card[nx][ny]==' ':
                    queue.append((nx,ny))
                    nx,ny=nx+dx,ny+dy
                    if nx==x2 and ny==y2:
                        return step
case=0
while True:
    case+=1
    n,m=map(int,input().split())
    if n==m==0:
        break
    print('Board #',case,':',sep='')
    card=[]
    card.append(' '*(n+2))
    for _ in range(m):
        s=input()
        card.append(' '+s+' ')
    card.append(' ' * (n+2))
    xiaocase=0
    while True:
        xiaocase+=1
        visited=set()
        x1,y1,x2,y2=map(int,input().split())
        x1, y1, x2, y2 =y1,x1,y2,x2
        path=[(x1,y1)]
        a=0
        if x1==x2==y1==y2==0:
            break
        a=bfs(x1,y1)
        if not a:
            print('Pair ',xiaocase,': impossible.',sep='')
        else:
            print('Pair ',xiaocase,': ',a,' segments.',sep='')
    print()