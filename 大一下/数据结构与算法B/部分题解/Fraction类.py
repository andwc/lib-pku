a,b,c,d=map(int,input().split())
def yue(n,m):
    if min(n,m)<2:
        return n,m
    for i in range(2,min(n,m)+1):
        if not m%i and not n%i:
            return yue(n//i,m//i)
    return n,m
zi,mu=yue(a*d+c*b,d*b)
print(f'{zi}/{mu}')