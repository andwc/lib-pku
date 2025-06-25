import heapq
N,M,K,S=map(int,input().split())
P,Q=map(int,input().split())
visited=[0]*(N+1)
ganran=set()
for _ in range(K):
    c=int(input())
    ganran.add(c)
    visited[c]=1
visited[0]=1
e=[[]for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    if a in ganran and b in ganran:
        continue
    elif b in ganran and a not in ganran:
        e[0].append(a)
    elif a in ganran and b not in ganran:
        e[0].append(b)
    else:
        e[a].append(b)
        e[b].append(a)
weixian=set()
def dfs(x,step):
    global e,weixian,S
    if step>S:
        return
    weixian.add(x)
    for y in e[x]:
        dfs(y,step+1)
    return
dfs(0,0)
distance=[float('inf')]*(N+1)
q=[]
heapq.heappush(q,(0,1))
while q:
    cost,x=heapq.heappop(q)
    if x==N:
        print(cost)
        exit()
    if visited[x]:
        continue
    visited[x]=1
    if x!=1:
        cost+=Q if x in weixian else P
    for y in e[x]:
        if not visited[y] and distance[y]>cost:
            distance[y]=cost
            heapq.heappush(q,(cost,y))