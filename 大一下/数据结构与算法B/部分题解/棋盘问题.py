from sys import setrecursionlimit
setrecursionlimit(1000)
def solve(n,m,k,current,col,ans):
    if k>n-current:
        return 0
    if k==0:
        return 1
    for i in m[current]:
        if i in col:
            continue
        else:
            col.add(i)
            ans+=solve(n,m,k-1,current+1,col,0)
            col.remove(i)
    ans+=solve(n,m,k,current+1,col,0)
    return ans
def main():
    n,k=map(int,input().split())
    if n==-1==k:
        exit()
    m=[[]for _ in range(n)]
    for i in range(n):
        s=input()
        for j in range(n):
            if s[j]=='#':
                m[i].append(j)
    col=set()
    print(solve(n,m,k,0,col,0))
while True:
    main()