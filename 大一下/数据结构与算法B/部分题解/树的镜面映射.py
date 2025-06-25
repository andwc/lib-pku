n=int(input())
p=input().split()
class btn:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class tn:
    def __init__(self,val):
        self.val=val
        self.children=[]
def build(p):
    st=[]
    for i in p:
        if i[1]=='0':
            node=btn(i[0])
            if not st:
                root=node
                st.append([node,0])
            else:
                if st[-1][-1]==0:
                    st[-1][0].left=node
                    st[-1][-1]=1
                else:
                    st[-1][0].right=node
                    st.pop()
                st.append([node,0])
        else:
            if i[0]=='$':
                if st[-1][-1]==0:
                    st[-1][-1]=1
                else:
                    st.pop()
                continue
            node=btn(i[0])
            if st[-1][-1] == 0:
                st[-1][0].left = node
                st[-1][-1] = 1
            else:
                st[-1][0].right = node
                st.pop()
    return root
def postorder(root):
    if root is None:
        return []
    return [root.val] + postorder(root.left) + postorder(root.right)
def transform(root):
    if root is None:
        return None
    st=[]
    rt=tn(root.val)
    cur=root.left
    while cur:
        st.append(transform(cur))
        cur=cur.right
    rt.children=st
    return rt
def postorder2(root):
    if root is None:
        return []
    ans=[root.val]
    for i in root.children:
        ans.extend(postorder2(i))
    return ans
def fan(root):
    if root is None:
        return []
    root.children=root.children[::-1]
    for i in root.children:
        fan(i)
    return root
def bfs(root):
    from collections import deque
    q=deque()
    q.append(root)
    ans=[]
    while q:
        node=q.popleft()
        q.extend(node.children)
        ans.append(node.val)
    return ' '.join(map(str,ans))
root=build(p)
# print(' '.join(map(str,postorder(root))))
root=transform(root)
# print(' '.join(map(str,postorder2(root))))
root=fan(root)
print(bfs(root))