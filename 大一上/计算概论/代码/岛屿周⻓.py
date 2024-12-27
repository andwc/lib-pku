n,m=map(int,input().split())
x=[[0 for _ in range(m+2)]for _ in range(n+2)]
ans=0
for i in range(1,n+1):
    shuru=list(map(int,input().split()))
    for j in range(1,m+1):
        if shuru[j-1]==1:
            x[i][j]=1
            ans+=2-x[i-1][j]-x[i][j-1]
        else:
            ans+=(x[i-1][j]+x[i][j-1])
    ans += x[i][m]
ans+=shuru.count(1)
print(ans)