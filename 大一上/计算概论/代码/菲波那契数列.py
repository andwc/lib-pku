def f(a):
    if a<=2:
        return 1
    if dp[a]!=-1:
        return dp[a]
    else:
        dp[a]=f(a-1)+f(a-2)
        return dp[a]

n=int(input())
dp=[-1]*21
ans=[]
for _ in range(n):
    x=int(input())
    print(f(x))