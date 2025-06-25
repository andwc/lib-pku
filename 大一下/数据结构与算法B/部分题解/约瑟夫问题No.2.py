while 1:
    n,p,m=map(int,input().split())
    if n==p==0==m:
        break
    monkey=[x+1 for x in range(n)]
    ans=[]
    p-=1
    while monkey:
        p+=m-1
        p%=n
        ans.append(monkey.pop(p))
        n-=1
    print(','.join(map(str,ans)))