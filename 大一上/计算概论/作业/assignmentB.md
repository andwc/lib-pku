# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>陈俊逸，工学院</mark>



**说明：**

1）⽉考： AC6<mark>（2）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张（20min，AC）

http://cs101.openjudge.cn/practice/22548/

思路：

遍历每一天，看看这一天买后收益是多少

代码：

```python
p=list(map(int,input().split()))
dp=[0]*(len(p))
i=0
judge=float('inf')
while p:
    if p[0]>judge:
        p.pop(0)
        continue
    m=max(p)
    if p[0]!=m:
        dp[i]=m-p[0]
    judge=p[0]
    p.pop(0)
    i+=1
print(max(dp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206102201336](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241206102201336.png)

### M28701: 炸鸡排（考试时没看，下来也做了好久）

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

先往锅里放最大的k个，剩下的求和并与k个中最小的加和，并于下一个求平均数，如果求出的平均数大于下下个鸡排，再求平均和，直到平均值小于下一个鸡排为止

代码：

```python
def main():
    n,k=map(int,input().split())
    t=list(map(float,input().split()))
    t.sort()
    if n==k:
        print("{:.3f}".format(min(t)))
        return
    s=0
    for i in range(0,n-k):
        s+=t[i]
    t[n-k]+=s
    ans=t[n-k]
    for i in range(1,1+k):
        if ans<t[n-k+i-1]:
            break
        ans=(t[n-k+i-1]+ans*(i-1))/(i)
    print("{:.3f}".format(ans))
main()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241206133140911](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241206133140911.png)



### M20744: 土豪购物（考试50min，TLE，下来20min）

dp, http://cs101.openjudge.cn/practice/20744/

思路：

dp表示不扔东西且末尾是i的最优解

dpp表示扔东西，这时取max，dp i 表示取第i个数的情况，dpi-1表示不取的情况，dppi-1表示取第i个数并且前i-1的最优解，（其实还有第四种情况就是不取i-1加前i-1的最优解，但这个在i-1的时候相当于已经讨论过了，所以可以不加）

代码：

```python
shu=input()
p=list(map(int,shu.split(',')))
dp=[0 for _ in range(1+len(p))]
dpp=[0 for _ in range(1+len(p))]
for i in range(1,1+len(p)):
    dp[i]=max(p[i-1],dp[i-1]+p[i-1])
for i in range(1,1+len(p)):
    dpp[i]=max(dp[i],dp[i-1],dpp[i-1]+p[i-1])
print(max(dpp))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206110519734](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241206110519734.png)

### T25561: 2022决战双十一(1h)

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：

先把优惠券按减的最多的拍一下顺序，然后dfs枚举，然后算和就行了（这道题主要卡在审题上了）

代码：

```python
n,m=map(int,input().split())
goods=[[]for i in range(n)]
for i in range(n):
    shuru = list(map(str, input().split()))
    for j in range(len(shuru)):
        a, b = map(int,shuru[j].split(':'))
        goods[i].append((a, b))
youhui=[[]for _ in range(m)]
for i in range(m):
    shuru=list(map(str,input().split()))
    for j in range(len(shuru)):
        a,b=map(int,shuru[j].split('-'))
        youhui[i].append((a,b))
    youhui[i].sort(key=lambda x: x[1],reverse=True)
daan=float('inf')
def jisuan(path):
    global m
    dian=[0]*(m+1)
    ans=0
    for a,b in path:
        dian[a]+=b
        ans+=b
    ans-=50*(ans//300)
    for i in range(1,m+1):
        for j in range(len(youhui[i-1])):
            if dian[i]>=youhui[i-1][j][0]:
                ans-=youhui[i-1][j][1]
                break
    return ans
def dfs(i,path):
    global n,daan
    if i==n:
        ans=jisuan(path)
        daan=min(daan,ans)
        return
    for j in range(len(goods[i])):
        path.append((goods[i][j][0],goods[i][j][1]))
        dfs(i+1,path)
        path.pop()
dfs(0,[])
print(daan)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206150118955](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241206150118955.png)



### T20741: 两座孤岛最短距离（50min，AC）

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

先找一个岛，然后用bfs看架夺少桥的时候能碰到第二个岛

代码：

```python
n=int(input())
p=[input()for _ in range(n)]
from sys import setrecursionlimit
from collections import deque
setrecursionlimit(10000)
m=len(p[0])
judge=False
for i in range(n):
    if judge:
        break
    for j in range(m):
        if p[i][j]=='1':
            x=i
            y=j
            judge=True
            break
di=[[1,0],[0,1],[-1,0],[0,-1]]
island=deque()
island.append((x,y))
visited=set()
visited.add((x,y))
def dfs(x,y):
    global n,m
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and p[nx][ny]=='1' and (nx,ny) not in visited:
            island.append((nx,ny))
            visited.add((nx,ny))
            dfs(nx,ny)
dfs(x,y)
step=-1
judge=False
while island and not judge:
    step+=1
    #print(island)
    for _ in range(len(island)):

        if judge:
            break
        nx, ny = island.popleft()
        for dx, dy in di:
            nnx, nny = nx + dx, ny + dy
            if 0 <= nnx < n and 0 <= nny < m and (nnx, nny) not in visited and p[nnx][nny] == '0':
                island.append((nnx, nny))
                visited.add((nnx, nny))
            elif 0 <= nnx < n and 0 <= nny < m and (nnx, nny) not in visited and p[nnx][nny] == '1':
                judge = True
                break
print(step)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241206102524713](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241206102524713.png)

### T28776: 国王游戏（1h30min）

greedy, http://cs101.openjudge.cn/practice/28776

思路：

把乘积和大的往后排，然后求max

代码：

```python
num=int(input())
a,b=map(int,input().split())
king=(a,b)
cheng=[]
for i in range(num):
    a,b=map(int,input().split())
    cheng.append((a,b))
cheng.sort(key=lambda x:x[0]*x[1])
ans=[0]*(num)
ans[0]=king[0]/cheng[0][1]
qianzhuiji=[0]*(num)
qianzhuiji[0]=king[0]*cheng[0][0]
for i in range(1,num):
    qianzhuiji[i]=qianzhuiji[i-1]*cheng[i][0]
for i in range(1,num):
    ans[i]=qianzhuiji[i-1]//cheng[i][1]
print(max(ans))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241206173141164](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241206173141164.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

考试的时候卡在土豪购物上了，一致tle，没有想到更好的解法。主要是人到考场上先傻一半，有点紧张。

考试的时候做出来了架桥呢个题，dfs和bfs的结合，但就是对bfs还不熟，浪费了很多时间，不然可能30min左右就能写完。

然后下来做的时候发现，剩下的题都不好做，巨难。双十一呢个题思路还好，就是审题太难了，而且我还读错了，卡了好久。然后两道greedy题都不好想，我基本都是在我室友的辅助下才摸索出思路的，太太太太难了。

月考

​                                                                                              太太太太太太太太太太太                                                                                                   太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太l                                                                                             太太太太太太太太太太太                                                                                                  l                                                                                             太太太太太太太太太太太                                                                                                   l                                                                                          太太太太太太太太太太太太太                                                                                                                 l                                                                                       太太太太太太太  太太太太太太太                                                                                                      l                                                                                    太太太太太太太        太太太太太太太                                                                                                      l                                                                               太太太太太太太太             太太太太太太太                                                                                                    l                                                                          太太太太太太太太太                  太太太太太太太                                                                                                           l                                                                     太太太太太太太太太                         太太太太太太太太                                                                                             l                                                              太太太太太太太太太太                                太太太太太太太太                                                                                            l                                                        太太太太太太太太太太太                                          太太太太太太太                                                                               l                                                  太太太太太太太太太太太                                                      太太太太太太太太                                                                        l                                           太太太太太太太太太太太太                                                            太太太太太太太太                                                                           l                               太太太太太太太太太太太太太太太太太太太太太                                           太太太太太太太太                                                                   l                     太太太太太太太太太太太太太太太太太太太太太太太太太太                                      太太太太太太太太                                                             l              太太太太太太太太太太太太太太太太太太太太太太太太太太太太太太                                  太太太太太太太太太                                                     l        太太太太太太太太太太太太太太太          太太太太太太太太太太太太太                                          太太太太太太太太太太                                            l 太太太太太太太太太太太太太太太                             太太太太太太                                                              太太太太太太太太太太太太太太太



难了，~~主要可能是前段时间太忙了，忘退课了，现在还有机会退课吗~~
