n,c=map(int,input().split())
stones=[]
for i in range(n):
    stones.append(int(input()))
stones.sort()
# print(stones)
def check(target):
    global stones,c,n
    cnt=c-1
    pre=stones[0]
    for i in range(1,n):
        if stones[i]-pre>=target:
            cnt-=1
            pre=stones[i]
    if cnt>0:
        return False
    return True
left,right=0,stones[-1]+1
# for i in range(stones[-1]):
#     print(i,check(i))
ans=0
while left<right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid
print(ans)