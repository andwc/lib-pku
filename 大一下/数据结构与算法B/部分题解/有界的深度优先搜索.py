n,m,L=map(int,input().split())
used=[False]*n
bian=set()
for _ in range(m):
    a,b=map(int,input().split())
    bian.add((a,b))
start=int(input())
print(start,end=' ')
used[start]=True
def dls(start,cur):
    global n,bian,L,used
    if cur==L:
        return
    cur+=1
    for i in range(n):
        if used[i]:
            continue
        if (start,i) in bian or (i,start) in bian:
            print(i,end=' ')
            used[i]=True
            dls(i,cur)
dls(start,0)