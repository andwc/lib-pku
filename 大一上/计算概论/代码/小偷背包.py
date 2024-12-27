n,b=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[[0 for _ in range(b+1)]for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,b+1):
        if weight[i-1]<=j:
            dp[i][j]=max(dp[i-1][j-weight[i-1]]+price[i-1],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][-1])