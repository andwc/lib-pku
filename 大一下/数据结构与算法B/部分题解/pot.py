a,b,c=map(int,input().split())
from collections import deque
q=deque()
q.append((0,0,''))
v=set()
v.add((0,0))
step=0
def shuchu(s):
    print(len(s)//2)
    for i in range(0,len(s),2):
        if s[i]=='f':
            print('FILL(',s[i+1],')',sep='')
        elif s[i]=='d':
            print('DROP(',s[i+1],')',sep='')
        else:
            a=int(s[i+1])
            if a==1:
                b=2
            else:
                b=1
            print('POUR(',b,',',a,')',sep='')
while q:
    step+=1
    for _ in range(len(q)):
        x,y,path=q.popleft()
        if x==c or y==c:
            shuchu(path)
            exit()
        #fill
        if x!=a and (a,y) not in v:
            v.add((a,y))
            q.append((a,y,path+'f1'))
        if y != b and (x, b) not in v:
            v.add((x, b))
            q.append((x, b, path + 'f2'))
        #drop
        if x and (0,y) not in v:
            v.add((0,y))
            q.append((0,y,path + 'd1'))
        if y and (x,0) not in v:
            v.add((x,0))
            q.append((x,0,path + 'd2'))
        #pour
        if x!=a and y and x+y<=a and (x+y,0) not in v:
            v.add((x+y,0))
            q.append((x+y,0,path + 'p1'))
        elif x!=a and y and x+y>=a and (a,x+y-a) not in v:
            v.add((a,x+y-a))
            q.append((a,x+y-a,path + 'p1'))
        if y!=b and x and x+y<=b and (0,x+y) not in v:
            v.add((0,x+y))
            q.append((0,x+y,path + 'p2'))
        elif y!=b and x and x+y>=b and (x+y-b,b) not in v:
            v.add((x+y-b,b))
            q.append((x+y-b,b,path + 'p2'))
print('impossible')