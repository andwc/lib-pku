from collections import deque
case=int(input())
for _ in range(case):
    n,m=map(int,input().split())
    degree=[0]*n
    e=[[]for _ in range(n)]
    for _ in range(m):
        x,y=map(int,input().split())
        x,y=x-1,y-1
        degree[y]+=1
        e[x].append(y)
    q=deque()
    cnt=0
    for i in range(n):
        if degree[i]==0:
            q.append(i)
            cnt+=1
    while q:
        x=q.popleft()
        for i in e[x]:
            degree[i]-=1
            if degree[i]==0:
                q.append(i)
                cnt+=1
    print('No') if cnt==n else print('Yes')