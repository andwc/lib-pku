# class treenode:
#     def __init__(self,val):
#         self.val=val
#         self.children=[]
# def preorder(root):
#     print(root.val,end='')
#     for child in root.children:
#         preorder(child)
# def postorder(root):
#     for child in root.children:
#         postorder(child)
#     print(root.val,end='')
# def show(root):
#     preorder(root)
#     print()
#     postorder(root)
# s=input()
# if len(s)==1:
#     print(s)
#     print(s)
#     exit()
# stack=[]
# for i in s:
#     if i not in '(),':
#         node=treenode(i)
#         if stack:
#             stack[-1].children.append(node)
#         stack.append(node)
#     elif i==',' or i==')':
#         stack.pop()
# root=stack.pop()
# show(root)
class treenode:
    def __init__(self,val):
        self.val=val
        self.children=[]
def preorder(root):
    if not root:
        return []
    ans=[root.val]
    for i in root.children:
        ans.extend(preorder(i))
    return ans
def postorder(root):
    if not root:
        return []
    ans=[]
    for i in root.children:
        ans.extend(postorder(i))
    return ans+[root.val]
def show(root):
    print(''.join(preorder(root)))
    print(''.join(postorder(root)))
    return
s=input()
where=0
def f(i):
    global where,s
    st=[]
    while i<len(s) and s[i]!=')':
        if s[i]==',':
            i+=1
        elif 'A'<=s[i]<='Z':
            st.append(treenode(s[i]))
            i+=1
        elif s[i]=='(':
            st[-1].children=f(i+1)
            i=where+1
    where=i
    return st
root=f(0)[0]
show(root)