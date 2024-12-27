dui=[]
mini=float('inf')
judge=0
while True:
    try:
        shuru=input()
        if shuru[1]=='u':
            s=shuru.split()
            a=int(s[1])
            if mini>a:
                mini=a
                judge=1
            elif mini==a:
                judge+=1
            dui.append(a)
        if shuru[1]=='o' and dui:
            b=dui.pop()
            if b==mini:
                judge-=1
                if not judge and dui:
                    mini=min(dui)
                    judge=1
        if shuru[0]=='m' and dui:
            print(mini)
    except EOFError:
        break