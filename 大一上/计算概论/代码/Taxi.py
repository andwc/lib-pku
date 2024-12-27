n=int(input())
child=list(map(int,input().split()))
answer=0
a1=child.count(1)
a2=child.count(2)
a3=child.count(3)
a4=child.count(4)
answer+=a4+a3+int(a2/2)
a1-=a3
a2-=int(a2/2)*2
#print(a1,a2,a3,a4,answer)
if a2!=0:
    a1-=2
    answer+=1
if a1>0:
    answer+=int(a1/4)
    if a1%4!=0:
        answer+=1
print(answer)
