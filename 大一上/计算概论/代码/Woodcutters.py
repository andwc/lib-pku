n=int(input())
x=[]
h=[]
for i in range(n):
    shuru=input().split()
    x.append(int(shuru[0]))
    h.append(int(shuru[1]))
if n==1:
    answer=1
else:
    answer=2
c=True
for i in range(1,n-1):
    m=x[i]
    if x[i]-h[i]>x[i-1]:
        answer+=1
        continue
    if x[i]+h[i]<x[i+1]:
        answer+=1
        x[i]+=h[i]
print(answer)