class treenode:
    def __init__(self, val):
        self.val = val
        self.left=None
        self.right=None
def preorder(root):
    if root is None or root.val=='*':
        return []
    return [root.val]+preorder(root.left)+preorder(root.right)
def inorder(root):
    if root is None or root.val=='*':
        return []
    return inorder(root.left)+[root.val]+inorder(root.right)
def postorder(root):
    if root is None or root.val=='*':
        return []
    return postorder(root.left)+postorder(root.right)+[root.val]
n=int(input())
for case in range(n):
    st=[]
    while 1:
        s=input()
        if s=='0':
            break
        if not st:
            st.append([treenode(s),0])
            continue
        cnt=len(s)-1
        node=treenode(s[-1])
        while st[-1][1]>=cnt:
            st.pop()
        if st[-1][0].left:
            st[-1][0].right=node
        else:
            st[-1][0].left=node
        if node.val!='*':
            st.append([node,cnt])
    print(''.join(map(str,preorder(st[0][0]))))
    print(''.join(map(str,postorder(st[0][0]))))
    print(''.join(map(str,inorder(st[0][0]))))
    if case!=n-1:
        print()