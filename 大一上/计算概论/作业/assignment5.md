# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>陈俊逸，工学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期（之前做过）

brute force, http://cs101.openjudge.cn/practice/04148

思路：

代码：

```python
def zhouqi(a,a1,b,b1):
    while a!=b:
        if a>b:
            b+=b1
            continue
        a+=a1
    return (a)
i=1
while True:
    a,b,c,d=map(int,input().split())
    if a==b==c==d==-1:
        break
    answer=0
    k=zhouqi(a,23,b,28)
    #print(k)
    answer+=zhouqi(c,33,k,644)
    answer-=d
    #print(a,b,c,d)
    if answer<=0:
        answer+=21252
    print('Case ',i,': the next triple peak occurs in ',answer,' days.',sep='')
    i+=1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241026102359628](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241026102359628.png)





### 18211: 军备竞赛（13min）

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

思路：挑最小的买，挑最大的卖

代码：

```python
money=int(input())
l=list( map( int,input().split() ) )
wo,di=0,0
while l:
    xiao=min(l)
    da=max(l)
    if money>=xiao:
        money-=xiao
        wo+=1
        l.remove(xiao)
    elif wo>di and money<xiao and len(l)!=1:
        money+=da
        di+=1
        l.remove(da)
    else:
        break
print(wo-di)
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241026123109203](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241026123109203.png)

### 21554: 排队做实验（25min）

greedy, http://cs101.openjudge.cn/practice/21554

思路：

快排排序，输出索引，算等待时间，求平均时间

代码：

```python
def quicksort(l):
    if len(l) <= 1:
        return l
    else:
        a=l[0]
        left=[x for x in l if x<a]
        m=[x for x in l if x==a]
        right=[x for x in l if x>a]
        return quicksort(left)+m+quicksort(right)
n=int(input())
l=list(map(int,input().split()))
l1=quicksort(l)
#print(l1)
answer=0.0
for i in range(len(l1)):
    p=l.index(l1[i])
    print(p+1,end=' ')
    l[p]=-1
    answer+=(n-i-1)*l1[i]
    #print(answer)
print()
answer/=n
print("{:.2f}".format(answer))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241026130819086](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241026130819086.png)



### 01008: Maya Calendar（40min）

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

建字典，算总天数，先算年，再算13和20的一个循环

代码：

```python
num=int(input())
print(num)
haab={'pop':0,'no':20,'zip':40,'zotz':60,'tzec':80,'xul':100,'yoxkin':120,'mol':140,'chen':160,'yax':180,'zac':200,'ceh':220,'mac':240,'kankin':260,'muan':280,'pax':300,'koyab':320,'cumhu':340,'uayet':360}
tzolkin={1:'imix',2:'ik',3:'akbal',4:'kan',5:'chicchan',6:'cimi',7:'manik',8:'lamat',9:'muluk',10:'ok',11:'chuen',12:'eb',13:'ben',14:'ix',15:'mem',16:'cib',17:'caban',18:'eznab',19:'canac',20:'ahau'}
day=0
for i in range(num):
    shuru=input().split()
    day=int(shuru[0][:len(shuru[0])-1])+haab.get(shuru[1])+365*int(shuru[2])
    #print(day)
    year=day//260
    day%=260
    day+=1
    month=day%13
    if month==0:
        month=13
    day%=20
    if day==0:
        day=20
    print(month,tzolkin.get(day),year)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241026135138604](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241026135138604.png)



### 545C. Woodcutters（40min）

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：尽量左倒，最边上两个向外倒（也可能是一个，比如test9）

代码：

```python
n=int(input())
x=[]
h=[]
for i in range(n):
    shuru=input().split()
    x.append(int(shuru[0]))
    h.append(int(shuru[1]))
if n==1:
    answer=1
else:
    answer=2
c=True
for i in range(1,n-1):
    m=x[i]
    if x[i]-h[i]>x[i-1]:
        answer+=1
        continue
    if x[i]+h[i]<x[i+1]:
        answer+=1
        x[i]+=h[i]
print(answer)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>



![image-20241026144031375](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241026144031375.png)

### 01328: Radar Installation（40min）

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

先把每一个岛屿对应的x范围求出来，然后进行区间找点的运算

代码：

```python
import math
num=0
def qujian(l):
    l.sort(key = lambda x : x[1])
    ed=l[0][1]
    re=1
    for i in range(1,len(l)):
        if l[i][0]<=ed:
            pass
        else:
            re+=1
            ed=l[i][1]
    return re
while True:
    answer=0
    shuru=input()
    if shuru=='':
        continue
    n,d=map(int,shuru.split())
    if n==d==0:
        break
    num+=1
    x=[]
    for i in range(n):
        sx,sy=map(int,input().split())
        if d**2<sy**2 or d<0:
            answer=-1
        s=d*d-sy*sy
        if s<=0:
            s=0
        dx=math.sqrt(s)
        x.append([sx-dx,sx+dx])
    if answer==-1:
        print('Case ',num,': ',answer,sep='')
    else:
        answer=qujian(x)
        print('Case ',num,': ',answer,sep='')


```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241026153337292](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241026153337292.png)

## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

军备竞赛一题，漏了题目一个条件，导致浪费了时间。（审题很重要）

第一次写woodcutters时居然超内存了，之前从没有碰到过，可能还是对10的9次方不太敏感。思路是对的但是实现起来有点复杂了，后续稍微优化了一下就通过了（有一个坑点是n=1的情况，还好cf可以看测试数据，如果在oj上的话我估计要卡很久）

最后一题很有收获，首先是一些没想到的坑点，比如d他居然还能给负的（~~要是没有群里的测试数据的话我估计我这辈子也想不到这个坑点~~）；还有就是通过ai学会了如何对于一个空行不做处理且不报错；最后是，虽然思路很快就有了，虽然做这道题前一天复习了一遍上课的pdf，但在把区间取点问题的思路转化为代码是还是有卡壳。我觉得还是不熟练吧，后续我打算抽时间默写一下我之前学过的重要代码，比如欧拉筛，快速排序，五类区间问题（目前我能想到的）。

最近感觉题目难度上了一个很大的台阶，一般来说，如果有测试数据的话，不用ai大概每一题要花上40min左右（这次作业基本就是）。开始有点担心考试了（感觉就6个题，少一个题就会少很多分），不过学期才过一半，我也感觉通过大量的自学渐渐入门了，相信后续练习能继续提升能力。

相信没有白做的题，没有白踩的坑。
