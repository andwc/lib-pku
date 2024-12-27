h=int(input())
m=int(input())
h=h*2-0.5*m
score=[]
xuefen=[]
a=[]
answer=0.0
for i in range(1,m+1):
    s,c=map(float,input().split())
    score.append(s)
    xuefen.append(c)
    a.append(c*s)
while h>0:
    if a.count(-1)!=len(a):
        shi=max(a)
        index=a.index(shi)
        if h*score[index]>=5.0:
            answer+=5.0*xuefen[index]
        if h*score[index]<5.0:
            answer+=xuefen[index]*h*score[index]
        h-=5.0/score[index]
        a[index]=-1
    else:
        break
    #print(a,score,xuefen,h,answer)
answer="{:.1f}".format(answer)
print(answer)