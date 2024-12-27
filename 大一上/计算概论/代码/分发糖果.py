n=int(input())
c=list(map(int, input().split()))
if n==1:
    print(1)
    exit()
dp=[1]*n
index=0
judge_index=0
for i in range(n-1):
    if c[i]<c[i+1]:
        if judge_index:
            judge_index=0
        dp[i+1]=dp[i]+1
        index=i+1
    elif c[i]==c[i+1]:
        judge_index=i+1
        index=i+1
    else:
        if judge_index:
            dp[judge_index]+=1
            judge_index=0
        else:
            if dp[i]==dp[i+1]:
                for k in range(index+1,i+1):
                    dp[k]+=1
                if dp[index]<=dp[index+1]:
                    dp[index]=dp[index+1]+1
    #print(dp)
print(sum(dp))