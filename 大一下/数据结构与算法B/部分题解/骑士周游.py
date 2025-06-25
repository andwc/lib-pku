# pylint: skip-file
n=int(input())
sx,sy=map(int,input().split())
di=[(-1,-2),(1,-2),(-2,-1),(2,-1),(-2,1),(2,1),(-1,2),(1,2)]
board=[[-1]*n for _ in range(n)]
def degree(x,y,board):
    global n,di
    cnt=0
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny]==-1:
            cnt+=1
    return cnt
def dfs(x,y,cnt):
    global di,board,n
    if cnt==n*n:
        return True
    next_move=[]
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny]==-1:
            next_move.append((degree(nx,ny,board),nx,ny))
    next_move.sort()
    for _,nx,ny in next_move:
        board[nx][ny]=cnt
        if dfs(nx,ny,cnt+1):
            return True
        board[nx][ny]=-1
    return False
ans=0
board[sx][sy]=0
if dfs(sx,sy,1):
    print('success')
else:
    print('fail')