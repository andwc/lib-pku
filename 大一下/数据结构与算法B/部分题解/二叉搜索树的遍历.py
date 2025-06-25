class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def buildtree(p):
    n=len(p)
    stack=[]
    root=Treenode(p[0])
    stack.append(root)
    for i in range(1,n):
        cur=Treenode(p[i])
        if p[i]<stack[-1].val:
            stack[-1].left=cur
            stack.append(cur)
        else:
            pre = None
            while stack and p[i] > stack[-1].val:
                pre = stack.pop()
            if pre:
                pre.right = cur
            else:
                stack[-1].right = cur
            stack.append(cur)
            # pre=stack.pop()
            # while p[i]>pre.val:
            #     if stack:
            #         pre=stack.pop()
            #     else:
            #         pre.right=cur
            #         stack.append(cur)
            #         break
            # else:
            #     pre.left.right=cur
            #     stack.append(pre)
            #     stack.append(cur)
    return root
def hou(root):
    if not root:
        return []
    return hou(root.left)+hou(root.right)+[root.val]
def z(root):
    if not root:
        return []
    return z(root.left)+[root.val]+z(root.right)
def zhuan(qian,zhong):
    if not qian:
        return []
    i=0
    while zhong[i]!=qian[0]:
        i+=1
    return zhuan(qian[1:i+1],zhong[:i])+zhuan(qian[i+1:],zhong[i+1:])+[qian[0]]
n=int(input())
p=list(map(int,input().split()))
root=buildtree(p)
ans=hou(root)
# zhong=list(x for x in range(1,1+n))
# ans=zhuan(p,zhong)
e=z(root)
#print(' '.join(map(str,e)))
print(' '.join(map(str,ans)))
