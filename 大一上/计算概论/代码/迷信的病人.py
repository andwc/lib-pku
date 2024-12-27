def oula(n):
    dp=[True]*(n+1)
    zhishu=[]
    for i in range(2,n+1):
        if dp[i]:
            zhishu.append(i)
        for j in zhishu:
            if j*i<=n:
                dp[j*i]=False
    return zhishu
def pingfang(n):

zhishu=oula(1000)
n,m=map(int,input().split())
