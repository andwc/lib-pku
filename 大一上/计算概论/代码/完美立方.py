num=int(input())
answer=[]
for a in range(3,num+1):
    for b in range(2,a):
        for c in range(2,b+1):
            for d in range(2,c+1):
                if a**3==b**3+c**3+d**3:
                    answer.append((a,d,c,b))
answer.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
for a,e,f,g in answer:
    print('Cube = ',a,', Triple = (',e,',',f,',',g,')',sep='')