import math
num=0
def qujian(l):
    l.sort(key = lambda x : x[1])
    ed=l[0][1]
    re=1
    for i in range(1,len(l)):
        if l[i][0]<=ed:
            pass
        else:
            re+=1
            ed=l[i][1]
    return re
while True:
    answer=0
    shuru=input()
    if shuru=='':
        continue
    n,d=map(int,shuru.split())
    if n==d==0:
        break
    num+=1
    x=[]
    for i in range(n):
        sx,sy=map(int,input().split())
        if d**2<sy**2 or d<0:
            answer=-1
        s=d*d-sy*sy
        if s<=0:
            s=0
        dx=math.sqrt(s)
        x.append([sx-dx,sx+dx])
    if answer==-1:
        print('Case ',num,': ',answer,sep='')
    else:
        answer=qujian(x)
        print('Case ',num,': ',answer,sep='')

