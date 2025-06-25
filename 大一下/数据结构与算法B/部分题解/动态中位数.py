import bisect
t=int(input())
for _ in range(t):
    p=list(map(int,input().split()))
    n=len(p)
    print((n+1)//2)
    