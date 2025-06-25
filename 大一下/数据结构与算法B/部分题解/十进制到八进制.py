n=int(input())
s=''
while n>=8:
    m=n%8
    s=str(m)+s
    n=n//8
if n!=0 or (n==0 and s==''):
    s=str(n)+s
print(s)