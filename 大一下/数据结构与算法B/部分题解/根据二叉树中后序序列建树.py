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
def qian(root):
    if not root:
        return []
    return [root.val]+qian(root.left)+qian(root.right)
zhong=input()
hou=input()
root=s(zhong,hou)
print(''.join(qian(root)))