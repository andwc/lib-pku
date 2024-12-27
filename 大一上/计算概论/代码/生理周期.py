def zhouqi(a,a1,b,b1):
    while a!=b:
        if a>b:
            b+=b1
            continue
        a+=a1
    return (a)
i=1
while True:
    a,b,c,d=map(int,input().split())
    if a==b==c==d==-1:
        break
    answer=0
    k=zhouqi(a,23,b,28)
    #print(k)
    answer+=zhouqi(c,33,k,644)
    answer-=d
    #print(a,b,c,d)
    if answer<=0:
        answer+=21252
    print('Case ',i,': the next triple peak occurs in ',answer,' days.',sep='')
    i+=1