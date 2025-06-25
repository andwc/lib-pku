n,m=map(int,input().split())
de=[0]*n
chu=[0]*n
u=[0]*n
c= [0] * n
from collections import deque
q=deque()
for i in range(n):
    a,b=map(int,input().split())
    c[i]=a
    u[i]=b

e=[{}for _ in range(n)]
for i in range(m):
    a,v,w=map(int,input().split())
    a-=1
    v-=1
    if a==v:
        print('NULL')
        exit()
    if v in e[a]:
        e[a][v]+=w
    else:
        e[a][v]=w
        de[v]+=1
        chu[a]+=1

for i in range(n):
    if de[i]==0:
        q.append(i)
        c[i]+=u[i]

judge=True
cnt=0

while q:
    x=q.popleft()
    cnt+=1
    c[x]-=u[x]
    for y in e[x]:
        de[y] -= 1
        if c[x]>0:
            c[y]+=c[x]*e[x][y]
        if de[y] == 0:
            q.append(y)

if cnt!=n:
    print('NULL')
    exit()
ans=[]
for i in range(n):
    if chu[i]==0 and c[i]>0:
        ans.append((i+1,c[i]))
if not ans:
    print('NULL')
    exit()
for i in ans:
    print(' '.join(map(str,i)))
