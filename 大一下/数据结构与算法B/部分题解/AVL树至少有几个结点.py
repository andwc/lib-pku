n=int(input())
if n==1:
    print('1')
    exit()
if n==2:
    print('2')
    exit()
d=[0]*n
d[0]=1
d[1]=2
for i in range(2,n):
    d[i]=1+d[i-1]+d[i-2]
print(d[-1])