from copy import deepcopy
m=[]
for _ in range(5):
    m.append(list(map(int,input().split())))
ma=deepcopy(m)
di=[(1,0),(0,1),(-1,0),(0,-1)]
ans=[[0]*6 for _ in range(5)]
def turn(i,j):
    global ma
    ma[i][j]=1-ma[i][j]
def change(i,j):
    global ans
    turn(i,j)
    ans[i][j]=1-ans[i][j]
    for dx,dy in di:
        nx,ny=i+dx,j+dy
        if 0<=nx<5 and 0<=ny<6:
            turn(nx,ny)
def solve():
    global ma,m,ans
    for i in range(1,5):
        for j in range(6):
            if ma[i-1][j]:
                change(i,j)
    if 1 in ma[-1]:
        ma=deepcopy(m)
        ans=[[0]*6 for _ in range(5)]
        return
    for i in ans:
        for j in i:
            print(j,end=' ')
        print()
    exit()
for i in range(64):
    if i%2==1:
        change(0,0)
    if (i%4)//2==1:
        change(0,1)
    if (i%8)//4==1:
        change(0,2)
    if (i%16)//8==1:
        change(0,3)
    if (i%32)//16==1:
        change(0,4)
    if (i%64)//32==1:
        change(0,5)
    solve()