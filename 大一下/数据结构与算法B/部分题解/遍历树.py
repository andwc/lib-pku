n=int(input())
f=[[]for _ in range(n)]
d={}
dd={}
r=[True]*n
i=0
for _ in range(n):
    shuru=list(map(int,input().split()))
    d[i]=shuru[0]
    dd[shuru[0]]=i
    f[i]=shuru
    i+=1
for k in range(n):
    for j in f[k][1:]:
        r[dd[j]]=False
for k in range(n):
    if r[k]:
        root=k
        break
def shuchu(root):
    global f,d,dd
    ans=[]
    val=d[root]
    l=sorted(f[root])
    for i in l:
        if i==val:
            ans.append(i)
        else:
            ans.extend(shuchu(dd[i]))
    return ans
ans=shuchu(root)
for i in ans:
    print(i)