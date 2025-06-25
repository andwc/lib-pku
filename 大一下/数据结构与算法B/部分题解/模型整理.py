n=int(input())
p=[]
for _ in range(n):
    a,b=input().split('-')
    c=float(b[:-1])
    if b[-1]=='B':
        c*=1000
    p.append((a,c,b))
p.sort()
s=''
ss=''
for i in range(n):
    if s!=p[i][0]:
        if ss:
            print(ss)
            ss=''
        s=p[i][0]
        print(f'{s}:',end='')
    if not ss:
        ss+=' '+p[i][2]
    else:
        ss+=', '+p[i][2]
print(ss)