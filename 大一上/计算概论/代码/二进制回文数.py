num=int(input())
a=bin(num)[2:]
b=a[::-1]
if a==b:
    print('Yes')
else:
    print('No')