t=int(input())
for i in range(t):
    n=int(input())
    hao=set()
    judge=0
    for j in range(n):
        s=input()
        if s in hao:
            judge=1
        hao.add(s)
    if judge:
        print('NO')
        continue
    for j in hao:
        if judge:
            break
        cur=''
        for k in j[:-1]:
            cur+=k
            if cur in hao:
                judge=1
                break
    if judge:
        print('NO')
    else:
        print('YES')