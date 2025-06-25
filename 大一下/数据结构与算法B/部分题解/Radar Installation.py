case=0
while True:
    s=input().split()
    if s:
        n,d=int(s[0]),int(s[1])
        case+=1
    else:
        continue
    if n==0 and d==0:
        break
    print(f'Case {case}: ',end='')
    judge=0
    q=[]
    ans=1
    for i in range(n):
        x,y=map(int,input().split())
        y=abs(y)
        if y>d:
            judge=1
            continue
        dx=(d**2-y**2)**(1/2)
        q.append([x-dx,x+dx])
    if judge:
        print(-1)
        continue
    q.sort(key=lambda x:(-x[1],-x[0]))
    st=q[0][0]
    for i in range(1,n):
        if q[i][1]<st:
            ans+=1
            st=q[i][0]
        elif q[i][0]>st:
            st=q[i][0]
    print(ans)