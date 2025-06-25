n,m=map(int,input().split())
p=list(map(int,input().split()))
M=65536
j=0
def judge(a,b):
    c=bin(a)
    c=c[:1:-1]
    if len(c)<=b:
        return 0
    else:
        return int(c[b])
for i in range(m):
    s,num=input().split()
    num=int(num)
    if s=='C':
        j+=num
        j%=M
    elif s=='Q':
        cnt=0
        for ii in range(n):
            cnt+=judge((p[ii]+j)%M,num)
        print(cnt)