def hannuota(n,a,b,c):#a is begin,b is fuzhu,c is target
    step=[]
    if n==1:
        s=a+'->'+c
        step.append(s)
        return step
    else:
        step.extend(hannuota(n-1,a,c,b))
        s = a + '->' + c
        step.append(s)
        step.extend(hannuota(n-1,b,a,c))
    return step
n=int(input())
step=hannuota(n,'A','B','C')
print(len(step))
for i in step:
    print(i)