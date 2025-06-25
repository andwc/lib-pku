class node:
    def __init__(self,val):
        self.val = val
        self.left=None
        self.right=None
n=int(input())
dian=[None]*(n)
num=n*(n+1)//2
for i in range(n):
    dian[i]=node(i+1)
for i in range(n):
    l,r=map(int,input().split())
    if l!=-1:
        num-=l
        dian[i].left=dian[l-1]
    if r!=-1:
        num-=r
        dian[i].right=dian[r-1]
from collections import deque
root=dian[num-1]
q=deque()
q.append(root)
depth=0
while q:
    depth+=1
    for _ in range(len(q)):
        x=q.popleft()
        if x.left:
            q.append(x.left)
        if x.right:
            q.append(x.right)
print(depth)