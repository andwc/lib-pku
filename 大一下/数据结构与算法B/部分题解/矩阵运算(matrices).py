row,col=map(int,input().split())
a=[None]*row
for j in range(row):
    a[j]=list(map(int,input().split()))
row,col=map(int,input().split())
b=[None]*row
for j in range(row):
    b[j]=list(map(int,input().split()))
row,col=map(int,input().split())
if len(a[0])!=len(b) or len(a)!=row or len(b[0])!=col:
    print("Error!")
    for i in range(row):
        s=input()
    exit()
for i in range(row):
    s=list(map(int,input().split()))
    for j in range(col):
        cnt=0
        for k in range(len(b)):
            cnt+=a[i][k]*b[k][j]
        print(s[j]+cnt,end=' ')
    print()