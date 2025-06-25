n=int(input())
st=[]
p=[]
ans=0
for _ in range(2*n):
    shuru=input().split()
    if shuru[0]=='add':
        st.append(int(shuru[1]))
    else:
        num=st[-1]
        if not p:
            if num!=1:
                ans+=1
                st.sort(reverse=True)
                p.append(st.pop())
                continue
        else:
            if num!=p[-1]+1:
                ans+=1
                st.sort(reverse=True)
                p.append(st.pop())
                continue
        p.append(st.pop())
print(ans)