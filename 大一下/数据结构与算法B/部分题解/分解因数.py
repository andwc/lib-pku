n=int(input())
import math
def f(n,judge):
    if n<=3:
        return 1
    ans=1
    for i in range(max(2,judge),int(math.sqrt(n))+1):
        if n%i!=0:
            continue
        ans+=f(n//i,i)
    return ans
for _ in range(n):
    num=int(input())
    print(f(num,0))