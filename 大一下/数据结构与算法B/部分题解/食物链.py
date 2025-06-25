def find(x):
    global p
    if p[x]!=x:
        p[x]=find(p[x])
        return p[x]
    else:
        return x

n,k=map(int,input().split())
p=[i for i in range(n*3+1)]
ans=0
for i in range(k):
    d,x,y=map(int,input().split())
    if x>n or y>n:
        ans+=1
        continue
    if d==1:
        if find(x)==find(n+y) or find(n+x)==find(y):
            ans+=1
            continue
        p[find(y)]=find(x)
        p[find(n+y)]=find(n+x)
        p[find(n+n+y)]=find(n+n+x)
    else:
        if find(y)==find(n+n+x) or find(y)==find(x):
            ans+=1
            continue
        p[find(n+x)]=find(y)
        p[find(n+n+y)]=find(x)
        p[find(n+n+x)]=find(n+y)#就算是看了题解也忘记的一步
print(ans)

# class disjointset:
#     def __init__(self,n):
#         self.father=[x for x in range(n)]
#         self.dict={}
#     def find(self,x):
#         stack=[]
#         while self.father[x]!=x:
#             stack.append(x)
#             x=self.father[x]
#         for i in stack:
#             self.father[i]=x
#         return x
#     def issameset(self,x,y):
#         return self.find(x) == self.find(y)
#
#     def union(self,x,y):
#         fx=self.find(x)
#         fy=self.find(y)
#         if fx!=fy:
#             self.father[fy]=fx
#

# n,k=map(int,input().split())
# p=disjointset(n)
# ans=0
# nta={}#num to abc
# for i in range(k):
#     d,x,y=map(int,input().split())
#     if x>n or y>n:
#         ans+=1
#         continue
#     if d==1:
#         if p.issameset(x,y):
#             ans+=1
#         else:
#             p.union(x,y)
#     elif d==2:
#         if p.issameset(x,y):
#             ans+=1
#             continue
#         if nta[x]:
#             sx=nta[x]
#             if nta[y]:
#                 sy=nta[y]
#                 if (sx=='A' and sy=='B') or (sx=='B' and sy=='C') or (sx=='C' and sy=='A'):
#                     pass
#                 else:
#                     ans+=1
#             else:
#                 if sx=='A':
#                     nta[y]='B'
#                 elif sx=='B':
#                     nta[y]='C'
#                 else:
#                     nta[y]='A'
#         else:
#             if nta[y]:
#                 sy=nta[y]
#                 if sy=='A':
#                     nta[x]='C'
#                 elif sy=='B':
#                     nta[x]='A'
#                 else:
#                     nta[y]='B'
#             else:
#                 nta[x]='A'
#                 nta[y]='B'
# print(ans)