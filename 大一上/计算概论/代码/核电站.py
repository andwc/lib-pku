n,m=map(int,input().split())
dp=[[0,0]for _ in range(n+1)]
dp[0]=[1,1]
dp[1]=[1,1]
for i in range(2,n+1):
    if i>=m:
        dp[i][0]=dp[i-1][0]+dp[i-1][1]
        dp[i][1]=dp[i-1][0]+dp[i-1][1]-dp[i-m][0]
    else:
        dp[i][0]=dp[i-1][0]*2
        dp[i][1] = dp[i - 1][1] * 2
print(dp[-1][0]+dp[-1][1])
