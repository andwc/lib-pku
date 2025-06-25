s=input()
n=len(s)
if n==1:
    print(s)
    exit()
ns=s[0]
for i in range(n):
    if s[i]=='+' or s[i]=='-':
        ns+=' '+s[i+2]+' '+s[i]
print(ns)