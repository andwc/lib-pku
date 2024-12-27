a=input()
shuru=['o']*(len(a))
for i in range(len(a)):
    shuru[i]=a[i]
    if ord(shuru[i])<97:
        shuru[i]=chr(ord(shuru[i])+32)
zimu=[]
shuzi=[]
zimu.append(shuru[0])
num=1
if len(shuru)==1:
    shuzi.append(num)
for i in range(0,len(shuru)-1):
    if shuru[i]==shuru[i+1]:
        num+=1
    else:
        shuzi.append(num)
        zimu.append(shuru[i+1])
        num=1
    if i==len(shuru)-2:
        if shuru[i]==shuru[i+1]:
            shuzi.append(num)
        else:
            shuzi.append(num)
for i in range(len(zimu)):
    print('(',zimu[i],',',shuzi[i],')',sep='',end='')