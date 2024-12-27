n=int(input())
p=[]
import sys
for i in range(n):
    shuru=input().split()
    p.append((int(shuru[0]),int(shuru[1])))
p.sort(key=lambda x: x[1])
ed=-sys.maxsize
res=0
for v in p:
    if ed < v[0]:
        res += 1
        ed = v[1]
print(res)
#print(p)