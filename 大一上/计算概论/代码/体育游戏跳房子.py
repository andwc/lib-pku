from collections import deque
def bfs(n,m):
    global step,p
    visited=set()
    queue=deque()
    queue.append((n,''))
    visited.add(n)
    judge=1
    while queue and judge:
        for _ in range(len(queue)):
            x,path=queue.popleft()
            x1=x*3
            if x1 not in visited:
                queue.append((x1,path+'H'))
                visited.add(x1)
            x2=x//2
            if x2 not in visited:
                queue.append((x2,path+'O'))
                visited.add(x2)
            if x1==m:
                judge=0
                step=len(path)+1
                if p:
                    p=min(p,path+'H')
                else:
                    p=path+'H'
            if x2==m:
                judge=0
                step=len(path)+1
                if p:
                    p=min(p,path+'O')
                else:
                    p=path+'O'
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    step=0
    p=''
    bfs(n,m)
    print(step)
    print(p)