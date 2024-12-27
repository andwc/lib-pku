num=int(input())
a,b=map(int,input().split())
king=(a,b)
cheng=[]
for i in range(num):
    a,b=map(int,input().split())
    cheng.append((a,b))
cheng.sort(key=lambda x:x[0]*x[1])
ans=[0]*(num)
ans[0]=king[0]/cheng[0][1]
qianzhuiji=[0]*(num)
qianzhuiji[0]=king[0]*cheng[0][0]
for i in range(1,num):
    qianzhuiji[i]=qianzhuiji[i-1]*cheng[i][0]
for i in range(1,num):
    ans[i]=qianzhuiji[i-1]//cheng[i][1]
print(max(ans))