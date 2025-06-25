n=int(input())
di=[(-1,-2),(1,-2),(-2,-1),(2,-1),(-2,1),(2,1),(-1,2),(1,2)]
def dfs(p,q,x,y,path,visited,di,cnt):
    global ans
    if cnt==p*q:
        ans=path[:]
        return
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<p and 0<=ny<q and not visited[nx][ny]:
            visited[nx][ny]=1
            path.append(chr(ny+65)+str(nx+1))
            cnt+=1
            dfs(p,q,nx,ny,path,visited,di,cnt)
            if ans:
                return
            cnt-=1
            path.pop()
            visited[nx][ny]=0
    return
for ii in range(n):
    print(f'Scenario #{ii+1}:')
    p,q=map(int,input().split())
    visited=[[0]*q for _ in range(p)]
    ans=[]
    visited[0][0]=1
    path=[chr(65)+str(1)]
    dfs(p,q,0,0,path,visited,di,1)
    if ans:
        print(''.join(ans))
    else:
        print('impossible')
    print()