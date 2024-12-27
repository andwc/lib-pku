n,m=map(int,input().split())
goods=[[]for i in range(n)]
for i in range(n):
    shuru = list(map(str, input().split()))
    for j in range(len(shuru)):
        a, b = map(int,shuru[j].split(':'))
        goods[i].append((a, b))
youhui=[[]for _ in range(m)]
for i in range(m):
    shuru=list(map(str,input().split()))
    for j in range(len(shuru)):
        a,b=map(int,shuru[j].split('-'))
        youhui[i].append((a,b))
    youhui[i].sort(key=lambda x: x[1],reverse=True)
daan=float('inf')
def jisuan(path):
    global m
    dian=[0]*(m+1)
    ans=0
    for a,b in path:
        dian[a]+=b
        ans+=b
    ans-=50*(ans//300)
    for i in range(1,m+1):
        for j in range(len(youhui[i-1])):
            if dian[i]>=youhui[i-1][j][0]:
                ans-=youhui[i-1][j][1]
                break
    return ans
def dfs(i,path):
    global n,daan
    if i==n:
        ans=jisuan(path)
        daan=min(daan,ans)
        return
    for j in range(len(goods[i])):
        path.append((goods[i][j][0],goods[i][j][1]))
        dfs(i+1,path)
        path.pop()
dfs(0,[])
print(daan)