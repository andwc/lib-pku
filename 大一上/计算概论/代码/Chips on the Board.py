def deal(n1,row,col):
    r=min(row)
    c=min(col)
    sr=sum(row)
    sc=sum(col)
    answer=0
    return (min(n1*r+sc,n1*c+sr))
n=int(input())
for i in range(n):
    n1=int(input())
    row=list(map(int,input().split()))
    col=list(map(int,input().split()))
    answer=deal(n1,row,col)
    print(answer)
