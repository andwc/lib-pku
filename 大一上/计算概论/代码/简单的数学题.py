from math import log
t=int(input())
def solve(n):
    he=n*(n+1)//2
    judge=log(n,2)
    for i in range(int(judge)+1):
        he-=2*2**i
    return he
for _ in range(t):
    n=int(input())
    print(solve(n))