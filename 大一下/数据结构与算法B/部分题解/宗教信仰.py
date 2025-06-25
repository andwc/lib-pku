class bingchaji():
    def __init__(self,n):
        self.father=[x for x in range(n)]
        self.size=[1]*n

    def find(self,a):
        stack=[]
        while self.father[a]!=a:
            stack.append(a)
            a=self.father[a]
        for j in stack:
            self.father[j]=a
        return a

    def issameset(self,a,b):
        return self.find(a)==self.find(b)

    def union(self,a,b):
        fa=self.find(a)
        fb=self.find(b)
        if fa!=fb:
            if self.size[fa]>self.size[fb]:
                self.father[fb]=fa
                self.size[fa]+=self.size[fb]
            else:
                self.father[fa]=fb
                self.size[fb]+=self.size[fa]

case=1
while 1:
    n,m=map(int,input().split())
    if n==m==0:
        break
    p=bingchaji(n)
    for i in range(m):
        a,b=map(int,input().split())
        p.union(a-1,b-1)
    print(f'Case {case}: ',end='')
    case+=1
    if m==0:
        print(n)
        continue
    ans=0
    visited=set()
    for i in range(n):
        if p.find(i) not in visited:
            visited.add(p.find(i))
            ans+=1
    print(ans)
