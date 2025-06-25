# n=int(input())
# ind=[set(map(int,input().split()[1:]))for _ in range(n)]
# m=int(input())
# for _ in range(m):
#     s=list(map(int,input().split()))
#     i=0
#     while s[i]!=1:i+=1
#     ans=ind[i].copy()
#     for j in range(i):
#         if s[j]==-1:ans-=ind[j]
#     for j in range(i+1,n):
#         if s[j]==1:ans&=ind[j]
#         elif s[j]==-1:ans-=ind[j]
#     if ans:print(' '.join(map(str,sorted(ans))))
#     else:print('NOT FOUND')
n=int(input())
d=[None]*n
for i in range(n):
    d[i]=set(map(int,input().split()[1:]))
m = int(input())
for _ in range(m):
    p=list(input().split())
    i=0
    while p[i]!='1':
        i+=1
    ans=d[i].copy()
    for j in range(i):
        if p[j]=='-1':
            ans-=d[j]
    for j in range(i+1,n):
        if p[j]=='1':
            ans&=d[j]
        elif p[j]=='-1':
            ans-=d[j]
    if ans:
        print(' '.join(map(str,sorted(ans))))
    else:
        print('NOT FOUND')