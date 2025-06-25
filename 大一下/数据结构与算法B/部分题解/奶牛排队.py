n=int(input())
p=[]
for _ in range(n):
    p.append(int(input()))
#遍历
st=[]
xiao=[0]*n
for i in range(n):
    while st and p[st[-1]]>=p[i]:
        cur=st.pop()
        xiao[cur]=i
    st.append(i)
while st:
    cur=st.pop()
    xiao[cur]=-1
#遍历
st=[]
da=[0]*n
for i in range(n):
    while st and p[st[-1]]<=p[i]:
        cur=st.pop()
        da[cur]=i
    st.append(i)
while st:
    cur=st.pop()
    da[cur]=-1
for i in range(n-2,-1,-1):
    if da[i]!=-1 and p[da[i]]==p[i]:
        da[i]=da[da[i]]
ans=0
# print(p)
# print(xiao)
# print(da)
#test=[]
for left in range(n):
    right=left
    if xiao[left]==-1:
        limit=float('inf')
    else:
        limit=xiao[left]-1
    while da[right]!=-1 and da[right]<=limit:
        right=da[right]
    length=right-left+1
    #test.append((left,right))
    ans=max(ans,length)
# print(test)
if ans==1:
    ans=0
print(ans)