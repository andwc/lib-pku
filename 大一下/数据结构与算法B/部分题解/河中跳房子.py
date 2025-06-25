l,n,m=map(int,input().split())
p=[]
for _ in range(n):
    p.append(int(input()))
p.append(l)
def check(t):
    global p,l,m
    pre=0
    cnt=0
    for i in range(len(p)):
        if p[i]-pre<t:
            cnt+=1
        elif p[i]-pre==t:
            pre=p[i]
        else:
            pre=p[i]
        if cnt>m:
            return False
    return True
left,right=0,l
ans=0
while left<right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid
print(ans)