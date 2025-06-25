import sys
shuru=sys.stdin.read()
n=len(shuru)
i=0
class treenode:
    def __init__(self,val):
        self.val=val
        self.children=[]

def classify(shuru):
    global i,n
    s=''
    while shuru[i]!='(':
        if shuru[i] not in ' \n':
            s+=shuru[i]
        i+=1
    st=1
    s+=shuru[i]
    i+=1
    while st:
        if shuru[i] == '(':
            st+=1
        elif shuru[i] == ')':
            st-=1
        if shuru[i] not in ' \n':
            s+=shuru[i]
        i+=1
    return s

def judge(target,root):
    if root is None:
        return False
    cnt=set()
    # def test(root):
    #     if not root:
    #         return []
    #     ans=[root.val]
    #     for i in root.children:
    #         ans+=test(i)
    #     return ans
    # print(test(root))
    def dfs(root,num):
        nonlocal cnt
        if root.children[0]==None and root.children[1]==None:
            cnt.add(num+root.val)
            return
        if root.children[0]:
            dfs(root.children[0],num+root.val)
        if root.children[1]:
            dfs(root.children[1],num+root.val)
        return
    dfs(root,0)
    return (target in cnt)

def deal(s):
    def f(i):
        nonlocal where, s
        if s[i]==')':
            where=i
            return
        st = []
        num=''
        while i < len(s) and s[i] != ')':
            if s[i] in '-0123456789':
                num+=s[i]
                i += 1
            elif s[i] == '(':
                if num:
                    st.append(treenode(int(num)))
                    num=''
                st[-1].children .append( f(i + 1) )
                i = where + 1
        where = i
        return st[0]

    target=''
    where=0
    while s[where] in '-0123456789':
        target+=s[where]
        where+=1
    target=int(target)
    where+=1
    root=f(where)
    where+=1
    if judge(target,root):
        print('yes')
    else:
        print('no')
    return
while i < n:
    while i < n and shuru[i] in ' \n':
        i += 1
    if i < n:
        deal(classify(shuru))