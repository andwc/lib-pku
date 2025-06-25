case=int(input())
for _ in range(case):
    n=int(input())
    p=[]
    for i in range(n):
        a,b=input().split()
        if a=='1':
            p.append(int(b))
        elif a=='2':
            if p:
                if b=='0':
                    p.pop(0)
                else:
                    p.pop()
    if p:
        for i in p:
            print(i,end=' ')
        print()
    else:
        print('NULL')