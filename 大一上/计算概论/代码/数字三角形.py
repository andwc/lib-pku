n=int(input())
num=[]
dp=[[-1 for _ in range(n)]for _ in range(n)]
for i in range(n):
    shuru=list(map(int,input().split()))
    num.append(shuru)
for i in range(n):
    dp[n-1][i]=num[n-1][i]
if n!=1:
    for i in range(n-2,-1,-1):
        for j in range(i,-1,-1):
            dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+num[i][j]
print(dp[0][0])

