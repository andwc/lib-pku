p=int(input())
d={}
for i in range(p):
    s=input()
    d[s]={}
q=int(input())
for i in range(q):
    a,b,c=input().split()
    d[a][b]=int(c)
    d[b][a]=int(c)
r=int(input())
def dijkstra(start,end,d,p):
    import heapq
    if start==end:
        return [start]
    dist = {i: (float('inf'), []) for i in d}
    dist[start] = (0, [start])
    q = []
    heapq.heappush(q, (0, start, [start]))
    while q:
        dist1, current, path = heapq.heappop(q)
        for (next, dist2) in d[current].items():
            if dist2 + dist1 < dist[next][0]:
                dist[next] = (dist2 + dist1, path + [next])
                heapq.heappush(q, (dist1 + dist2, next, path + [next]))
    return dist[end][1]
for j in range(r):
    start,end=input().split()
    path=dijkstra(start,end,d,p)
    n=len(path)
    print(path[0],end='')
    for i in range(1,n):
        print(f"->({d[path[i]][path[i-1]]})->{path[i]}",end='')
    if j!=r-1:
        print()