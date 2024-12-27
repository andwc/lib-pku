def oula(a):
    zhishu=[]
    zhishu1=[True]*(a+1)
    for i in range(2,a+1):
        if zhishu1[i]:
            zhishu.append(i)
        for h in zhishu:
            if h*i<=a:
                zhishu1[h*i]=False
    zhishu=set(zhishu)
    return zhishu
zhishu=oula(10000)
n=int(input())
answer=1
for i in zhishu:
    if n-i in zhishu:
        answer=max(answer,i*(n-i))
print(answer)