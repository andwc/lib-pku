class tree:
    def __init__(self, value):
        self.value = value
        self.children = []
def show(tab,root):
    if not root:
        return
    for _ in range(tab):
        print('|     ',end='')
    print(root.value)
    n=len(root.children)
    for i in range(n):
        if root.children[i].value[0]=='d':
            continue
        for j in range(i,n):
            if root.children[j].value[0]=='d':
                root.children[i],root.children[j]=root.children[j],root.children[i]
                break
            elif root.children[i].value>root.children[j].value:
                root.children[i],root.children[j]=root.children[j],root.children[i]
            else:
                continue
    for i in root.children:
        if i.value[0]=='d':
            show(tab+1,i)
        else:
            show(tab,i)
    return
k=0
while True:
    k+=1
    root = tree('ROOT')
    st=[]
    while True:
        s=input()
        nd=tree(s)
        if s=='#':
            exit()
        if s=='*':
            if k!=1:
                print()
            print(f'DATA SET {k}:')
            show(0,root)
            break
        if s[0]=='f':
            if not st:
                root.children.append(nd)
            else:
                st[-1].children.append(nd)
        elif s[0]=='d':
            if st:
                st[-1].children.append(nd)
            else:
                root.children.append(nd)
            st.append(nd)
        elif s==']':
            st.pop()