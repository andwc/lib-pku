# Assignment #4: T-primes + 贪心

Updated 0337 GMT+8 Oct 15, 2024

2024 fall, Complied by <mark>陈俊逸、工院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）课程网站是Canvas平台, https://pku.instructure.com, 学校通知9月19日导入选课名单后启用。**作业写好后，保留在自己手中，待9月20日提交。**

提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale（10多分钟）

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：建一个列表，尽可能求所有负数的和。（其实是我没读懂题目，然后根据样例和测试数据的错误一步一步改出来的）



代码

```python
# 
n,m=map(int,input().split())
shuru=input().split()
a=[]
answer=0
for i in range(n):
    a.append(int(shuru[i]))
for i in range(m):
    if min(a)<=0:
        answer+=min(a)
        a.remove(min(a))
    else:
        break
if answer>=0:
    print(0)
else:
    print(-answer)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241018224616685](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241018224616685.png)



### 160A. Twins（12min）

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A

思路：不断取数最大值



代码

```python
num=int(input())
coins=list(map(int,input().split()))
#print(coins)
s=sum(coins)
m=max(coins)
i=0
i+=m
answer=1
while i<=s-m:
    s-=m
    answer+=1
    coins.remove(m)
    m=max(coins)
    i+=m
    #print(s,m)
print(answer)

```



代码运行截图 ==（至少包含有"Accepted"）==

**![image-20241019101223902](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241019101223902.png)**





### 1879B. Chips on the Board（30min）

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B

思路：算n*行最小加列总和的和行列互换的值 的最小值



代码

```python
def deal(n1,row,col):
    r=min(row)
    c=min(col)
    sr=sum(row)
    sc=sum(col)
    answer=0
    return (min(n1*r+sc,n1*c+sr))
n=int(input())
for i in range(n):
    n1=int(input())
    row=list(map(int,input().split()))
    col=list(map(int,input().split()))
    answer=deal(n1,row,col)
    print(answer)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241019104502492](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241019104502492.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：

类似于装箱问题，我用了的应该是数学的方法计算

代码

```python
n=int(input())
child=list(map(int,input().split()))
answer=0
a1=child.count(1)
a2=child.count(2)
a3=child.count(3)
a4=child.count(4)
answer+=a4+a3+int(a2/2)
a1-=a3
a2-=int(a2/2)*2
#print(a1,a2,a3,a4,answer)
if a2!=0:
    a1-=2
    answer+=1
if a1>0:
    answer+=int(a1/4)
    if a1%4!=0:
        answer+=1
print(answer)


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241019110842101](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241019110842101.png)



### *230B. T-primes（选做）（1h）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

基本写到学习总结部分了

代码

```python
import math
def zhishu(u):
    a=[True]*(u+1)
    a[0]=False
    a[1]=False
    z=[]
    for i in range(2,u+1):
        if a[i]:
            z.append(i)
        for p in z:
            if p*i>u:
                break
            a[p*i]=False
            if i%p==0:
                break
    return z
num=int(input())
n=list(map(int,input().split()))
z=set(zhishu(10**6))
#print(z)
for i in range(num):
    if n[i]==1:
        print('NO')
    else:
        b = int(math.sqrt(n[i]))
        if b * b != n[i]:
            print('NO')
        elif b in z:
            print('YES')
        else:
            print('NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241019124419398](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241019124419398.png)





### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

基本写到了学习总结与收获里

代码

```python
def h(x,y):
    if x+y>y+x:
        return x
    else:
        return y
def hh(x,y):
    if x+y>y+x:
        return y
    elif x+y<y+x:
        return x
    else:
        return y
num=int(input())
n=input().split()#str list
n1=n[:]
n2=n[:]
s=''
da=''
xiao=''
while n1:
    s=''
    for i in range(len(n1)):
        s=h(s,n1[i])
    #print(s)
    da+=s
    n1.remove(s)
while n2:
    s='999999999999999999999999999999999999999999999999999999999999999999999999999999999'
    for i in range(len(n2)):
        s=hh(s,n2[i])
    #print(s)
    xiao+=s
    n2.remove(s)
print(da,xiao)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241019141652016](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241019141652016.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

本周作业第三题有点坑，首先是英文题都不太懂，用翻译软件翻译出来的题目有点混乱，靠自己猜的解法才慢慢理解（不过cf有个好处是可以看见测试数据哪里错了，帮助我理解了题目），再加上样例图片的非完全正确的引导，导致我一直在理解这个题目（理解后代码也就几行，但改了又改很浪费时间）

第四题借助ai让我学会了count的用法（不然老用 if item in list 会超时）

吃饭真的管用（doge）早上写t-prime的时候没啥思路，在吃饭的路上想到了测试36超时的方法，吃完饭歇了一会又想到了58超时的方法。但最后发现，其实一开始的思路也是对的 （由于不会一些质数的筛选方法，导致测试数据1就超时了），但通过ai，我也由这道题学会了很多优化代码的思路以及最重要的——欧拉筛。还有就是集合比列表快很多，优化完算法后，我最后一次就是把列表换成集合就过了（太不容易了）。我发现每次大的提升确实是在做难题以及看难题答案的时候。

最后一题想了一个半小时思路卡在了（比如给21和212怎么排，这类数据上），后来发现思路有点跑偏了。最后大概看了一眼ai的思路，才发现可以用类似冒泡排序的方法做，然后剩下自己独立完成并ac（很多时候思路就差呢么临门一脚）

上周（包括现在）眼睛犯结膜炎了，每日选座落下了好多。等眼睛好了以后会慢慢跟进。
