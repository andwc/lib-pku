import heapq
n=int(input())
q=list(map(int,input().split()))
ans=0
p=[]
for i in range(n):
    heapq.heappush(p,q[i])
while len(p)>=2:
    x=heapq.heappop(p)
    y=heapq.heappop(p)
    ans+=x+y
    heapq.heappush(p,x+y)
print(ans)