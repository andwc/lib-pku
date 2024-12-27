directions=[[1,0],[-1,0],[0,-1],[0,1]]
def main():
    n,m=map(int,input().split())
    ma=[]
    ma.append([2 for _ in range(m+2)])
    for i in range(1,n+1):
        ma.append([2]+list(map(int,input().split()))+[2])
    ma.append([2 for _ in range(m+2)])
    print(bfs(ma,1,1))
def bfs(ma,i,j):
    stack=[(i,j,0)]
    visited=set([(i,j)])
    while stack:
        x,y,step=stack.pop(0)
        if ma[x][y]==1:
            return step
        for dx,dy in directions:
            if (x+dx,y+dy) not in visited and ma[x+dx][y+dy]!=2:
                stack.append((x+dx,y+dy,step+1))
                visited.add((x+dx,y+dy))
    return 'NO'
main()