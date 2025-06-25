t=int(input())
zu=[]*t
for i in range(t):
    shuru=set(map(int,input().split()))
    zu.append(shuru)
queue=[]
while True:
    s=input()
    if s[0]=='S':
        break
    elif s[0]=='E':
        s=s.split()
        s=int(s[1])
        index=0
        for i in zu:
            if s in i:
                for j in range(len(queue)):
                    if queue[j] in i:
                        index=j
                        break
                break
        queue.insert(index,s)
        #print(queue)
    elif s[0]=='D':
        print(queue.pop())