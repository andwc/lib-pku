n=int(input())
edge=[[]for _ in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)
p=list(map(int,input().split()))
visited=[0]*n
visited[0]=1
for i in p:
    visited[i]=1
from collections import deque
q=deque()
q.append(0)
ans=0
while q:
    x=q.popleft()
    ans+=1
    visited[x]=1
    for i in edge[x]:
        if not visited[i]:
            q.append(i)
print(ans)