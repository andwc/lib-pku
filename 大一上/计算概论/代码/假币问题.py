def main():

    l= {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L'}
    l1= {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11}
    s1=[]
    s2=[]
    s=[]
    qing=[0]*12
    zhong=[0]*12
    for i in range(3):
        shuru=input().split()
        s1.append(shuru[0])
        s2.append(shuru[1])
        s.append(shuru[2])
    for i in range(3):
        if s[i]=='even':
            for j in s1[i]:
                qing[l1[j]]=-114514
                zhong[l1[j]] = -114514
            for j in s2[i]:
                qing[l1[j]] = -114514
                zhong[l1[j]] = -114514
    for i in range(3):
        if s[i]=='up':
            for j in s2[i]:
                qing[l1[j]]+=1
            for j in s1[i]:
                zhong[l1[j]]+=1
        if s[i]=='down':
            for j in s1[i]:
                qing[l1[j]]+=1
            for j in s2[i]:
                zhong[l1[j]]+=1
        #print(qing,zhong)
    q=s.count('down')+s.count('up')
    for i in range(12):
        if qing[i]==q:
            print(l[i],' is the counterfeit coin and it is light.',sep='')
            break
        if zhong[i]==q:
            print(l[i], ' is the counterfeit coin and it is heavy.', sep='')
            break
n=int(input())
for i in range(n):
    main()