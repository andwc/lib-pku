n=int(input())
if n==0:
    print(-1,0)
    exit()
if n==1:
    print(0,1)
    s=input()
    exit()
if n==2:
    print(1,1)
    s=input()
    s=input()
    exit()
tree=[[-1,-1,-1] for i in range(n)]
leaves=0
for i in range(n):
    l,r=map(int,input().split())
    if l==-1 and r==-1:
        leaves+=1
    tree[i][1]=l
    tree[i][2]=r
    if r!=-1:
        tree[r][0]=i
    if l!=-1:
        tree[l][0]=i
from collections import deque
queue=deque()
for i in range(n):
    if tree[i][0]==-1:
        root=i
        break
queue.append(root)
h=0
while queue:
    h+=1
    for i in range(len(queue)):
        x=queue.popleft()
        if tree[x][1]!=-1:
            queue.append(tree[x][1])
        if tree[x][2]!=-1:
            queue.append(tree[x][2])
print(h-1,leaves)