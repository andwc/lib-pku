n=int(input())
w=[]
for i in range(4):
    w.append(input())
used=[False,False,False,False]
def dfs(s,i):
    global j,used
    if i==len(s):
        j='YES'
        return
    for k in range(4):
        if s[i] in w[k] and used[k]==False:
            used[k]=True
            dfs(s,i+1)
            used[k]=False
for i in range(n):
    j='NO'
    used = [False] * 4
    s=input()
    dfs(s,0)
    print(j)