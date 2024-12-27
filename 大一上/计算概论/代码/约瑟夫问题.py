from binascii import a2b_hex

while True:
    shuru=input().split()
    n=int(shuru[0])
    m=int(shuru[1])
    if n==m==0:
        break
    a=[]
    s=m
    for i in range(n):
        a.append(i+1)
    while len(a)>1:
        while s>len(a):
            s-=len(a)
        a[s-1]=0
        #print(a)
        a.remove(0)
        s+=(m-1)
    print(a[0])