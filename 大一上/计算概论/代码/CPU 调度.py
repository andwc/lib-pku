n=int(input())
p=[]
for i in range(n):
    a,b=map(int,input().split())
    p.append((a,b))
p.sort(key=lambda x:(-x[1],x[0]))
ans1,ans2=0,0
for i in range(n):
    ans1+=p[i][0]
    ans2=max(ans2,ans1+p[i][1])
print(ans2)