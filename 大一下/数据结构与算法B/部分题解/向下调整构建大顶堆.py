class bigheap:
    def __init__(self):
        self.size=n
        self.heap=[0]
    def percdown(self,i):
        while i*2<=self.size:
            bc=self.bigchild(i)
            if self.heap[i]<self.heap[bc]:
                self.heap[i],self.heap[bc]=self.heap[bc],self.heap[i]
            i=bc
    def bigchild(self,i):
        if i*2+1>self.size:
            return i*2
        else:
            if self.heap[i*2]<self.heap[i*2+1]:
                return i*2+1
            else:
                return i*2
    def show(self):
        for i in range(self.size-1):
            print(self.heap[i+1],end=' ')
        print(self.heap[-1],end='')
    def build(self,n,p):
        i=n//2
        self.size=n
        self.heap=[0]+p[:]
        while i>0:
            self.percdown(i)
            i=i-1
n=int(input())
p=list(map(int,input().split()))
q=bigheap()
q.build(n,p)
q.show()