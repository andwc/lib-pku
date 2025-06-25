import math
import heapq

sx,sy,ex,ey=map(int,input().split())
nd={}
nd[(sx,sy)]=0
nd[(ex,ey)]=1
node={}
node[0]=(sx,sy)
node[1]=(ex,ey)
subways=[]
index=2
while 1:
    try:
        shuru=list(map(int,input().split()))
        i=0
        p=[]
        while i<len(shuru)-2:
            node[index]=(shuru[i],shuru[i+1])
            nd[(shuru[i],shuru[i+1])]=index
            p.append(node[index])
            index+=1
            i+=2
        subways.append(p)
    except EOFError:
        break
n=len(node)
edge=[[] for _ in range(n)]
VP=10000/60
VS=40000/60
def d(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
for i in subways:
    for j in range(len(i)-1):
        edge[nd[i[j]]].append((nd[i[j+1]],d(i[j],i[j+1])/VS))
    for j in range(1,len(i)):
        edge[nd[i[j]]].append((nd[i[j-1]],d(i[j],i[j-1])/VS))
for i in range(n):
    for j in range(i+1,n):
        edge[i].append((j,d(node[i],node[j])/VP))
        edge[j].append((i,d(node[j],node[i])/VP))
visited=[0]*n
d=[float('inf')]*n
q=[]
heapq.heappush(q,(0,0))
while q:
    z,x=heapq.heappop(q)
    visited[x]=1
    if x==1:
        print(round(z))
        break
    for nx,cost in edge[x]:
        if not visited[nx] and z+cost<d[nx]:
            d[nx]=z+cost
            heapq.heappush(q,(d[nx],nx))