n=int(input())
s=input()
class treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def judge(s):
    if '1' in s and '0' in s:
        return 'F'
    if '1' not in s:
        return 'B'
    return 'I'
def build(s):
    n=len(s)
    root=treenode(judge(s))
    if n==1:
        return root
    root.left=build(s[:n//2])
    root.right=build(s[n//2:])
    return root
def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right)+[root.val]
print(''.join(postorder(build(s))))