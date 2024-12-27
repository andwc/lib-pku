num=int(input())
coins=list(map(int,input().split()))
#print(coins)
s=sum(coins)
m=max(coins)
i=0
i+=m
answer=1
while i<=s-m:
    s-=m
    answer+=1
    coins.remove(m)
    m=max(coins)
    i+=m
    #print(s,m)
print(answer)