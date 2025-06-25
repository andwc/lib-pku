import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
p = int(data[index])
index += 1
nums = [int(i) for i in data[index:index+n]]
d={}
ans=[]
def tan(m):
    global d,p
    i=1
    cur=m
    while cur in d:
        cur=m+i*abs(i)
        if i<0:
            i=-i+1
        else:
            i=-i
    return cur
for i in range(n):
    m = nums[i] % p
    if m in d and nums[i] not in d[m]:
        m=tan(m)
    d[m] = set([nums[i]])
    ans.append(m)
print(' '.join(map(str,ans)))