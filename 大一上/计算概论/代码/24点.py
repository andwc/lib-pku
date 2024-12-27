m=int(input())
for i in range(m):
    a=input().split()
    for j in range(4):
        a[j]=int(a[j])
    if a[0]+a[1]+a[2]+a[3]==24 or a[0]+a[1]+a[2]-a[3]==24 or a[0]+a[1]-a[2]+a[3]==24 or a[0]+a[1]-a[2]-a[3]==24 or a[0]-a[1]+a[2]+a[3]==24 or a[0]-a[1]+a[2]-a[3]==24 or a[0]-a[1]-a[2]+a[3]==24 or a[0]-a[1]-a[2]-a[3]==24 or 0-a[0]+a[1]+a[2]+a[3]==24 or 0-a[0]+a[1]+a[2]-a[3]==24 or 0-a[0]+a[1]-a[2]+a[3]==24 or 0-a[0]+a[1]-a[2]-a[3]==24 or 0-a[0]-a[1]+a[2]+a[3]==24 or 0-a[0]-a[1]+a[2]-a[3]==24 or 0-a[0]-a[1]-a[2]+a[3]==24 or 0-a[0]-a[1]-a[2]-a[3]==24:
        print('YES')
    else:
        print('NO')