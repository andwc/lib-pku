while True:
    try:
        s=input()
        n=len(s)
        p=[]
        q=[]
        for i in range(n):
            if s[i]=='(':
                p.append(i)
            elif s[i]==')':
                if p:
                    p.pop()
                else:
                    q.append(i)
        ns=''
        for i in range(n):
            if i in p:
                ns+='$'
            elif i in q:
                ns+='?'
            else:
                ns+=' '
        print(s)
        print(ns)
    except EOFError:
        break