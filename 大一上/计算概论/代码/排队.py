from collections import deque
n,d=map(int,input().split())
h=deque()
for i in range(n):
    h.append(int(input()))
while h:
    l=[]
    da=h[0]
    xiao=h[0]
    for i in range(len(h)):
        x=h.popleft()
        if abs(da-x)<=d and abs(xiao-x)<=d:
            l.append(x)
        else:
            h.append(x)
        if da<x:
            da=x
        if xiao>x:
            xiao=x
    l.sort()
    for i in l:
        print(i)