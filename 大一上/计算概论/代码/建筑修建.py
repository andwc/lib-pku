n,m=map(int,input().split())
s=[]
def ha(a,b):
    global m,s
    for i in range(max(0,a-b+1),1+min(m-b,a)):
        s.append((i,i+b))
for i in range(n):
    a,b=map(int,input().split())
    ha(a,b)
s.sort(key=lambda x:(x[1],x[0]))
e=s[0][1]
ans=1
for i in range(len(s)):
    if s[i][0]>=e:
        ans+=1
        e=s[i][1]
print(ans)