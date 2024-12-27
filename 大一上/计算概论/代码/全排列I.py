def quanpai(n):
    s=[]
    if len(n)-1==n.count(-1):
        for i in n:
            if i!=-1:
                i=str(i)
                s.append(i)
                #print(n,i,s,' opk')
        return s
    for i in n:
        if i==-1:
            continue
        nn=n[::]
        nn[i-1]=-1
        i=str(i)
        #print(nn,i,s)
        s1=quanpai(nn)
        #print(s1,'pj')
        for j in s1:
            s.append(i+' '+j)
            #print(s)
    return s
num=int(input())
n=[]
for i in range(num):
    n.append(i+1)
s=quanpai(n)
for i in s:
    print(i)