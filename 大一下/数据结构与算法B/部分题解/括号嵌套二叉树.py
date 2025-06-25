class treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def b(s):
    if not s or s=='*':
        return
    a=''
    i=0
    while i<len(s)and s[i]!='(' :
        a+=s[i]
        i+=1
    root = treenode(a)
    if i==len(s):
        return root
    else:
        judge=0
        p=0
        for j in range(i+1,len(s)-1):
            if s[j]=='(':
                judge+=1
            elif s[j]==')':
                judge-=1
            if s[j]==',' and not judge:
                p=1
                l=s[i+1:j]
                r=s[j+1:len(s)-1]
                root.left=b(l)
                root.right=b(r)
                break
        if not p:
            root.left=treenode(s[i+1:len(s)-1])
    return root
def showqian(root):
    print(root.value,end='')
    if root.left:
        showqian(root.left)
    if root.right:
        showqian(root.right)
def showzhong(root):
    def digui(root):
        if not root:
            return []
        return digui(root.left)+[root.value]+digui(root.right)
    p=digui(root)
    for i in p:
        print(i,end='')
def show(root):
    showqian(root)
    print()
    showzhong(root)
    print()
case=int(input())
for _ in range(case):
    s=input()
    root=b(s)
    show(root)