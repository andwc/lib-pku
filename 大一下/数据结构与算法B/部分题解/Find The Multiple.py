from collections import deque
q=deque()
while 1:
    n=int(input())
    if n==0:
        break
    q.append(1)
    while 1:
        x=q.popleft()
        if x%n==0:
            print(x)
            q.clear()
            break
        else:
            q.append(x*10)
            q.append(x*10+1)
