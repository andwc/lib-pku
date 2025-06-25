def solve(a,b):
    l,r=0,0
    while (a!=1 or b!=1):
        if a>b:
            if a%b!=0:
                l+=(a//b)
                a=a%b
            else:
                l+=(a//b)-1
                a=b
        else:
            if b%a!=0:
                r+=(b//a)
                b=b%a
            else:
                r+=(b//a)-1
                b=a
    return l,r
case=int(input())
for i in range(case):
    print(f'Scenario #{i+1}:')
    a,b=map(int,input().split())
    l,r=solve(a,b)
    print(l,r)
    if i!=case:
        print()