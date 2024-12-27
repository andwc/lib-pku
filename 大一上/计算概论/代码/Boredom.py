def main():
    n=int(input())
    num=list(map(int,input().split()))
    a=set(num)
    m=max(a)
    dp=[0]*(m+1)
    c=[0]*(m+1)
    for i in num:
        c[i]+=1
    dp[1]=c[1]
    for i in range(1,m+1):
        dp[i]=dp[i-1] if dp[i-1]>dp[i-2]+i*c[i] else dp[i-2]+i*c[i]
    print(dp[m])
main()