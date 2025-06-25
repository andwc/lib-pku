while 1:
    n,m=map(int,input().split())
    if n==m==0:
        break
    num_to_key={}
    key_to_num={}
    key=0
    for i in range(n):
        shuru=(list(map(int,input().split())))
        for j in shuru:
            if j not in num_to_key:
                num_to_key[j]=[key,1]
                key_to_num[key]=j
                key+=1
            else:
                num_to_key[j][1]+=1
    result=[]
    #print(key)
    # print(num_to_key)
    # print(key_to_num)
    for i in range(key):
        num=key_to_num[i]
        result.append([num_to_key[num][1],i])
    result.sort(key=lambda x:(-x[0],x[1]))
    f=result[0][0]
    index=1
    while result[index][0]==f:
        index+=1
    s=result[index][0]
    ans=[]
    while index<len(result) and result[index][0]==s :
        ans.append(key_to_num[result[index][1]])
        index+=1
    ans.sort()
    print(' '.join(map(str,ans)))