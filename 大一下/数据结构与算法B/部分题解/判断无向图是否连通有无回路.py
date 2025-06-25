from collections import deque
class disjointset:
    def __init__(self,n):
        self.f=[x for x in range(n)]
    def find(self,x):
        st=[]
        while self.f[x]!=x:
            st.append(x)
            x=self.f[x]
        for i in st:
            self.f[i]=x
        return x
    def issameset(self,x,y):
        return self.find(x) == self.find(y)
    def union(self,x,y):
        fx=self.find(x)
        fy=self.find(y)
        self.f[fx]=fy
        return

n,m=map(int,input().split())
e=[[]for _ in range(n)]
b=disjointset(n)
loop=False
for _ in range(m):
    u,v=map(int,input().split())
    e[u].append(v)
    e[v].append(u)
    if b.issameset(u,v):
        loop=True
    b.union(u,v)
target=b.find(0)
for i in range(n):
    if b.find(i)!=target:
        ans='no'
        break
else:
    ans='yes'
loop='yes' if loop else 'no'
print(f'connected:{ans}')
print(f'loop:{loop}')