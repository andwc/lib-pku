n=int(input())
a=[[None for _ in range(n)] for _ in range(n)]
d,i,j,s=0,0,0,1
a[0][0]=1
def t(a,i,j,n,d,s):
    k=1
    if d%4==0:
        while True:
            if j+k<n:
                if a[i][j+k]==None:
                    a[i][j+k]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i,j+k,n,d,s+k
    elif d%4==1:
        while True:
            if i+k<n:
                if a[i+k][j]==None:
                    a[i+k][j]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i+k,j,n,d,s+k
    elif d%4==2:
        while True:
            if j-k>-1:
                if a[i][j-k]==None:
                    a[i][j-k]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i,j-k,n,d,s+k
    elif d%4==3:
        while True:
            if i-k<n:
                if a[i-k][j]==None:
                    a[i-k][j]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i-k,j,n,d,s+k
for _ in range(2*n-1):
    a,i,j,n,d,s=t(a,i,j,n,d,s)
for i in range(n):
    for j in a[i]:
        print(j,end=" ")
    print()