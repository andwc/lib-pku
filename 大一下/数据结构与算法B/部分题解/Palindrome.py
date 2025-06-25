def zi(a,b,n):
    dp=[0]*(n+1)
    dpp=[0]*(n+1)
    for i in range(1,1+n):
        for j in range(1,1+n):
            if (b[i-1]==a[j-1]):
                dpp[j]=dp[j-1]+1
            else:
                dpp[j]=dp[j] if dp[j]>dpp[j-1] else dpp[j-1]
        dp=dpp.copy()
    return n-dp[-1]
n=int(input())
s=input()
print(zi(s,s[::-1],n))