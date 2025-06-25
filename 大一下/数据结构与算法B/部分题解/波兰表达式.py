s=list(map(str,input().split()))
fuhao={'+','-','*','/'}
stack=[]
while s:
    x=s.pop()
    if x in fuhao:
        a=stack.pop()
        b=stack.pop()
        stack.append(float(eval(str(a)+x+str(b))))
    else:
        stack.append(float(x))
print('{:.6f}'.format(float(stack[0])))