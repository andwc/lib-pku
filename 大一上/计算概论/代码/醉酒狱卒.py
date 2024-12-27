num=int(input())
for i in range(num):
    n=int(input())
    a=[0]*n
    answer=0
    for j in range(0,n):
        for k in range(j,n,j+1):
            if a[k]==0:
                a[k]=1
            else:
                a[k]=0
    for j in range(n):
        if a[j]==1:
            answer+=1
    print(answer)