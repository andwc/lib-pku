class disjointset:
    def __init__(self,n,p):
        self.f=[x for x in range(n)]
        self.p=p
    def find(self,a):
        st=[]
        while self.f[a]!=a:
            st.append(a)
            a=self.f[a]
        for i in st:
            self.f[i]=a
        return a
    def issameset(self,a,b):
        return self.find(a)==self.find(b)
    def union(self,a,b):
        fa=self.find(a)
        fb=self.find(b)
        if fa==fb:
            return
        self.f[fa]=fb
        self.p[fb]=min(self.p[fb],self.p[fa])
        return
n,m=map(int,input().split())
p=list(map(int,input().split()))
g=disjointset(n,p)
for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    g.union(a,b)
ans=0
visited=set()
for i in range(n):
    fi=g.find(i)
    if fi not in visited:
        ans+=g.p[fi]
        visited.add(fi)
print(ans)