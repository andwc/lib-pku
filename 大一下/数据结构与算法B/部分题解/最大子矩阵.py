import sys
def slove(p):
    dp=[0]*len(p)
    dp[0]=p[0]
    for i in range(1,len(p)):
        dp[i]=max(dp[i-1]+p[i],p[i])
    return max(dp)
n=int(input())
shuru=sys.stdin.read().split()
ma=[[None]*n for _ in range(n)]
ptr=0
for i in range(n):
    for j in range(n):
        ma[i][j]=int(shuru[ptr])
        ptr+=1
pre=[[0]*(n+1) for _ in range(n)]
for i in range(n):
    cnt=0
    for j in range(1,1+n):
        cnt+=ma[i][j-1]
        pre[i][j]=cnt
ans=-float('inf')
cnt=0
for left in range(n):
    for right in range(left+1,n+1):
        p=[]
        for k in range(n):
            p.append(pre[k][right]-pre[k][left])
        ans=max(ans,slove(p))
print(ans)