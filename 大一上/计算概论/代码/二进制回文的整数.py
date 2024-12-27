n=int(input())
m=bin(n)
for i in range(len(m)):
    if m[i]=='b':
        m=m[i+1:]
        break
for i in range(len(m)//2+1):
    if m[i]!=m[-i-1]:
        print('No')
        exit()
print('Yes')