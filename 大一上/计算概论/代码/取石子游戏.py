def dfs(a,b,xuanshou):
    if a<b:
        a,b=b,a
    if a//b>=2 or a%b==0:
        return xuanshou
    else:
        return(dfs(a-b,b,xuanshou+1))
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    cishu=dfs(a,b,0)
    cishu%=2
    if cishu:
        print('lose')
    else:
        print('win')