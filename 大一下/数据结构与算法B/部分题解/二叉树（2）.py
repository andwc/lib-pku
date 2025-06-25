while 1:
    m,n=map(int,input().split())
    if n==m==0:
        break
    index=1
    x,y=m,m
    while x<n:
        index+=1
        x,y=x*2+1,y*2
    print(2**index-1-min((x-n),(x-y+1)))