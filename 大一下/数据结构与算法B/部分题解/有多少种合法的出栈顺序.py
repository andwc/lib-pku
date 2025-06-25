from sys import setrecursionlimit
setrecursionlimit(1<<10)
def f(i,j):
    global ma
    #i is stack
    #j is nums_leave
    if i<0:
        return 0
    if ma[i][j]:
        return ma[i][j]
    if j==0 and i!=0:
        return 1
    ma[i][j]+=f(i-1,j)
    ma[i][j]+=f(i+1,j-1)
    return ma[i][j]
n=int(input())
ma=[[0]*(n+1) for _ in range(n+1)]
f(0,n)
print(ma[0][-1])