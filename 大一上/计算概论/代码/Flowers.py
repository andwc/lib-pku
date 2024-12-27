t,k= map(int, input().split())
L=1000000007
dp=[0]*(100001)
dp[0]=1
if k>1:
    dp[1]=1
else:
    dp[1]=2
for n in range(2,100001):
    dp[n]+=dp[n-1]
    if n>k-1:
        dp[n]=(dp[n]+dp[n-k])%L
q=[0]*(100001)
for n in range(1,100001):
    q[n]=(q[n-1]+dp[n])%L
for pp in range(t):
    a,b=map(int,input().split())
    print((q[b]-q[a-1])%L)