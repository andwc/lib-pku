num=int(input())
a=[None]*20
a[0]=a[1]=1
for i in range(2,20):
    a[i]=a[i-1]+a[i-2]
for i in range(num):
    s=int(input())
    print(a[s-1])