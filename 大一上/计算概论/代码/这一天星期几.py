import math
week={0:'Sunday',6:'Saturday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday'}
def zeller(y,c,m,d):
    return((y+math.floor(y/4)+math.floor(c/4)-2*c+math.floor(26*(m+1)/10)+d-1)%7)
num=int(input())
answer=[]
for i in range(num):
    s=input()
    c=int(s[0]+s[1])
    y=int(s[2]+s[3])
    m=int(s[4]+s[5])
    if m==1 or m==2:
        m+=12
        if y!=0:
            y-=1
        else:
            c-=1
            y=99
    d=int(s[6]+s[7])
    w=zeller(y,c,m,d)
    answer.append(week[w])
for j in range(len(answer)):
    print(answer[j])