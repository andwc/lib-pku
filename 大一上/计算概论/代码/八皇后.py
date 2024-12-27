import copy
def t(row,col,pp):
    p=copy.deepcopy(pp)
    for i in range(1,9):
        p[i][col]=False
        if 0<col+(i-row)<9:
            p[i][col+(i-row)]=False
        if 0<col-(i-row)<9:
            p[i][col - (i - row)] = False
    for i in range(1, 9):
        p[row][i] = False
        if 0<row+(i-col)<9:
            p[row+(i-col)][i]=False
        if 0 < row - (i - col) < 9:
            p[row - (i - col)] [i]= False
    return p
def search(a,p,s,answer):
    for i in range(1,9):
        if p[a][i]:
            s+=str(i)
            #print(s)
            if a==8:
                answer.append(s)
            else:
                search(a + 1,t(a, i, p), s, answer)
            s=s[:-1]
    return answer
s=''
p=[[True for i in range(9)] for j in range(9)]
answer=[]
answer=search(1,p,s,answer)
#print(answer)
n=int(input())
for i in range(n):
    shuru=int(input())
    print(answer[shuru-1])