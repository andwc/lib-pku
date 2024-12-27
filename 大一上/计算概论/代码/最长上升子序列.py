n=int(input())
num=list(map(int,input().split()))
dp=[[0 for _ in range(n)]for _ in range(n)]
snum=sorted(num)
for i in range(n):
    for j in range(n-1,-1,-1):

#print(dp[-1][0])
print(' ',snum)
for i in range(n):
    print(num[i],dp[i])