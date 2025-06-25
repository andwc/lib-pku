#这个写法有点笨了
x,y=map(int,input().split())
path_x=[]
path_y=[]
while x!=1:
    path_x.append(x)
    x//=2
while y!=1:
    path_y.append(y)
    y//=2
path_x.append(1)
path_y.append(1)
a=path_x+path_y
b=path_y+path_x
i=0
while a[i]!=b[i]:
    i+=1
print(a[i])