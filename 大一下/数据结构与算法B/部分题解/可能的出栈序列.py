n=int(input())
nums=[x+1 for x in range(n)]
nums.reverse()
ans=[]
def dfs(nums,n,stack,path,ans):
    # print(path)
    # print(stack)
    # print(nums)
    # print()
    if len(path)==n:
        ans.append(path.copy())
        return
    if stack:
        path.append(stack.pop())
        dfs(nums,n,stack,path,ans)
        stack.append(path.pop())
        if nums:
            stack.append(nums.pop())
            dfs(nums,n,stack,path,ans)
            nums.append(stack.pop())
    else:
        stack.append(nums.pop())
        dfs(nums,n,stack,path,ans)
        nums.append(stack.pop())
    return
dfs(nums,n,[],[],ans)
for i in ans:
    print(' '.join(map(str,list(i))))
