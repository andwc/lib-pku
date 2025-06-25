t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    tree=[[None,None,None] for _ in range(n)]
    for i in range(n):
        x,y,z=map(int,input().split())
        if y!=-1:
            tree[x][1]=y
            tree[y][0] = x
        if z!=-1:
            tree[x][2]=z
            tree[z][0]=x
    for i in range(m):
        shuru=list(map(int,input().split()))
        if shuru[0]==1:
            f1,f2=tree[shuru[1]][0],tree[shuru[2]][0]
            if f1==f2:
                tree[f1][1],tree[f1][2]=tree[f1][2],tree[f1][1]
            else:
                tree[shuru[1]][0],tree[shuru[2]][0]=f2,f1
                if tree[f1][1]==shuru[1]:
                    tree[f1][1]=shuru[2]
                else:
                    tree[f1][2]=shuru[2]
                if tree[f2][1]==shuru[2]:
                    tree[f2][1]=shuru[1]
                else:
                    tree[f2][2]=shuru[1]
        else:
            cur=shuru[1]
            while tree[cur][1]:
                cur=tree[cur][1]
            print(cur)