s=input()
from math import log
m=int(log(len(s),2))
s1=''
for i in range(m+1):
    s1+=s[2**i-1]
l=len(s1)
s2=s1[::-1]
if l%2==0:
    for i in range(l//2):
        print(s1[i],s2[i],sep='',end='')
else:
    for i in range(l//2):
        print(s1[i],s2[i],sep='',end='')
    print(s1[l//2])