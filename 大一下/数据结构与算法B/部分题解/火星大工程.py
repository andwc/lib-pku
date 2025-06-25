from collections import deque
n,m=map(int,input().split())
degree=[0]*n
edge=[[]for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    a,b=a-1,b-1
    degree[b]+=1
    edge[a].append((b,c))
distance=[float('-inf')]*n
path=[[]for _ in range(n)]
q=deque()
for i in range(n):
    if degree[i]==0:
        q.append((i,[i],0))
        distance[i]=0
while q:
    # print(path)
    # print(distance)
    # print()
    x,way,cost=q.popleft()
    for nx,ncost in edge[x]:
        if cost+ncost>distance[nx]:
            nway=[way+[nx]]
            distance[nx]=cost+ncost
            path[nx]=nway
        elif cost+ncost==distance[nx]:
            path[nx].append(way+[nx])
        degree[nx]-=1
        if degree[nx]==0:
            q.append((nx,path[nx][-1],distance[nx]))
ans=set()
time=0
target=[]
aim=max(distance)
for i in range(n):
    if distance[i]==aim:
        target.append(i)
for i in target:
    time=max(time,distance[i])
    for j in path[i]:
        for k in range(1,len(j)):
            ans.add((j[k-1],j[k]))
print(time)
ans=sorted(ans)
for i,j in ans:
    print(i+1,j+1)