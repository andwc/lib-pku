# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>陈俊逸、工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：加了点数学的计算，对每个数据，只考虑左边和上边的格子，0和1分情况讨论。

代码：

```python
n,m=map(int,input().split())
x=[[0 for _ in range(m+2)]for _ in range(n+2)]
ans=0
for i in range(1,n+1):
    shuru=list(map(int,input().split()))
    for j in range(1,m+1):
        if shuru[j-1]==1:
            x[i][j]=1
            ans+=2-x[i-1][j]-x[i][j-1]
        else:
            ans+=(x[i-1][j]+x[i][j-1])
    ans += x[i][m]
ans+=shuru.count(1)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241112204810808](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241112204810808.png)

### LeetCode54.螺旋矩阵（20min）

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

定一个direction，表明当前的方向，取余4就是当前的方向，四个方向都写（没有本质区别，四个方向就是复制粘贴）。我又发现对于n，只需要进行2n-1此操作，所以循环2n-1次就行。

代码：

```python
n=int(input())
a=[[None for _ in range(n)] for _ in range(n)]
d,i,j,s=0,0,0,1
a[0][0]=1
def t(a,i,j,n,d,s):
    k=1
    if d%4==0:
        while True:
            if j+k<n:
                if a[i][j+k]==None:
                    a[i][j+k]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i,j+k,n,d,s+k
    elif d%4==1:
        while True:
            if i+k<n:
                if a[i+k][j]==None:
                    a[i+k][j]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i+k,j,n,d,s+k
    elif d%4==2:
        while True:
            if j-k>-1:
                if a[i][j-k]==None:
                    a[i][j-k]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i,j-k,n,d,s+k
    elif d%4==3:
        while True:
            if i-k<n:
                if a[i-k][j]==None:
                    a[i-k][j]=s+k
                    k+=1
                else:
                    break
            else:
                break
        k-=1
        d+=1
        return a,i-k,j,n,d,s+k
for _ in range(2*n-1):
    a,i,j,n,d,s=t(a,i,j,n,d,s)
for i in range(n):
    for j in a[i]:
        print(j,end=" ")
    print()
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241114154550453](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241114154550453.png)

### 04133:垃圾炸弹（两个多小时）

matrices, http://cs101.openjudge.cn/practice/04133/

思路：

把一个垃圾周围d格都填上这个垃圾数，最后求列表中的最大值即可

代码：

```python
d=int(input())
n=int(input())
a=[[0 for _ in range(1025)]for _ in range(1025)]
di={}
for _ in range(n):
    shuru=list(map(int,input().split()))
    di[(shuru[0],shuru[1])]=shuru[2]
    a[shuru[0]][shuru[1]]=shuru[2]
for x,y in di.keys():
    for i in range(max(0,x-d),min(1024,x+d)+1):
        for j in range(max(0,y-d),min(1024,y+d)+1):
            if i==x and j==y:
                continue
            a[i][j]+=a[x][y]
s,f=0,0
for i in range(1025):
    s0=max(a[i])
    if s<s0:
        s=s0
        f=a[i].count(s)
    elif s==s0:
        f+=a[i].count(s)
print(f,s)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114173613444](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241114173613444.png)

### LeetCode376.摆动序列（25min）

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

贪心（还好题目里有提示），上升的时候肯定越高越好，下降的时候肯定越低越好，这样对每两个相邻的数都可以局部分析，如果相等，不管它

代码：

```python
def main():
    n=int(input())
    num=list(map(int,input().split()))
    ans=0
    if n==1:
        print(1)
        exit()
    else:
        k=0
        try:
            while num[k]==num[k+1]:
                k+=1
        except IndexError:
            print(1)
            exit()
        judge=sgn(num[k],num[k+1])
        ans+=2
        current=num[k+1]
        for i in range(k+2,n):
            if num[i]==current:
                continue
            if judge>0:
                if num[i]>current:
                    current=num[i]
                    continue
                elif num[i]<current:
                    current=num[i]
                    judge=-1
                    ans+=1
                    continue
            elif judge<0:
                if num[i]>current:
                    current=num[i]
                    judge=1
                    ans+=1
                    continue
                elif num[i]<current:
                    current=num[i]
                    continue
        print(ans)
def sgn(a,b):
    if a>b:
        return -1
    elif a<b:
        return 1
main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241114180157839](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241114180157839.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

主要的是dp的呢个通项公式（灵光一现）

代码：

```python
def main():
    n=int(input())
    num=list(map(int,input().split()))
    a=set(num)
    m=max(a)
    dp=[0]*(m+1)
    c=[0]*(m+1)
    for i in num:
        c[i]+=1
    dp[1]=c[1]
    for i in range(1,m+1):
        dp[i]=dp[i-1] if dp[i-1]>dp[i-2]+i*c[i] else dp[i-2]+i*c[i]
    print(dp[m])
main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241115112311159](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241115112311159.png)

### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：



代码：

```python
def main():
    while True:
        n=int(input())
        if n==0:
            exit()
        tianji=sorted(list(map(int,input().split())))
        king=sorted(list(map(int,input().split())))
        win,lose=0,0
        while True:
            if not tianji:
                break
            if tianji[-1]>king[-1]:
                win+=1
                del tianji[-1]
                del king[-1]
            elif tianji[-1]<king[-1]:
                lose+=1
                del tianji[0]
                del king[-1]
            elif tianji[-1]==king[-1]:
                if tianji[0]>king[0]:
                    del tianji[0]
                    del king[0]
                    win+=1
                else:
                    if tianji[0]<king[-1]:
                        lose+=1
                    del tianji[0]
                    del king[-1]
        print(200*(win-lose))
main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241115142158378](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241115142158378.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

感觉垃圾炸弹这个题很巧妙，自己做了半天也没搞出来，最后通过一个同学的提示（即上面写的思路），豁然开朗，感觉十分的巧妙，而且代码运行速度也很快（自己做的时候一直超时）

倒数第二题也很有收获，一开始用了count，很慢测试超时。后来反应过来老师说过count很慢，于是稍微换了个思路就ac了。我发现很多坑通过老师讲只是纸上谈兵，只有自己真的用这个错过一次印象就会很深。而且发现，dp做多了以后真的会产生第六感，我都没想清楚这个题的时候，我先猜了一个迭代公式，然后居然ac了。感觉就是最近做多了dp后的第六感（虽然dp刚开始接触的时候确实很头疼）

最后一题太难了，那道题的时候就反应过来是greedy了，但是一直没想清楚greedy的思路，写了一上午最后放弃了，感觉把能试的方法都试了，最后问了一下我室友，觉得这个greedy的思路很巧妙，收获很大。

12月还有一次月考，转眼就感觉快要期末了，感觉时间过的好快，但是很多算法掌握的还不是很牢靠，最近要抓紧时间多练练题了。
