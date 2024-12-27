n=int(input())
p=list(map(int,input().split()))
q=[]
for i in range(n):
    q.append((max(0,i-p[i]),min(n-1,i+p[i])))
q.sort(key=lambda x:x[0])
start=0
end=0
ans=1
for i in range(n):
    if end==n-1:
        break
    if q[i][0]<=start<=q[i][1]:
        end=max(end,q[i][1])
    elif q[i][0]>start:
        ans+=1
        start=0
        start+=end
print(ans)