score=list(map(float,input().split()))
def check(t):
    global score
    a=t/1000000000
    cnt=0
    for i in score:
        if a*i+1.1**(a*i)>=85.0:
            cnt+=1
    if cnt>=0.6*len(score):
        return True
    return False
left,right=0,1000000000
ans=0
while left<right:
    mid=(left+right)//2
    if check(mid):
        right=mid
        ans=mid
    else:
        left=mid+1
print(ans)