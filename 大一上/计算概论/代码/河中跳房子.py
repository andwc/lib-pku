l,n,m=map(int,input().split())
rocks=[0]
for i in range(n):
    rocks.append(int(input()))
rocks.append(l)
left=0
right=l
ans=0
while left<=right:
    mid=(left+right)//2
    #print(left,right,mid)
    cnt=0
    current=0
    for i in range(1,n+2):
        if rocks[i]-current>=mid:
            cnt+=1
            current=rocks[i]
    #print(cnt)
    if cnt<n-m+1:
        right=mid-1
    elif cnt>n-m+1:
        left=mid+1
    else:
        left=mid+1
        ans=max(ans,mid)
print(ans)