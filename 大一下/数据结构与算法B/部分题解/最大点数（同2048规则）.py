row,col,step=map(int,input().split())
ma=[]
for _ in range(row):
    ma.append(list(map(int,input().split())))
def f(d,ma):
    nma=[[0]*len(ma[0]) for _ in range(len(ma))]
    if d==0:
        for j in range(len(ma[0])):
            num=[]
            for i in range(len(ma)):
                if ma[i][j]!=0:
                    num.append(ma[i][j])
            i=0
            cnt=0
            while i<len(num):
                if i+1<len(num) and num[i]==num[i+1]:
                    nma[i-cnt][j]=num[i]*2
                    i+=2
                    cnt+=1
                else:
                    nma[i-cnt][j]=num[i]
                    i+=1
    if d==2:
        for j in range(len(ma[0])):
            num=[]
            for i in range(len(ma)):
                if ma[i][j]!=0:
                    num.append(ma[i][j])
            i=-1
            cnt=0
            while i>=-len(num):
                if i-1>=-len(num) and num[i]==num[i-1]:
                    nma[i+cnt][j]=num[i]*2
                    i-=2
                    cnt+=1
                else:
                    nma[i+cnt][j]=num[i]
                    i-=1
    if d==1:
        for i in range(len(ma)):
            num=[]
            for j in range(len(ma[0])):
                if ma[i][j]!=0:
                    num.append(ma[i][j])
            j=-1
            cnt=0
            while j>=-len(num):
                if j-1>=-len(num) and num[j]==num[j-1]:
                    nma[i][j+cnt]=num[j]*2
                    j-=2
                    cnt+=1
                else:
                    nma[i][j+cnt]=num[j]
                    j-=1
    if d==3:
        for i in range(len(ma)):
            num=[]
            for j in range(len(ma[0])):
                if ma[i][j]!=0:
                    num.append(ma[i][j])
            j=0
            cnt=0
            while j<len(num):
                if j+1<len(num) and num[j]==num[j+1]:
                    nma[i][j-cnt]=num[j]*2
                    j+=2
                    cnt+=1
                else:
                    nma[i][j-cnt]=num[j]
                    j+=1
    return nma
def dfs(ma,step):
    ans=0
    if step==0:
        for i in ma:
            ans=max(ans,max(i))
        return ans
    for i in range(4):
        ans=max(ans,dfs(f(i,ma),step-1))
    return ans
print(dfs(ma,step))