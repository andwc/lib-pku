n=int(input())
p=list(map(int,input().split()))
import heapq
heapq.heapify(p)
ans=0
for _ in range(n-1):
    x=heapq.heappop(p)
    y=heapq.heappop(p)
    heapq.heappush(p,x+y)
    ans+=x+y
print(ans)