directions=[[-1,1],[0,1],[1,1],[-1,-1],[1,-1],[0,-1],[-1,0],[1,0]]
def dfs(ma,i,j,ans):
    for dx,dy in directions:
        if ma[i+dx][j+dy]=='W':
            ans+=1
            ma[i + dx][j + dy] = '.'
            ma,ans=dfs(ma,i+dx,j+dy,ans)
    return ma,ans
case=int(input())
for _ in range(case):
    n,m=map(int,input().split())
    ma=[]
    ans,judge=0,0
    ma.append(['.' for _ in range(m+2)])
    for _ in range(n):
        ma.append(['.']+list(input())+['.'])
    ma.append(['.' for _ in range(m+2)])
    for i in range(1,n+1):
        for j in range(1,m+1):
            if ma[i][j]=='W':
                ma[i][j]='.'
                ma,judge=dfs(ma,i,j,1)
                ans=judge if judge>ans else ans
    print(ans)