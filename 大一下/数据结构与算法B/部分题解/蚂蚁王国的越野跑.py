from bisect import bisect_left
n=int(input())
v=[]
ans=0
for i in range(n):
    p=int(input())
    index=bisect_left(v,p)
    v.insert(index,p)
    ans+=index
print(ans)