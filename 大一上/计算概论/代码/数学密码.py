def fenjie(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i!=0:
            i += 1
        else:
            n=int(n/i)
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
num=int(input())
a=fenjie(num)
#print(a)
answer=num
if 2 in a and 3 in a:
    answer=int(num/6)
elif 7 in a:
    answer=int(num/7)
elif a.count(2)>=3:
    answer=int(num/8)
elif a.count(3)>=2:
    answer=int(num/9)
elif 2 in a and 5 in a:
    answer=int(num/10)
elif 3 in a and 5 in a:
    answer=int(num/15)
elif a.count(5)>=2:
    answer=int(num/25)
else:
    for i in range(len(a)):
        if a[i]!=2 and a[i]!=3 and a[i]!=5:
            answer=int(answer/a[i])
            break
print(answer)