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
        self.f[fa]=fb
        return
while 1:
    try:
        n=int(input())
        cost=0
        node=disjointset(n)
        edge=[]
        cnt=0
        while cnt<n*n:
            shuru=list(map(int,input().split()))
            for k in shuru:
                cnt+=1
                i,j=(cnt-1)//n,(cnt-1)%n
                if i==j:
                    continue
                edge.append((k,i,j))
        edge.sort()
        for a,b,c in edge:
            if not node.issameset(b,c):
                cost+=a
                node.union(b,c)
        print(cost)
    except EOFError:
        break