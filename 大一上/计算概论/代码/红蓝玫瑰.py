s=input()
n=len(s)
dp=[0]*n
dpp=[0]*n
for i in range(n):
    if s[i]=='R':
        dp[i]=dp[i-1]
        dpp[i]=min(dpp[i-1],dp[i])+1
    else:
        dpp[i]=dpp[i-1]
        solution1=dp[i-1]+1
        index=-1
        for j in range(i-1,-1,-1):
            if s[j]=='R':
                index=j
                break
        solution2=1 if index==-1 else dpp[index]+1
        dp[i]=min(solution2,solution1)
print(dp[-1])