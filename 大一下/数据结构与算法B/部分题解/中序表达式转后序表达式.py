def turn(s):
    fuhao={'+':1,'-':1,'*':2,'/':2}
    stack=[]
    ans=[]
    num=''
    for i in s:
        if i in '0123456789.':
            num+=i
        else:
            if num:
                ans.append(num)
                num=''
            if i in '+-*/':
                while stack and stack[-1] in '+-*/' and fuhao[i]<=fuhao[stack[-1]]:
                    ans.append(stack.pop())
                stack.append(i)
            elif i=='(':
                stack.append(i)
            elif i==')':
                while stack and stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
    if num:
        ans.append(num)
    while stack:
        ans.append(stack.pop())
    return ' '.join(str(i) for i in ans)
case=int(input())
for _ in range(case):
    s=input()
    print(turn(s))
# class treenode:
#     def __init__(self, val):
#         self.val=val
#         self.left=None
#         self.right=None
# def postorder(root):
#     if root is None:
#         return
#     postorder(root.left)
#     postorder(root.right)
#     print(root.val,end=' ')
#     return
# def build_tree(s):
#     def f(i):
#         nonlocal where,s
#         num=''
#         left_node=None
#         while i<len(s) and s[i]!=')':
#             if s[i]=='(':
#                 left_node=f(i+1)
#                 i=where+1
#             elif s[i] in '0123456789.':
#                 num+=s[i]
#                 i+=1
#             elif s[i] in '+-*/':
#                 nd=treenode(s[i])
#                 if left_node:
#                     nd.left=left_node
#                     left_node=None
#                 else:
#                     nd.left=treenode(num)
#                     num=''
#                 nd.right=f(i+1)
#                 i=where+1
#         where=i
#         if num:
#             return treenode(num)
#         return left_node if left_node else nd
#     where=0
#     root=f(0)
#     return root
# case=int(input())
# for _ in range(case):
#     root=build_tree(input())
#     postorder(root)
#     print()