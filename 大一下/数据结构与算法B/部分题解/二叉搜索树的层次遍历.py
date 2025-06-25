p=list(map(int,input().split()))
n=len(p)
class treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(p,n):
    root=treenode(p[0])
    visited=set()
    visited.add(root.val)
    for i in range(1,n):
        if p[i] not in visited:
            visited.add(p[i])
        else:
            continue
        node=treenode(p[i])
        cur=root
        while 1:
            if cur.val<p[i]:
                if cur.right:
                    cur=cur.right
                    continue
                else:
                    cur.right=node
                    break
            else:
                if cur.left:
                    cur=cur.left
                    continue
                else:
                    cur.left=node
                    break
    return root

def ceng(root):
    from collections import deque
    queue=deque()
    queue.append(root)
    ans=[]
    while queue:
        for i in range(len(queue)):
            x=queue.popleft()
            ans.append(str(x.val))
            if x.left:
                queue.append(x.left)
            if x.right:
                queue.append(x.right)
    return ans
root=build_tree(p,n)
ans=ceng(root)
print(' '.join(ans))