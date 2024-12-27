T,n=map(int,input().split())
t=[]
w=[]
t.append(0)
w.append(0)
for _ in range(n):
    shuru=input().split()
    t.append(int(shuru[0]))
    w.append(int(shuru[1]))
dp=[[0 for _ in range(1+T)]for _ in range(1+n)]
for i in range(1,1+n):
    dp[i][t[i]]=max(w[i],dp[i-1][t[i]])
    for j in range(1,1+T):
        if dp[i-1][j]:
            dp[i][j]=max(dp[i][j],dp[i-1][j])
            if j+t[i]<=T:
                dp[i][j+t[i]]=max(dp[i-1][j+t[i]],dp[i-1][j]+w[i])
if dp[-1][-1]:
    print(dp[-1][-1])
else:
    print(-1)