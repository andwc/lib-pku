n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    g[a].append([b,c])
import heapq
d=[float('inf')]*(n+1)
visited=[0]*(n+1)
d[1]=0
q=[]
heapq.heappush(q,(0,1))
while q:
    c,x=heapq.heappop(q)
    if visited[x]:
        continue
    visited[x]=1
    for i,cost in g[x]:
        if not visited[i] and c+cost<d[i]:
            d[i]=c+cost
            heapq.heappush(q,(d[i],i))
print(d[n])