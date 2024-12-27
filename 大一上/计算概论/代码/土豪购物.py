shu=input()
p=list(map(int,shu.split(',')))
dp=[0 for _ in range(1+len(p))]
dpp=[0 for _ in range(1+len(p))]
for i in range(1,1+len(p)):
    dp[i]=max(p[i-1],dp[i-1]+p[i-1])
for i in range(1,1+len(p)):
    dpp[i]=max(dp[i],dp[i-1],dpp[i-1]+p[i-1])
print(max(dpp))