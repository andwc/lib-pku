class treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
s=input()
stack=[]
tree=treenode(s[0])
stack.append((tree,0))
for i in range(1,len(s)):
    x,y=stack.pop()
    if y:
        if s[i]!='.':
            x.right=treenode(s[i])
            stack.append((x.right,0))
            i+=1
    else:
        if s[i]=='.':
            stack.append((x,1))
        else:
            x.left=treenode(s[i])
            stack.append((x,1))
            stack.append((x.left,0))
def showzhong(root):
    def digui(root):
        if not root:
            return []
        return digui(root.left)+[root.value]+digui(root.right)
    p=digui(root)
    for i in p:
        print(i,end='')
def showhou(root):
    def hou(root):
        if not root:
            return []
        return hou(root.left)+hou(root.right)+[root.value]
    for i in hou(root):
        print(i,end='')
showzhong(tree)
print()
showhou(tree)