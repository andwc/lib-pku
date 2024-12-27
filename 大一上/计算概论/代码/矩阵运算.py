row=[None]*3
col=[None]*3
for i in range(3):
    shuru=input().split()
    row[i]=int(shuru[0])
    col[i]=int(shuru[1])
    if i==0:
        a=[[0 for _ in range(col[i])] for _ in range(row[i])]
    if i == 1:
        b = [[0 for _ in range(col[i])] for _ in range(row[i])]
    if i == 2:
        c = [[0 for _ in range(col[i])] for _ in range(row[i])]
    for j in range(row[i]):
        hang=input().split()
        for k in range(col[i]):
            if i==0:
                a[j][k]=int(hang[k])
            elif i==1:
                b[j][k]=int(hang[k])
            elif i==2:
                c[j][k]=int(hang[k])
if col[0]!=row[1] or row[0]!=row[2] or col[1]!=col[2]:
    print('Error!')
else:
    d=[[0 for _ in range(col[2])]for _ in range(row[2])]
    for i in range(row[0]):
        for j in range(col[1]):
            for ii in range(row[1]):
                    d[i][j]+=a[i][ii]*b[ii][j]
            d[i][j]+=c[i][j]
    for i in range(row[2]):
        for j in range(col[2]):
            print(d[i][j],end=' ')
        print()