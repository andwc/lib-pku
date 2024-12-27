def f(a,b):
    global t,judge
    q=(a<=t+judge)
    a-=t
    b-=t
    if a<0:
        a=-a
    if b<0:
        b=-b
    return a<=b and q
n,t=map(int,input().split())
p=list(map(int,input().split()))
judge=0
a=min(p)
s=sum(p)
dp=[0]*(s+1)
dp[0]=1
for i in range(len(p)):
    for j in range(s,p[i]-1,-1):
        if dp[j-p[i]]:
            dp[j]=1
            if j>=t and j<=t+a:
                a=j-t
                judge=1
    #print(dp)
if judge:
    print(t+a)
else:
    print(0)