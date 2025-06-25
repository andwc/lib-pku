n=int(input())
m=list(map(int,input().split()))
path=[]
way=[m[0]]
def dfs(i):
    global n,m,path,way
    if 2*i+2<n:
        way.append(m[2*i+2])
        dfs(2*i+2)
        way.pop()
        way.append(m[2 * i + 1])
        dfs(2 * i + 1)
        way.pop()
    elif 2*i+1<n:
        way.append(m[2*i+1])
        dfs(2*i+1)
        way.pop()
    else:
        path.append(way.copy())
    return
def f(path):
    cnt=0
    for i in path:
        judge1=0
        judge2=0
        for j in range(1,len(i)):
            if i[j-1]>=i[j]:
                judge1+=1
            if i[j-1]<=i[j]:
                judge2+=1
        if judge1==len(i)-1:
            cnt+=1
        elif judge2==len(i)-1:
            cnt-=1
        else:
            return 0
    if cnt==len(path):
        return 1
    elif cnt==-len(path):
        return -1
    return 0
dfs(0)
for i in path:
    print(' '.join(map(str,i)))
if f(path)==1:
    print('Max Heap')
elif f(path)==-1:
    print('Min Heap')
else:
    print('Not Heap')