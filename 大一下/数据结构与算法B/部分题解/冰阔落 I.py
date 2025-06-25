class bingchaji:
    def __init__(self,n):
        self.f=[x for x in range(n+1)]
        self.s=[1]*(n+1)
        self.size=n

    def find(self,a):
        if a!=self.f[a]:
            self.f[a]=self.find(self.f[a])
        return self.f[a]

    def issameset(self,a,b):
        if self.find(a)==self.find(b):
            print('Yes')
        else:
            print('No')
            self.join(a,b)

    def join(self,a,b):
        fa=self.find(a)
        fb=self.find(b)
        if fa!=fb:
            self.f[fb]=fa
            self.size-=1
            self.s[fb]=0
        return
while 1:
    try:
        n,m=map(int,input().split())
        d=bingchaji(n)
        for _ in range(m):
            x,y=map(int,input().split())
            d.issameset(x,y)
        print(d.size)
        ans=[]
        for i in range(1,1+n):
            if d.s[i]:
                ans.append(str(i))
        print(' '.join(ans))
    except EOFError:
        break