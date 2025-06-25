t=int(input())
from collections import deque
for _ in range(t):
    n,k=input().split()
    k=int(k)
    q=deque()
    q.append(n)
    for _ in range(k):
        for _ in range(len(q)):
            s=q.popleft()
            for i in range(len(s)):
                ss=s[0:i]+s[i+1:]
                q.append(ss)
    print(min(q))