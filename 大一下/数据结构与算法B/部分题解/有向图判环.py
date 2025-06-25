n,m=map(int,input().split())
e=[set()for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    e[a].add(b)
def bfs(sx):
    global e
    from collections import deque
    q=deque()
    vis=set()
    for i in e[sx]:
        q.append(i)
        vis.add(i)
    while q:
        x=q.popleft()
        if x==sx:
            return True
        for i in e[x]:
            if i not in vis:
                vis.add(i)
                q.append(i)
    return False
ans=False
for i in range(n):
    ans|=bfs(i)
if ans:
    print('Yes')
else:
    print('No')