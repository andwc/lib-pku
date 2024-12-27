def deal(a1,a2):
    fanhui=0
    if a2>=9:
        fanhui+=a2//9
        a2%=9
    if a2!=0:
        fanhui+=1
        a1-=(36-4*a2)
    if a1<=0:
        pass
    elif a1<=36:
        fanhui+=1
    elif a1%36==0:
        fanhui+=(a1//36)
    else:
        fanhui=fanhui+(a1//36)+1
    return fanhui
while True:
    shuru=input().split()
    a1=int(shuru[0])
    a2=int(shuru[1])
    a3=int(shuru[2])
    a4=int(shuru[3])
    a5=int(shuru[4])
    a6=int(shuru[5])
    if a1==a2==a3==a4==a5==a6==0:
        break
    answer=a6+a5+a4+(a3//4)
    a1-=a5*11
    a2-=a4*5
    a3%=4
    if a2 <= 0:
        if a1>0:
            a1+=a2*4
        a2 = 0
    if a3!=0:
        answer+=1
        s=7-2*a3
        if a2>=s:
            a2-=s
            a1-=(36-a3*9-4*s)
            if a2 <= 0:
                a2 = 0
            answer+=deal(a1,a2)
        else:
            a2=0
            a1-=(36-a3*9-4*a2)
            answer+=deal(a1,a2)
    else:
        answer+=deal(a1,a2)
    print(answer)