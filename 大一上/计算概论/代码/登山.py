n=int(input())
p=list(map(int,input().split()))
dp=[1]*n
for i in range(n-1,-1,-1):
    for j in range(i+1,n):
        if p[i]>p[j]:
            dp[i]=dp[i] if dp[i]>dp[j]+1 else dp[j]+1
dpp=[0]*n
ans=0
for i in range(n):
    for j in range(0,i):
        if p[i]>p[j]:
            dpp[i]=dpp[i] if dpp[i]>dpp[j]+1 else dpp[j]+1
    ans = ans if ans>dpp[i]+dp[i] else dpp[i]+dp[i]
print(ans)