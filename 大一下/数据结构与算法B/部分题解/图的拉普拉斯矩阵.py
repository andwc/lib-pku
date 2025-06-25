class vertex:
    def __init__(self,k):
        self.key=k
        self.neighbors={}
    def set_neighbor(self,other,w):
        self.neighbors[other]=w
class graph:
    def __init__(self,n):
        self.vertices={}
        for i in range(n):
            self.vertices[i]=vertex(i)
    def set_vertex(self,k):
        self.vertices[k]=vertex(k)
    def add_edge(self,s,t,w):
        self.vertices[s].set_neighbor(self.vertices[t],w)
n,m=map(int,input().split())
g=graph(n)
for i in range(m):
    a,b=map(int,input().split())
    g.add_edge(a,b,1)
    g.add_edge(b,a,1)
ans=[[0]*n for _ in range(n)]
for i in range(n):
    ans[i][i]+=len(g.vertices[i].neighbors)
    for j in g.vertices[i].neighbors:
        ans[i][j.key]-=1
for i in ans:
    print(' '.join(map(str,i)))