num=int(input())
height=list(map(int,input().split()))
h=sorted(height)
d=max(height)
row,col=num+1,len(h)+1
dp=[[0 for _ in range(col)]for _ in range(row)]
#print(dp)
for i in range(1,row):
    for j in range(col-1,0,-1):
        if height[i-1]==h[j-1]:
            dp[i][j]=max(dp[i-1][j]+1,dp[i][j-1])
        elif height[i-1]>h[j-1]:
            dp[i][j]=max(dp[i][j+1],dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[-1][1])