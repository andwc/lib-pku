class treenode:
    def __init__(self, val):
        self.val = val
        self.left=None
        self.right=None
def s(qian,zhong):
    n=len(qian)
    if n==0:
        return
    root=treenode(qian[0])
    for i in range(n):
        if zhong[i]==qian[0]:
            root.left=s(qian[1:i+1],zhong[:i])
            root.right=s(qian[i+1:],zhong[i+1:])
            break
    return root
def hou(root):
    if not root:
        return []
    return hou(root.left)+hou(root.right)+[root.val]
while True:
    try:
        qian=input()
        zhong=input()
        root=s(qian,zhong)
        print(''.join(hou(root)))
    except EOFError:
        break