n,m=map(int,input().split())
shuru=input().split()
a=[]
answer=0
for i in range(n):
    a.append(int(shuru[i]))
for i in range(m):
    if min(a)<=0:
        answer+=min(a)
        a.remove(min(a))
    else:
        break
if answer>=0:
    print(0)
else:
    print(-answer)