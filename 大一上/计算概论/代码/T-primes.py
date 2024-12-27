import math
def zhishu(u):
    a=[True]*(u+1)
    a[0]=False
    a[1]=False
    z=[]
    for i in range(2,u+1):
        if a[i]:
            z.append(i)
        for p in z:
            if p*i>u:
                break
            a[p*i]=False
            if i%p==0:
                break
    return z
num=int(input())
n=list(map(int,input().split()))
z=set(zhishu(10**6))
#print(z)
for i in range(num):
    if n[i]==1:
        print('NO')
    else:
        b = int(math.sqrt(n[i]))
        if b * b != n[i]:
            print('NO')
        elif b in z:
            print('YES')
        else:
            print('NO')
