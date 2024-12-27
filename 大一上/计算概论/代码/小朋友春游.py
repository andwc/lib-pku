n=int(input())
shuru=input().split()
a=[]
b=[]
wuru=[]
diushi=[]
for i in range(n):
    a.append(i+1)
#print(a)
for i in range(len(shuru)):
    if int(shuru[i]) not in a:
        wuru.append(int(shuru[i]))
    else:
        b.append(int(shuru[i]))
#print(b,wuru)
wuru.sort(key=lambda x: int(x))
for i in range(len(a)):
    if a[i] not in b:
        diushi.append(int(a[i]))
diushi.sort(key=lambda x: int(x))
for i in range(len(diushi)):
    print(diushi[i],end=' ')
print()
for i in range(len(wuru)):
    print(wuru[i],end=' ')
