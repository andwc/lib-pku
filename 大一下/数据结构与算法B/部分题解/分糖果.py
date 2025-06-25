n,m=map(int,input().split())
p=list(map(int,input().split()))
from collections import deque
q=deque()
for i in range(n):
    q.append((i+1,p[i]))
while q:
    x,y=q.popleft()
    y-=m
    if y>0:
        q.append((x,y))
print(x)