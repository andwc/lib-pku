a,b,k=map(int,input().split())
ma=[[0]*b for _ in range(a)]
for _ in range(k):
    r,s,p,t=map(int,input().split())
    r-=1
    s-=1
    d=p//2
    left=max(0,s-d)
    right=min(b-1,s+d)
    up=max(0,r-d)
    down=min(a-1,r+d)
    if t==0:
        for j in range(left, right + 1):
            for k in range(up, down + 1):
                ma[k][j]=-2
    for j in range(left,right+1):
        for k in range(up,down+1):
            if ma[k][j]!=-2:
                ma[k][j]+=1
num=-1
cnt=0
for k in range(b):
    for j in range(a):
        if ma[j][k]>num:
            num=ma[j][k]
            cnt=1
        elif ma[j][k]==num:
            cnt+=1
print(cnt)