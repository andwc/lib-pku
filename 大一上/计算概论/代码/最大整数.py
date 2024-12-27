m=int(input())
n=int(input())
num=list(map(str,input().split()))
for i in range(n):
    for j in range(n-1-i):
        if int(num[j+1]+num[j])<int(num[j]+num[j+1]):
            num[j],num[j+1]=num[j+1],num[j]
num1=[0]
num1.extend(num)
num=num1
dp=[['' for _ in range(1+m)]for _ in range(1+n)]
for i in range(1,1+n):
    if dp[i-1][len(num[i])]:
        if int(dp[i-1][len(num[i])])>int(num[i]):
            dp[i][len(num[i])]=dp[i-1][len(num[i])]
        else:
            dp[i][len(num[i])]=num[i]
    else:
        dp[i][len(num[i])]=num[i]
    for j in range(1,1+m):
        if dp[i-1][j]:
            if dp[i][j]:
                dp[i][j]=dp[i-1][j] if int(dp[i][j])<int(dp[i-1][j]) else dp[i][j]
            else:
                dp[i][j]=dp[i-1][j]
            if j+len(num[i])<=m:
                if dp[i][j+len(num[i])]:
                    dp[i][j+len(num[i])]=num[i]+dp[i-1][j] if int(num[i]+dp[i-1][j])>int(dp[i][j+len(num[i])]) else dp[i-1][j + len(num[i])]
                else:
                    dp[i][j + len(num[i])] = num[i]+dp[i - 1][j]
print(dp[-1][-1])