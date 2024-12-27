n,a,b=map(int,input().split())
p=list(map(int,input().split()))
ca=a
cb=b
l=0
r=n-1
cnt=0
while l<r:
    if p[l]<=ca:
        ca-=p[l]
    else:
        ca=a-p[l]
        cnt+=1
    if p[r]<=cb:
        cb-=p[r]
    else:
        cb=b-p[r]
        cnt+=1
    r-=1
    l+=1
if l==r:
    if ca>=cb:
        if p[l] > ca:
            cnt += 1
    elif ca<cb:
        if p[l] > cb:
            cnt += 1
print(cnt)