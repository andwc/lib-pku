def check(s,ss):
    if len(s)!=len(ss):
        return False
    stack=[]
    j=0
    for i in ss:
        while (not stack or stack[-1]!=i) and j<len(s):
            stack.append(s[j])
            j+=1
        if not stack or stack[-1]!=i:
            return False
        stack.pop()
    return True
s=input()
while 1:
    try:
        ss=input()
        if check(s,ss):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break