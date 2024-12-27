# Assignment #10: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>陈俊逸、工院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯（10min）

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

递归，n只能由n-1和n-2传递过来

代码：

```python
from sys import setrecursionlimit
setrecursionlimit(100000)
def s(n):
    global dp
    if dp[n-1] and dp[n-2]:
        dp[n]=dp[n-1]+dp[n-2]
    else:
        s(n-1)
        s(n-2)
n=int(input())
dp=[None]*(n+1)
dp[0]=1
dp[1]=1
if n==1:
    print(1)
    exit()
s(n)
print(dp[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241127092903691](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241127092903691.png)

### 27528: 跳台阶（3min）

dp, http://cs101.openjudge.cn/practice/27528/

思路：

n可以有1----n-1的所有来，所以感觉从1开始不断求和会方便理解一些

代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0]=1
dp[1]=1
for i in range(2,n+1):
    for j in range(0,i):
        dp[i]+=dp[j]
print(dp[-1])
```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20241127093505970](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241127093505970.png)

### 474D. Flowers（1h）

dp, https://codeforces.com/problemset/problem/474/D

思路：

这个dp转移方程看上去很直观，但不是很好想。我的大致证明思路如下：

对dp n来说，第一个花要么是r，要么是w。对于r的情况后面n-1的花就可以用dp n-1，对于w，要求前k个都得是w，故需要用dp n-w，然后将二者相加

代码：

```python
t,k= map(int, input().split())
L=1000000007
dp=[0]*(100001)
dp[0]=1
if k>1:
    dp[1]=1
else:
    dp[1]=2
for n in range(2,100001):
    dp[n]+=dp[n-1]
    if n>k-1:
        dp[n]=(dp[n]+dp[n-k])%L
q=[0]*(100001)
for n in range(1,100001):
    q[n]=(q[n-1]+dp[n])%L
for pp in range(t):
    a,b=map(int,input().split())
    print((q[b]-q[a-1])%L)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241127120426003](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241127120426003.png)



### LeetCode5.最长回文子串（13min）

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

最开始想到的思路就是简单的双指针，看了题解后发现了更优的dp思路（感觉好妙，但想不到）

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=''
        if n==1:
            return s
        for i in range(n):
            for j in range(n,i+len(ans),-1):
                old=s[i:j]
                new=old[::-1]
                if new==old and len(old)>len(ans):
                    ans=old
                    break
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241127201917796](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241127201917796.png)



### 12029: 水淹七军(很长时间)

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

两种情况：同高度判断是否淹过（不然会死循环），对于低高度直接淹

代码：

```python
import sys
sys.setrecursionlimit(1000000)
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y,h):
    global n,m,ditu
    for dx,dy in directions:
        nx,ny=x+dx,y+dy
        if -1<nx<m and -1<ny<n:
            if h>ditu[nx][ny]:
                ditu[nx][ny]=h
                judge[nx][ny]=True
                dfs(nx,ny,ditu[nx][ny])
            elif ditu[nx][ny]==h and not judge[nx][ny]:
                judge[nx][ny]=True
                dfs(nx,ny,ditu[nx][ny])
shuru=list(map(int,sys.stdin.read().split()))
case=shuru[0]
index=0
for _ in range(case):
    m,n=shuru[index+1],shuru[index+2]
    ditu=[[0 for _ in range(n)]for _ in range(m)]
    for ki in range(m):
        for kj in range(n):
            ditu[ki][kj]=shuru[index+ki*n+kj+3]
    i,j=shuru[index+3+n*m],shuru[index+4+m*n]
    i,j=i-1,j-1
    p=shuru[index+5+n*m]
    judge=[[False for _ in range(n)]for _ in range(m)]
    oh=ditu[i][j]
    for k in range(p):
        x,y=shuru[index+6+n*m+2*k],shuru[index+7+m*n+2*k]
        x,y=x-1,y-1
        judge[x][y]=True
        dfs(x,y,ditu[x][y])
    print('Yes' if oh<ditu[i][j] else 'No')
    index+=5+n*m+2*p
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241129125626770](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241129125626770.png)

### 02802: 小游戏（int long long time）

bfs, http://cs101.openjudge.cn/practice/02802/

思路：



代码：

```python
from collections import deque
directions=[(1,0),(-1,0),(0,1),(0,-1)]
def bfs(x1,y1):
    global card,n,m,x2,y2,visited
    queue=deque()
    queue.append((x1,y1))
    step=0
    while queue:
        step+=1
        for _ in range(len(queue)):
            x,y=queue.popleft()
            visited.add((x,y))
            for dx,dy in directions:
                nx,ny=x+dx,y+dy
                if nx==x2 and ny==y2:
                    return step
                while 0<=nx<m+2 and 0<=ny<n+2 and (nx,ny) not in visited and card[nx][ny]==' ':
                    queue.append((nx,ny))
                    nx,ny=nx+dx,ny+dy
                    if nx==x2 and ny==y2:
                        return step
case=0
while True:
    case+=1
    n,m=map(int,input().split())
    if n==m==0:
        break
    print('Board #',case,':',sep='')
    card=[]
    card.append(' '*(n+2))
    for _ in range(m):
        s=input()
        card.append(' '+s+' ')
    card.append(' ' * (n+2))
    xiaocase=0
    while True:
        xiaocase+=1
        visited=set()
        x1,y1,x2,y2=map(int,input().split())
        x1, y1, x2, y2 =y1,x1,y2,x2
        path=[(x1,y1)]
        a=0
        if x1==x2==y1==y2==0:
            break
        a=bfs(x1,y1)
        if not a:
            print('Pair ',xiaocase,': impossible.',sep='')
        else:
            print('Pair ',xiaocase,': ',a,' segments.',sep='')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241129165655829](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241129165655829.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>



flowers很有收获，我状态转移方程几乎是瞬间想到的，但是我想的严格证明一下，结果花了一点时间。还有就是写完以后一直超时，花了很多时间优化，还超时，在工院的一个小讨论群里问了一下才发现前缀和这个东西，这个太有用了，涨知识了。

水淹七军太坑了，前面是read花了好长时间，最后是我有个地方的指针写错了debug了半天，还有就是这个淹法太奇葩了（水平能淹别的地方但淹不了司令部，感到了题目的恶意以及读入数据的恶意）

最后一题收获还挺大的，一开始自己做拿dfs（因为对bfs不熟悉，我一般都用dfs写，结果超时了），但换成bfs后不会做了，最后在室友的帮助下做出来了，并且逐渐理解了广搜的本质。

还有就是碰到 presentation error 懵了，然后突然想起来上课讲过，然后回去又看了一眼题目，发现了万恶的换行
