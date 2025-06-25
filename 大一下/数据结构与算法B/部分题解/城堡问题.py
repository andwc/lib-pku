from collections import deque
row=int(input())
col=int(input())
ma=[[None]*col for i in range(row)]
visited=[[False]*col for i in range(row)]
class node:
    def __init__(self,num):
        self.neighbor=[]
        if not num&1:
            self.neighbor.append((0,-1))
        if not num&2:
            self.neighbor.append((-1,0))
        if not num&4:
            self.neighbor.append((0,1))
        if not num&8:
            self.neighbor.append((1,0))
for i in range(row):
    shuru=list(map(int,input().split()))
    for j in range(col):
        ma[i][j]=node(shuru[j])
number=0
ans=0
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            number+=1
            q=deque()
            q.append((i,j))
            visited[i][j]=True
            cnt=0
            while q:
                cnt+=1
                x,y=q.popleft()
                if ma[x][y].neighbor:
                    for dx,dy in ma[x][y].neighbor:
                        nx,ny=x+dx,y+dy
                        if not visited[nx][ny]:
                            q.append((nx,ny))
                            visited[nx][ny]=True
            ans=cnt if ans<cnt else ans
print(number)
print(ans)