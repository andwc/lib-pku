# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>陈俊逸，工院</mark>



**说明：**

1）⽉考： AC6<mark>（3）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队（考试用时13min，ac）

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

分成大小两个，大的进行排序，小的直接输出

代码：

```python
n=int(input())
idx=[]
idd=[]
agex=[]
aged=[]
for i in range(n):
    a,b=input().split()
    b=int(b)
    if b>=60:
        idd.append(a)
        aged.append(int(b))
    else:
        idx.append(a)
        agex.append(int(b))
p=len(aged)
for i in range(p):
    m=max(aged)
    index=aged.index(m)
    print(idd[index])
    aged[index]=0
for i in idx:
    print(i)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108101726191](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241108101726191.png)



### E23555: 节省存储的矩阵乘法（考试用时13min，ac）

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

正常进行矩阵运算，碰到非0进行输出

代码：

```python
n,m1,m2=map(int,input().split())
a=[[0 for _ in range(n)]for _ in range(n)]
b=[[0 for _ in range(n)]for _ in range(n)]
c=[[0 for _ in range(n)]for _ in range(n)]
for i in range(m1):
    shuru=list(map(int,input().split()))
    a[shuru[0]][shuru[1]]=shuru[2]
for i in range(m2):
    shuru=list(map(int,input().split()))
    b[shuru[0]][shuru[1]]=shuru[2]
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j]+=a[i][k]*b[k][j]
for i in range(n):
    for j in range(n):
        if c[i][j]!=0:
            print(i,j,c[i][j])
```



代码运行截图 ==（至少包含有"Accepted"）==



![image-20241108101837068](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241108101837068.png)

### M18182: 打怪兽 (考试用时30min左右，wa)

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：按时间顺序查找同时间下前m个扣血最多的技能（思路很好想，但代码实现起来会出现很多问题）

代码：

```python
ncase=int(input())
for _ in range(ncase):
    t=[]
    x=[]
    n,m,b=map(int,input().split())
    for i in range(n):
        ti,xi=map(int,input().split())
        t.append(ti)
        x.append(xi)
    ts=sorted(t)
    t0=-1
    xue=0
    for i in ts:
        if i!=t0:
            t0=i
            for j in range(m):
                xue = 0
                index=0
                for k in range(n):
                    if t[k] == i:
                        if xue<=x[k]:
                            xue = x[k]
                            index=k
                b-=xue
                x[index]=0
            #print(t0,b)
            if b<=0:
                break
    if b<=0:
        print(t0)
    else:
        print('alive')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108101552264](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241108101552264.png)

### M28780: 零钱兑换3（考试用时40min左右，tle）

dp, http://cs101.openjudge.cn/practice/28780/

思路：一维数组，从1开始不断dp，考虑拿各个硬币的最优解

代码：

```python
n,m=map(int,input().split())
c=list(map(int,input().split()))
jj=1
dp=[-1 for _ in range(m+1)]
for j in range(1, m + 1,jj):
    if j in c:
        dp[j] = 1
        if j==min(c):
            jj=min(c)
        continue
    for i in range(n):
        if dp[j - c[i]] == -1 :
            continue
        else:
            if dp[j]!=-1:
                dp[j] = min(dp[j],1 +dp[j - c[i]])
            else:
                dp[j]=1 +dp[j - c[i]]
a=dp[-1]
#print(dp)
print(a)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108120409202](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241108120409202.png)



### T12757: 阿尔法星人翻译官（考试用时20min左右，ac）

implementation, http://cs101.openjudge.cn/practice/12757

思路：有点屎山，但本质就是ifelse加读数，思路不卡

代码：

```python
d={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'forty':40, 'fifty':50, 'sixty':60, 'seventy':70,'eighty':80,'ninety':90,'hundred':100,'thousand':1000,'million':1000000}
s=list(map(str,input().split()))
n=len(s)
a,b,c,e=0,0,0,0
ans=0
if s[0]=='negative':
    for i in range(1,n):
        if s[i]=='million':
            ans+=a*1000000
            a=0
        else:
            if s[i] == 'thousand':
                ans += a * 1000
                a=0
            else:
                if s[i] == 'hundred':
                    a= a * 100
                else:
                    a+=d.get(s[i])
        #print(ans,a)
    ans+=a
    ans=0-ans
    print(ans)
else:
    for i in range(n):
        if s[i] == 'million':
            ans += a*1000000
            a = 0
        else:
            if s[i] == 'thousand':
                ans += a * 1000
                a = 0
            else:
                if s[i] == 'hundred':
                    a = a * 100
                else:
                    a += d.get(s[i])
        # print(ans,a)
    ans += a
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108102054447](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241108102054447.png)



### T16528: 充实的寒假生活（考试未做到）（下来20min左右）

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：选择最多的不重叠的区间个数（10.22讲过）

代码：

```python
n=int(input())
p=[]
import sys
for i in range(n):
    shuru=input().split()
    p.append((int(shuru[0]),int(shuru[1])))
p.sort(key=lambda x: x[1])
ed=-sys.maxsize
res=0
for v in p:
    if ed < v[0]:
        res += 1
        ed = v[1]
print(res)
#print(p)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![image-20241108123347515](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241108123347515.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

考试收获：

1.一般碰到错误就有些蒙，不知道自己哪里出错了，会很浪费时间

2.对数据大小不敏感，找零问题明显数据较大，结果第一次mle，第二次tle，浪费了大量的时间

3.找零tle，但当时我忘记了pypy会快很多，结果下来回宿舍了才想起来，拿pypy交就ac了，我真服了（本来可以多对一道的，但还好不是期末考试）

4.打怪兽一题，下来用ai debug发现，index只是列表中第一个的index，之前老师说很容易出错，这次深有体会，其实我只要中间记录一下index就好了，哎。

总结：这次月考本身题目不算特别难，但总有让我踩坑的地方，比如打怪兽的index，找零的tle，区间问题的不太熟练等等，对我而言是有很大的收获的。
