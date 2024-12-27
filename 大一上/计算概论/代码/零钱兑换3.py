n,m=map(int,input().split())
c=list(map(int,input().split()))
s=min(c)
dp=[float('inf')]*(m+1)
for j in range(1, m + 1):
    if j in c:
        dp[j] = 1
    for i in range(n):
        if dp[j]<1 +dp[j - c[i]]:
            dp[j] = dp[j]
        else:
            dp[j] = 1+dp[j - c[i]]
if dp[-1]!=float('inf'):
    print(dp[-1])
else:
    print(-1)