import math
num=int(input())
a=[]
a.append(2)
for i in range(3,int(math.sqrt(num))+2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        a.append(i)
b=[]
k=0
#print(a)
while num!=1 and k<len(a):
    if num%a[k]==0:
        num=int(num/a[k])
        b.append(a[k])
        continue
    #print(k)
    k+=1
    #print(k)
if num!=1:#解决不全的情况
    b.append(num)
#print(b)
for i in range(1,len(b)):
    if b[i]==b[i-1]:
        answer=0
        break
else:
    if len(b)%2==0:
        answer=1
    else:
        answer=-1
print(answer)