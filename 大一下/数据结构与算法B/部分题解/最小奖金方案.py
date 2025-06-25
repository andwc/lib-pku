n,m=map(int,input().split())
g=[[] for _ in range(n)]
de=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    g[b].append(a)
    de[a]+=1
d=[99]*n
from collections import deque
q=deque()
for i in range(n):
    if de[i]==0:
        q.append(i)
cost=0
while q:
    cost+=1
    for _ in range(len(q)):
        x=q.popleft()
        d[x]+=cost
        for i in g[x]:
            de[i]-=1
            if de[i]==0:
                q.append(i)
print(sum(d))