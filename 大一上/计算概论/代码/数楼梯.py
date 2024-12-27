from sys import setrecursionlimit
setrecursionlimit(100000)
def s(n):
    global dp
    if dp[n-1] and dp[n-2]:
        dp[n]=dp[n-1]+dp[n-2]
    else:
        s(n-1)
        s(n-2)
n=int(input())
dp=[None]*(n+1)
dp[0]=1
dp[1]=1
if n==1:
    print(1)
    exit()
s(n)
print(dp[-1])