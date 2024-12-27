def fanyi(b):
    a=b[:-1:]
    if b[-1]=='M':
        return float(a)
    if b[-1]=='B':
        if '.' in a:
            c,d=a.split('.')
            if len(d)<3:
                for i in range(3-len(d)):
                    d+='0'
            return float(int(c+d))
        else:
            return float(int(a)*1000)
def f(b):
    if b<1000:
        a=b%1000
        if int(a)==a:
            return str(int(a))+'M'
        return str(b)+'M'
    else:
        s=str(int(b//1000))
        a=int(b%1000)
        if a>=100:
            if a%100==0:
                s+='.'+str(int(a//100))
            elif a%10==0:
                s+='.'+str(int(a//10))
            else:
                s+='.'+str(a)
        elif a>=10:
            if a%10==0:
                s+='.'+'0'+str(a//10)
            else:
                s+='.'+str(a)
        elif a!=0:
            s+='.'+str(a)
        return s+'B'
#print(f(271800.0))
n=int(input())
m=set()
m1=[]
l=[]
for i in range(n):
    a,b=map(str,input().split('-'))
    l.append((a,fanyi(b)))
    if a not in m:
        m.add(a)
        m1.append(a)
m1.sort()
for i in range(len(m1)):
    li=[]
    for j in range(len(l)):
        if l[j][0]==m1[i]:
            li.append(l[j][1])
    li.sort()
    print(m1[i],':',sep='',end='')
    for j in range(len(li)-1):
        print(' ',f(li[j]),',',sep='',end='')
    print(' ', f(li[-1]),  sep='', end='')
    print()