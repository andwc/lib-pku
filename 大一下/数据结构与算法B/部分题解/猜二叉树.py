class treenode:
    def __init__(self, val):
        self.val = val
        self.left=None
        self.right=None
def s(zhong,hou):
    n=len(hou)
    if n==0:
        return
    root=treenode(hou[-1])
    for i in range(n):
        if zhong[i]==hou[-1]:
            root.left=s(zhong[:i],hou[:i])
            root.right=s(zhong[i+1:],hou[i:-1])
            break
    return root
from collections import deque
def ceng(root):
    queue=deque()
    queue.append(root)
    while queue:
        for i in range(len(queue)):
            x=queue.popleft()
            print(x.val,end='')
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
    print()
case=int(input())
for _ in range(case):
    zhong=input()
    hou=input()
    root=s(zhong,hou)
    ceng(root)