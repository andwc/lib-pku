n=int(input())
w=list(map(int,input().split()))
fu=[]
qian=[0]*n
ans=0
qian[0]=w[0] if w[0]>=0 else 0
ans=1 if w[0]>=0 else 0
for i in range(1,n):
    if w[i]<0:
        fu.append((w[i],i))
        qian[i]=qian[i-1]
    else:
        ans+=1
        qian[i]=qian[i-1]+w[i]
fu.sort(key=lambda x:x[0],reverse=True)
for i in range(len(fu)):
    if qian[fu[i][1]]+fu[i][0]>=0:
        judge=1
        for j in range(fu[i][1],len(qian)):
            qian[j]+=fu[i][0]
            if qian[j]<0:
                judge=0
                for k in range(j,fu[i][1]-1,-1):
                    qian[k]-=fu[i][0]
                break
        ans+=1 if judge==1 else 0
print(ans)