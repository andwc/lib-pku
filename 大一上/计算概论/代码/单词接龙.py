from copy import copy
def connect(s1,s2):
    k=0
    for i in s1:
        if i==s2[k]:
            k+=1
        else:
            k=0
    if k==0 or k==len(s1):
        return None
    return s1+s2[k::]
def f(s,ans):
    global l,a
    print(s,a)
    if not s:
        if len(ans)>l:
            l=len(ans)
            a=ans
        return
    for i in s:
        if connect(ans,i):
            print(0)
            s1=copy(s)
            s1.remove(i)
            f(s1,connect(ans, i))
    else:
        if len(ans)>l:
            l=len(ans)
            a=ans
n=int(input())
s=[]
for i in range(n):
    s.append(input())
e=input()
s1=s[::]
s.extend(s1)
a=''
for i in s:
    if i[0]==e:
        a+=i
        l=len(a)
        s1=copy(s)
        s1.remove(i)
        f(s1,a)
print(l,a)