s=input()
where=0
def f(i):
    global where,s
    num=''
    ans=''
    while i<len(s) and s[i]!=']':
        if s[i] in '0123456789':
            num+=s[i]
            i+=1
        elif s[i]=='[':
            ans+=f(i+1)
            i=where+1
        else:
            ans+=s[i]
            i+=1
        where=i
    if num:
        return ans*int(num)
    else:
        return ans
print(f(0))
# s=input()
# num={'0','1','2','3','4','5','6','7','8','9'}
# stack=[]
# n=''
# ss=''
# ans=''
# y=''
# for i in s:
#     if i in num:
#         n+=i
#     elif i=='[':
#         if n:
#             stack.append([int(n),ss])
#         else:
#             stack.append([0,ss])
#         n=''
#         ss=''
#     elif i==']':
#         x,y=stack.pop()
#         y+=ss*int(n)
#         n=x
#         ss=y
#         if not stack:
#             ans+=y
#             n=''
#             ss=''
#     else:
#         if n:
#             ss+=i
#         else:
#             ans+=i
#     #print(stack,n,ss)
# print(ans)