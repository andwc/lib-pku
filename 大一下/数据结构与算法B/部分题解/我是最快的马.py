sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
m=int(input())
zi=set()
for i in range(m):
    x,y=map(int,input().split())
    zi.add((x,y))
from collections import deque
q=deque()
q.append([sx,sy,1,f"({sx},{sy})"])
vis=set()
vis.add((sx,sy))
ans=0
ansp=''
di=[(1,2,0,1),(1,-2,0,-1),(-1,2,0,1),(-1,-2,0,-1),(2,1,1,0),(2,-1,1,0),(-2,1,-1,0),(-2,-1,-1,0)]
while not ans:
    v=set()
    for _ in range(len(q)):
        x,y,cnt,path=q.popleft()
        for dx,dy,ddx,ddy in di:
            nx,ny=x+dx,y+dy
            if nx==ex and ny==ey:
                ans+=cnt
                ansp=path+f"-({ex},{ey})"
            elif 0<=nx<=10 and 0<=ny<=10 and (nx,ny) not in vis and (x+ddx,y+ddy) not in zi:
                if (nx,ny) in v:
                    for i in q:
                        if i[0]==nx and i[1]==ny:
                            i[2]+=cnt
                else:
                    q.append([nx,ny,cnt,path+f"-({nx},{ny})"])
                    v.add((nx,ny))
    vis&=v
if ans!=1:
    print(ans)
else:
    print(ansp)