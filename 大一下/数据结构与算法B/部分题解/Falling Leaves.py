class treenode:
    def __init__(self, value):
        self.val = value
        self.left=None
        self.right=None
def preorder(root):
    if root.val:
        print(root.val,end='')
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)
while True:
    p=[]
    while True:
        s=input()
        if s=='*' or s=='$':
            break
        p.append(s)
    n=len(p)
    p=p[-1:-n-1:-1]
    root=treenode(p[0])
    stack=[]
    stack.append((chr(1),root.val,root))
    stack.append((root.val,chr(150),root))
    linshi=[]
    for i in range(1,n):
        for j in p[i]:
            node=treenode(j)
            for k in range(-1,-1-len(stack),-1):
                (a,b,c)=stack[k]
                if a<=j<=b:
                    if b==c.val:
                        c.left=node
                        linshi.append((a,j,node))
                        linshi.append((j,b,node))
                    else:
                        c.right=node
                        linshi.append((a,j,node))
                        linshi.append((j,b,node))
                    stack.pop(k)
                    break
        stack.extend(linshi)
        linshi=[]
    preorder(root)
    print()
    if s=='$':
        break