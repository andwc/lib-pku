qiu,xue,n=map(int,input().split())
data=[]
for i in range(n):
    shuru=input().split()
    if int(shuru[0])<=qiu and int(shuru[1])<=xue:
        data.append((int(shuru[0]),int(shuru[1])))
dp = [[0] * (xue + 1) for _ in range(qiu + 1)]
for q,x in data:
    for j in range(1+qiu-q):
        for k in range(1+xue-x):
            if dp[j+q][k+x]+1>dp[j][k]:
                dp[j][k]=dp[j+q][k+x]+1
num=dp[0][0]
zx=0
for j in range(xue,-1,-1):
    if dp[0][j]==num:
        zx=j if j>zx else zx
        break
print(dp[0][0],zx)