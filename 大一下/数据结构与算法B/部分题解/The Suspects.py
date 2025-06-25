class disjointset:
    def __init__(self,n):
        self.f=[x for x in range(n)]
        self.size=[1]*n
    def find(self,x):
        if self.f[x]==x:
            return x
        else:
            self.f[x]=self.find(self.f[x])
            return self.f[x]

    def union(self,x,y):
        fx=self.find(x)
        fy=self.find(y)
        if fx!=fy:
            if fx==0:
                self.f[fy]=fx
                self.size[fx]+=self.size[fy]
            else:
                self.f[fx]=fy
                self.size[fy]+=self.size[fx]
        return
while 1:
    n,m=map(int,input().split())
    if n==0==m:
        break
    p=disjointset(n)
    for i in range(m):
        shuru=list(map(int,input().split()))
        if shuru[0]<=1:
            continue
        ggbond=shuru[1]
        right=shuru[0]+1
        for j in range(2,right):
            p.union(shuru[j],ggbond)
    print(p.size[0])