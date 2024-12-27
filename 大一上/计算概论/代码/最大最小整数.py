def h(x,y):
    if x+y>y+x:
        return x
    else:
        return y
def hh(x,y):
    if x+y>y+x:
        return y
    elif x+y<y+x:
        return x
    else:
        return y
num=int(input())
n=input().split()#str list
n1=n[:]
n2=n[:]
s=''
da=''
xiao=''
while n1:
    s=''
    for i in range(len(n1)):
        s=h(s,n1[i])
    #print(s)
    da+=s
    n1.remove(s)
while n2:
    s='999999999999999999999999999999999999999999999999999999999999999999999999999999999'
    for i in range(len(n2)):
        s=hh(s,n2[i])
    #print(s)
    xiao+=s
    n2.remove(s)
print(da,xiao)