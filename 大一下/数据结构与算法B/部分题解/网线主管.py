n,k=map(int,input().split())
p=[]
for i in range(n):
    s=float(input())
    p.append(int(s*100))
def check(aim):
    global p,k
    if aim==0:
        return False
    cnt=0
    for i in p:
        cnt+=i//aim
    if cnt>=k:
        return True
    return False
left,right=0,max(p)+100
ans=0
while left<right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid
if ans==0:
    print('0.00')
else:
    ans=ans/100
    print(f'{ans:.2f}')