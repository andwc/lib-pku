n,m=map(int,input().split())
p=[]
for i in range(n):
    a=int(input())
    p.append(a)
left=max(p)
right=sum(p)+1
def check(t):
    global p,n,m
    cnt=1
    cur=0
    for i in range(n):
        cur+=p[i]
        if cur>t:
            cnt+=1
            cur=p[i]
        if cnt>m:
            return False
    return True
# print(check(499),check(500),check(501))
while left<right:
    mid=(left+right)//2
    if check(mid):
        right=mid
    else:
        left=mid+1
mid=(left+right)//2
print(mid)