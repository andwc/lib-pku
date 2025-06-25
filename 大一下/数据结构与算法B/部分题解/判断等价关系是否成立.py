class bcj:
    def __init__(self):
        self.f=[x for x in range(26)]
    def find(self,a):
        st=[]
        while self.f[a]!=a:
            st.append(a)
            a=self.f[a]
        for i in st:
            self.f[i]=a
        return a
    def issameset(self,a,b):
        return self.find(a)==self.find(b)
    def union(self,a,b):
        fa=self.find(a)
        fb=self.find(b)
        self.f[fa]=fb
        return
n=int(input())
q=bcj()
p=[]
ans=0
for i in range(n):
    s=input()
    if s[1]=='=':
        q.union(int(ord(s[0])-ord('a')),int(ord(s[3])-ord('a')))
    else:
        p.append((int(ord(s[0])-ord('a')),int(ord(s[3])-ord('a'))))
        if s[0]==s[3]:
            ans=1
if ans:
    print('False')
    exit()
for x,y in p:
    if q.issameset(x,y):
        ans=1
if ans:
    print('False')
else:
    print('True')