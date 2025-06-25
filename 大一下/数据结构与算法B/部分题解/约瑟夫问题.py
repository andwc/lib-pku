while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    p=[1]*(n+1)
    chu=0
    i=0
    while chu!=n-1:
        cnt=0
        while cnt<m:
            i+=1
            if i>n:
                i-=n
            if p[i]:
                cnt+=1
        p[i]-=1
        #print(p)
        chu+=1
    for i in range(1,1+n):
        if p[i]:
            print(i)
