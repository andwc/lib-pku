class disjointset:
    def __init__(self,n):
        self.f=[x for x in range(n)]
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
        return
n=int(input())
p=disjointset(n)
e=[]
for i in range(n-1):
    shuru=input().split()
    s=ord(shuru[0])-ord('A')
    j=2
    while j<len(shuru):
        index=ord(shuru[j])-ord('A')
        e.append((int(shuru[j+1]),s,index))
        j+=2
e.sort()
ans=0
for k,i,j in e:
    if not p.issameset(i,j):
        p.union(i,j)
        ans+=k
print(ans)