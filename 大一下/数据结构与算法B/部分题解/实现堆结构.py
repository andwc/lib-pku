class xiaoheap:
    def __init__(self):
        self.heaplist=[0]
        self.size=0
    def percup(self,i):
        while i//2>0:
            if self.heaplist[i]<self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2],self.heaplist[i]
            i//=2
    def insert(self,i):
        self.heaplist.append(i)
        self.size+=1
        self.percup(self.size)
    def percdown(self,i):
        while (i*2)<=self.size:
            mc=self.minchild(i)
            if self.heaplist[i]>self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc]=self.heaplist[mc],self.heaplist[i]
            i=mc
    def minchild(self,i):
        if (i*2+1)>self.size:
            return i*2
        else:
            if self.heaplist[i*2]<self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1
    def delmin(self):
        m=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.size]
        self.size-=1
        self.heaplist.pop()
        self.percdown(1)
        return m
    def buildheap(self,alist):
        i=len(alist)//2
        self.size=len(alist)
        self.heaplist=0+alist[:]
        while i>0:
            self.percdown(i)
            i-=1

n=int(input())
h=xiaoheap()
for _ in range(n):
    s=input()
    if s[0]=='1':
        s=s.split()
        a=int(s[1])
        h.insert(a)
    else:
        print(h.delmin())