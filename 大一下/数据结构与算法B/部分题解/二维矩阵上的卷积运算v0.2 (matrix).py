row,col,r,c=map(int,input().split())
a=[None]*row
b=[None]*r
for i in range(row):
    a[i]=list(map(int,input().split()))
for i in range(r):
    b[i]=list(map(int,input().split()))
for i in range(row-r+1):
    for j in range(col-c+1):
        cnt=0
        for k in range(r):
            for t in range(c):
                cnt+=a[i+k][j+t]*b[k][t]
        print(cnt,end=' ')
    print()