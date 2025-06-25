#因为每日选做最后又加了奇奇怪怪的题，比如差分，kmp等内容，我也都补充进来了，以防万一
#因为每日选做前期全都是计概的内容，所以binary search，manacher，greedy和dp乱七八糟的东西也加进来了。不过应该不会是考核重点，所以只加入了模板进来，考试的时候碰到类似的题有东西抄就行了。
#东西好像有点多了，前面加*的内容都是非重点内容，导出pdf时可以删去一部分
#我又把dp和greedy的删了，貌似不考模板题

 																									by 陈俊逸 工院

# pycharm调整：

1.实现按住 ctrl +滑动鼠标滚轮实现代码窗口字体大小调整：

**File** 一>**Settings** 一>**Editor**一>**General**里 的**Mouse Control**把**Change font size with Ctrl+Mouse Wheel**打上对勾，点击**OK**即可

2.确保编译文件是current file

# 小寄巧：

print(f'{ans},{res:.1f}')print是可以带sep和end参数的

可以用round进行四舍六入五成双的操作

枚举：  for i,x in enumerate(list),遍历list中的（下标，值）对

集合：
并：’|‘    交：’&‘     差：‘-‘    

# OOP：


 | `__eq__(self, other)` | `==` | 判断相等 |
 | `__ne__(self, other)` | `!=` | 判断不相等 |
 | `__lt__(self, other)` | `<` | 判断是否小于 |
 | `__le__(self, other)` | `<=` | 判断是否小于等于 |
 | `__gt__(self, other)` | `>` | 判断是否大于 |
 | `__ge__(self, other)` | `>=` | 判断是否大于等于 |

| 方法名                                                     | 用途说明                        |
| ---------------------------------------------------------- | ------------------------------- |
| `__init__`                                                 | 构造函数，创建对象时自动调用    |
| `__del__`                                                  | 析构函数，对象删除前调用        |
| `__str__`                                                  | 控制 `print(obj)` 时的输出      |
| `__repr__`                                                 | 控制对象在解释器中的表现        |
| `__len__`                                                  | 支持 `len(obj)`                 |
| `__getitem__`                                              | 支持 `obj[key]`                 |
| `__setitem__`                                              | 支持 `obj[key] = value`         |
| `__iter__`                                                 | 使对象可迭代（如用于 for 循环） |
| `__next__`                                                 | 支持迭代器的下一个元素          |
| `__call__`                                                 | 使对象可以像函数一样调用        |
| `__enter__` / `__exit__`                                   | 用于上下文管理器（with 语句）   |
| `__eq__`, `__lt__`, `__gt__`, `__ne__`, `__le__`, `__ge__` | 比较运算                        |
| `__add__`, `__sub__`, `__mul__`, 等等                      | 支持算术运算符重载              |

# 一些错误总结：

## Compile Error：

​	1.这个多半是变量名字打错了，或者多打；：之类的，这个好查，一般本地都运行不了。

​	2.OJ的pylint是静态检查，有时候报的compile error不对。解决方法有两种，如下：

​		1）第一行加# pylint: skip-file
​		2）方法二：如果函数内使用全局变量（变量类型是immutable，如int），则需要在程序最开始声明一下。如果是全局变量是list类型，则不受影响。

## Runtime Error：

​	1.指针越界，比如长度为5（index为0，1，2，3，4）的数组你去获取list[5]，但是注意list[-5]是合法的（index可以为-1，-2，-3，-4，-5）。

​	2.数组开太大了，比如开到1000000000（9个0）就会

​	3.递归爆栈：这个用以下代码解决

```python
from sys import setrecurisonlimit
setrecursionlimit(10000)#python 默认 200
```

​	4.输入读取错误，一般是输入没读完就exit（）    （所以要谨慎使用这个函数）

​	5.除以0，检查一下变量是不是可以是0

## Wrong Answer

​	这个需要好好审一遍代码

​	如果没有逻辑性的错误，就查一下边界值，比如0啊1啊什么的，很可能在这些地方出错

​	如果还不行，就仔细审题，看看哪个地方理解错了

## Presentation Error

​	只遇到过一次，就是该输出空行的时候没输出空行

## Time Limit Exceeded

​	1.死循环（这种在BFS类里容易碰到，要注意visited的逻辑是否正确）

​	2.算法问题（注意每次读题时注意数据量，以便快速确定算法）

​	3.卡常数，这种情况用pypy3就可以了，或者再优化一下代码，去除一些鸡肋的O（n）操作

## Memory Limit Exceeded

​	数组开太大了，一般DP难题会遇到，这时候就要考虑压缩空间了。

​	还有就是BFS的时候queue可能会超，要考虑进堆的数据的优化

# 常用库

```python
#堆
import heapq
#队列(default字典)
from collections import deque(defaultdict)
#递归上限
from sys import setrecursionlimit
#缓存
from functools import lru_cache
#数学***math库***：最常用的sqrt,对数log(x[,base])、三角sin()、反三角asin()也都有；还有e,pi等常数，inf表示无穷大；返回小于等于x的最大整数floor（）,大于等于ceil（）,判断两个浮点数是否接近isclose（a，b，*, rel_tol=1e-09, abs_tol=0.0）；一般的取幂pow（x，y）,阶乘factorial（x）如果不符合会ValueError,组合数comb（n，k）`math.radians()`将度数转换为弧度，或者使用`math.degrees()`将弧度转换为度数。
import math
#二分库
import bisect
bisect.bisect_right(a,6)#返回在a列表中若要插入6的index（有重复数字会插在右边）
bisect.insort(a,6)#返回插入6后的列表a
#conuter
from collections import Counter
```



# data structures：

说实话这部分考到的概率不大，还是梳理了一下。（只放了思路，代码就现场慢慢手敲吧）

LRU呢个题，字典的value是node，用双向链表实现访问时间的顺序<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250527194013383.png" alt="image-20250527194013383" style="zoom:5%;" />

快速求中位数，用两个堆<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250527195044310.png" alt="image-20250527195044310" style="zoom:5%;" />

最大词频表的结构<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250527195600811.png" alt="image-20250527195600811" style="zoom:5%;" />

返回最大（小）词频的字符串（O（1））。用桶+双链表实现<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250527201132378.png" alt="image-20250527201132378" style="zoom:5%;" />

# 妙妙算法：

## 排序：

### 冒泡排序：

```python
for i in range(n):
	ok=True
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
			arr[j],arr[j+1]=arr[j+1],arr[j]
            ok=False
	if ok:
        break
```

### 快速随机排序：

```python
def quicksort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i <= j:
        while i <= right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i
```

### 分治排序

```python
def mergeSort(arr):
	if len(arr) > 1:
		mid = len(arr)//2
		L = arr[:mid]	# Dividing the array elements
		R = arr[mid:] # Into 2 halves
		mergeSort(L) # Sorting the first half
		mergeSort(R) # Sorting the second half
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] <= R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
		# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1
```



## *Kadane's(最大子数组)

```python
def max_subarray_sum(arr):
    if not arr:
        return 0
    max_current=max_global=arr[0]
    for num in arr[1:]:
        max_current =max(num,max_current+num)
        if max_current>max_global:
			max_global= max_current
    return max_global
```

推广：最大子矩阵

```python
'''
为了找到最大的非空子矩阵，可以使用动态规划中的Kadane算法进行扩展来处理二维矩阵。
基本思路是将二维问题转化为一维问题：可以计算出从第i行到第j行的列的累计和，
这样就得到了一个一维数组。然后对这个一维数组应用Kadane算法，找到最大的子数组和。
通过遍历所有可能的行组合，我们可以找到最大的子矩阵。
'''
def max_submatrix(matrix):
    def kadane(arr):
      	# max_ending_here 用于追踪到当前元素为止包含当前元素的最大子数组和。
        # max_so_far 用于存储迄今为止遇到的最大子数组和。
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
          	# 对于每个新元素，我们决定是开始一个新的子数组（仅包含当前元素 x），
            # 还是将当前元素添加到现有的子数组中。这一步是 Kadane 算法的核心。
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                temp[row] += matrix[row][right]
            max_sum = max(max_sum, kadane(temp))
    return max_sum

n = int(input())
nums = []

while len(nums) < n * n:
    nums.extend(input().split())
matrix = [list(map(int, nums[i * n:(i + 1) * n])) for i in range(n)]

max_sum = max_submatrix(matrix)
print(max_sum)
```



## 欧拉筛：

```python
def oula(a):
    zhishu=[]
    zhishu1=[True]*(a+1)
    for i in range(2,a+1):
        if zhishu1[i]:
            zhishu.append(i)
        for h in zhishu:
            if h*i<=a:
                zhishu1[h*i]=False
    zhishu=set(zhishu)
    return zhishu
```



## *前缀和：

最早出现前缀和=aim：用哈希表（记得加0：-1）

判断正负数个数：先把正数改成1，负数改成-1   九把问题变成了sum=0的问题

元音呢个题，用一个int来存储状态，转化成前缀和的题

## *差分：

理解为前缀和的逆运算

e.g:

```python
nums=[...]
new_nums=[0...0]
#2~5,+3
new_nums[2]=3
new_nums[5+1]=-3
...
最后的nums就是new_nums前缀和的结果
```

等差数列差分：（越界了不加就行，但是需要判断，所以复杂的情况下可以加个offset避免越界）
<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250529123238706.png" alt="image-20250529123238706" style="zoom:5%;" /><img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250529123436278.png" alt="image-20250529123436278" style="zoom:5%;" />



## *二维前缀和：

操作：左+上-左上+自己（意义：从0，0到i，j的sum）

查询：从i，j到x，y：x，y减x，j-1减i-1，y加i-1，j-1

注意要套一个保护圈（减少条件判断）

## *二维差分：

操作：<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250529130956815.png" alt="image-20250529130956815" style="zoom:5%;" />

处理：二位前缀和

## binary search：

过程：

​	估计答案范围（可以很粗略）；
​	判断有无单调性；
​	建立check函数；
​	复杂度一般为O（nlogn），10^5以上就可以考虑了。

tips：

注意check函数中的mid不能是0，就是要注意除0的情况（网线主管那一题）
注意二分的是答案，画家画画呢个题，二分的是时间，然后判断画家数够不够。
第k小的插值：二分有没有k对小于mid，然后check是一个滑动窗口。
正难则反：刀和毒打怪兽呢个题就是这个思路（回合数以确定，毒的伤害就确定了，这样就可以贪心了）

贴一个小模板（河中跳房子）：

```python
l,n,m=map(int,input().split())
p=[]
for _ in range(n):
    p.append(int(input()))
p.append(l)
def check(t):
    global p,l,m
    pre=0
    cnt=0
    for i in range(len(p)):
        if p[i]-pre<t:
            cnt+=1
        else:
            pre=p[i]
        if cnt>m:
            return False
    return True
left,right=0,l
ans=0
while left<right:
    mid=(left+right)//2
    if check(mid):
        ans=mid
        left=mid+1
    else:
        right=mid
print(ans)
```



## sliding window：

滑动窗口：维持左右边界都不回退的一段范围，来求解很多子数组的相关问题

关键：找到 **范围** 和 **答案指标** 之间的 **单调性关系**

过程：可以用简单变量或者结构来维护信息

大流程：求子数组在每个位置 开头或结尾的情况下的答案

for 枚举右边界：
	while 枚举左边界：
	if 条件：
		ans更新

## *KMP

<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250526203520782.png" alt="image-20250526203520782" style="zoom: 25%;" />

```python
def kmp(s1,s2):
    n,m=len(s1),len(s2)
    x,y=0,0
    nt=nextarray(s2,m)
    while x<n and y<m:
        if s1[x]==s2[y]:
            x+=1
            y+=1
        elif y==0:
            x+=1
        else:
            y=nt[y]
    return x-y if y==m else -1
def nextarray(s,m):
    if m==1:
        return [-1]
    nt=[0]*m
    nt[0],nt[1]=-1,0
    i,cn=2,0
    while i<m:
        if s[i-1]==s[cn]:
            cn+=1
            nt[i]=cn
            i+=1
        elif cn>0:
            cn=nt[cn]
        else:
            nt[i]=0
            i+=1
    return nt
```



## *Manacher：

<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250526222836418.png" alt="image-20250526222836418" style="zoom:25%;" />

```python
def manacher(s):
    ss= '#' + '#'.join(s) + '#'
    n=len(ss)
    p=[0]*n
    ans=0
    c,r=0,0
    for i in range(n):
        length=min(p[2*c-i],r-i) if r>i else 1
        while i+length<n and i-length>=0 and ss[i + length]==ss[i - length]:
            length+=1
        if i+length>r:
            r=i+length
            c=i
        ans=max(ans,length)
        p[i]=length
    return ans-1
```



## 嵌套问题：

大概过程：

​	1.定义全局变量where
​	2.递归函数f（i）：s[i..]从i位置出发开始解析，遇到字符串终止 或 嵌套条件终止 就返回
​	3.返回值f(i)负责这一段的结果
​	4.f(i)在返回前更新的全局变量where，让上级函数通过where指导解析到了什么位置，进而继续

执行细节：

​	1.如果f(i)遇到 嵌套条件开始，就调用下级递归去处理嵌套，下级会负责嵌套部分的计算结果
​	2.f(i)下级处理完成后，f(i)可以根据下级更新的全局变量where，指导该从什么位置继续解析

e.g.括号嵌套树（重点是f函数）

```python
class treenode:
    def __init__(self,val):
        self.val=val
        self.children=[]
def preorder(root):
    if not root:
        return []
    ans=[root.val]
    for i in root.children:
        ans.extend(preorder(i))
    return ans
def postorder(root):
    if not root:
        return []
    ans=[]
    for i in root.children:
        ans.extend(postorder(i))
    return ans+[root.val]
def show(root):
    print(''.join(preorder(root)))
    print(''.join(postorder(root)))
    return
s=input()
where=0
def f(i):
    global where,s
    st=[]
    while i<len(s) and s[i]!=')':
        if s[i]==',':
            i+=1
        elif 'A'<=s[i]<='Z':
            st.append(treenode(s[i]))
            i+=1
        elif s[i]=='(':
            st[-1].children=f(i+1)
            i=where+1
    where=i
    return st
root=f(0)[0]
show(root)
```

# *linked list: 

## 快慢指针：

```python
slow,fast=head,head
while fast.next and fast.next.next:
    slow=slow.next
    fast=fast.next.next
#slow此时是中偏左位置
slow=slow.next
```

## 反转链表：

单链表：

```python
def fan(head):
    pre,cur=None,head
    while cur:
        tmp=cur.next
        cur.next=pre
        pre=cur
        cur=tmp
    return pre
```

双链表：

```python
def fan(head):
    pre,nt=None,None
    while head!=None:
        nt=head.next
        head.next=pre
        head.last=nt#last表示上一个
        pre=head
        head=nt
    return pre
```

## 链表判断环：

```python
def detectCycle(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    slow=head.next
    fast=head.next.next
    while slow!=fast:
        if fast.next is None or fast.next.next is None:
            return None
        slow=slow.next
        fast=fast.next.next
    fast=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow
```



# stack	

## 单调栈：（来自柱状图最大矩形，具体题目需要变形）

求左右最近的小于自身的数：<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250529142650463.png" alt="image-20250529142650463" style="zoom:5%;" /><img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250529142831486.png" alt="image-20250529142831486" style="zoom:5%;" />

有重复数字也是一样的操作（等于也弹出），但是最后要进行一遍右答案的修正（因为有可能记录的是相等的值）（从右往左修正）

```python
#求左右两边严格小于自身的最近的数 并且有重复值 的模板
#遍历
for i in range(n):
    while st and arr[st[-1]]>=arr[i]:#不严格不用清算
        cur=st.pop()
        ans[cur][0]=st[-1] if st else -1
        ans[cur][1]=i
    st.append(i)
#清算
while st:
    cur=st.pop()
    ans[cur][0]=st[-1] if st else -1
    ans[cur][1]=-1
#修正
#n-1一定是-1，所以不需要修正
for i in range(n-2，-1,-1):
    if ans[i][1]!=-1 and arr[ans[i][1]]==arr[i]:
        ans[i][1]=ans[ans[i][1]][1]
```

重复一定要特判，子数组一题重复的就要作为ans才可以不重不漏。有些时候中间的相等值答案可能不对，只要后续的相等值进来能把答案修正对就可以了（回忆最大矩形一题，相等也弹出）

妙题：01矩阵中面积最大的长方形：枚举每一行，以每一行作为底去进行单调栈即可（不连续就变成0，还要记得复用上一行的数据）

其他用法：维持答案的一种可能性，比如求数组中的坡，维持栈中是递减的，遇到大的弹出，然后再从右往左更新答案。
		比如字典序最小的规定字符的字符串，先用counter记录能不能删某个字符，再用单调栈去维护字典序最小

## 最小栈：

比较+取小的压入新栈

## 中序转后序Shunting Yard：

基本步骤：

1. 初始化运算符栈和输出栈为空。
2. 从左到右遍历中缀表达式的每个符号。
   - 如果是操作数（数字），则将其添加到输出栈。
   - 如果是左括号，则将其推入运算符栈。
   - 如果是运算符：
     - 如果运算符的优先级大于运算符栈顶的运算符，或者运算符栈顶是左括号，则将当前运算符推入运算符栈。
     - 否则，将运算符栈顶的运算符弹出并添加到输出栈中，直到满足上述条件（或者运算符栈为空）。
     - 将当前运算符推入运算符栈。
   - 如果是右括号，则将运算符栈顶的运算符弹出并添加到输出栈中，直到遇到左括号。将左括号弹出但不添加到输出栈中。
3. 如果还有剩余的运算符在运算符栈中，将它们依次弹出并添加到输出栈中。
4. 输出栈中的元素就是转换后的后缀表达式。

```python
def turn(s):
    fuhao={'+':1,'-':1,'*':2,'/':2}
    stack=[]
    ans=[]
    num=''
    for i in s:
        if i in '0123456789.':
            num+=i
        else:
            if num:
                ans.append(num)
                num=''
            if i in '+-*/':
                while stack and stack[-1] in '+-*/' and fuhao[i]<=fuhao[stack[-1]]:
                    ans.append(stack.pop())
                stack.append(i)
            elif i=='(':
                stack.append(i)
            elif i==')':
                while stack and stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
    if num:
        ans.append(num)
    while stack:
        ans.append(stack.pop())
    return ' '.join(str(i) for i in ans)
case=int(input())
for _ in range(case):
    s=input()
    print(turn(s))
```

# tree：

## 经典题型

### 遍历：

前中后序：递归实现（stack）

层序：BFS实现（queue）

非递归实现中序：

​	1.子树（头），左边界进栈（完全）
​	2.栈弹出的节点print，节点右树进栈并重复1
​	3.没子树且栈空：完成

### 宽度深度：

层宽：用编号，然后相减

深度：递归return max（孩子高度）+1

最小深度：递归 return min（孩子深度）+1  注意空节点会干扰递归，所以要先把孩子深度设为inf，如果不是空了再修改其值。

### 序列化（转成字符串，+‘#’）：

先序：<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250528143108594.png" alt="image-20250528143108594" style="zoom:5%;" />

中序不能序列化

后序是类似的

层序是BFS：<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250528143812394.png" alt="image-20250528143812394" style="zoom:5%;" />

### 反序列化：

先序：

```python
def g(vals):
    global cnt
    cur=vals[cnt]
    cnt+=1
    if cur=='#':
        return None
    else:
        head=TreeNode(int(cur))
        head.left=g(vals)
        head.right=g(vals)
        return head
vals=s.split(',')
cnt=0
head=g(vals)
```

层序：

```python
def generate(val):
    return None if val=='#' else treenode(int(val))
index=0
root=generate(s[index])
index+=1
queue=deque()
while queue:
    cur=queue.popleft()
    cur.left=generate(s[index])
    index+=1
    cur.right=generate(s[index])
    index+=1
    if cur.left is not None:
        queue.append(cur.left)
    if cur.right is not None:
        queue.append(cur.right)
```

### 先中转后：

可以先拿dict记一下中序每个数的位置，更快

### 判断完全二叉树：

1.有右无左：false
2.一旦发现有左无右：queue里的必须全是叶节点

### 算完全二叉树节点个数：

1.先不断left得到左边高度：
2.算右树高度：
	2.1如果右树高度=左=L：左树个数=2^（L-1）-1，递归解决右树节点个数
	2.2如果右树高度=L-1，右树个数=2^（L-2）-1，递归解决左树节点个数

返回1+左树节点个数+右树节点个数

### lca问题（寻找最早公共祖先）

```python
def lowestCommonAncestor(root,p,q):
    if root is None or p is None or q is None:
        return root
    l=lowestCommonAncestor(root.left,p,q)
    r=lowestCommonAncestor(root.right,p,q)
    if l is not None and r is not None:
        return root
    if l is None and r is None:
        return None
    return l if l is not None else r
```

### 判断平衡二叉树、判断搜索二叉树：(tree dp)

### 修剪搜索二叉树：

```python
def trimBST(cur,low,high):
    if cur is None:
        return None
    if cur.val<low:
        return trimBST(cur.right,low,high)
    if cur.val>high:
        return trimBST(cur.left,low,high)
    cur.left=trimBST(cur.left,low,high)
    cur.right=trimBST(cur.right,low,high)
    return cur
```



## 树形DP： 

套路：

​	1.分析父树得到答案需要子树的哪些信息
​	2.把子树的信息的全集定义成返回值
​	3.通过递归让子树返回全集信息
​	4.整合子树的全集信息得到父树的全集信息并返回

一般来说：空树的max是-inf，min是inf，这样不会干扰信息

## 前缀树trie

<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250528162917840.png" alt="image-20250528162917840" style="zoom:5%;" />

tips：

​	数组呢个题用num+#把它改成字符串，这样只有0-9和-和#，这样就不会爆空间
​	最大异或值也可以用前缀树来实现
​	表格中查单词：用前缀树来剪枝

```python
class Trie:
    class TrieNode:
        def __init__(self):
            self.p=0
            self.e=0
            self.next=[None]*26
            #若不仅仅是字母还有多个字符的话可以用dict优化{字母：下一个节点}

    def __init__(self):
        self.root=self.TrieNode()

    def insert(self,word):
        node=self.root
        node.p+=1
        for i in range(len(word)):
            path=ord(word[i])-ord('a')
            if node.next[path] is None:
                node.next[path]=self.TrieNode()
            node=node.next[path]
            node.p+=1
        node.e+=1
        return

    def search(self,word):
        node=self.root
        for i in range(len(word)):
            path=ord(word[i])-ord('a')
            if node.next[path] is None:
                return 0
            node=node.next[path]
        return node.e

    def startsWith(self,word):
        node=self.root
        for i in range(len(word)):
            path=ord(word[i])-ord('a')
            if node.next[path] is None:
                return 0
            node=node.next[path]
        return node.p

    def delete(self,word):
        if self.search(word)>0:
            node=self.root
            node.p-=1
            for i in range(len(word)):
                path=ord(word[i])-ord('a')
                if node.next[path].p==1:
                    node.next[path]=None
                    return
                node=node.next[path]
                node.p-=1
            node.e-=1
        return
```



## huffman：

给个例子应该就能想起来咋写的了，用heap

<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250517215803380.png" alt="image-20250517215803380" style="zoom: 15%;" />

```python
import heapq
class node:
    def __init__(self, char,freq):
        self.char = char
        self.left=None
        self.right=None
        self.freq=freq
    #用于比较
    def __lt__(self, other):
        if self.freq==other.freq:
            return self.char<other.char
        return self.freq<other.freq
def build_huffman(d):
    q=[]
    for char,freq in d.items():
        heapq.heappush(q,node(char,freq))
    heapq.heapify(q)
    while len(q)>1:
        left=heapq.heappop(q)
        right=heapq.heappop(q)
        if left.char<right.char:
            c=left.char
        else:
            c=right.char
        nn=node(c,left.freq+right.freq)
        nn.left=left
        nn.right=right
        heapq.heappush(q,nn)
    return heapq.heappop(q)
def build_code(root):
    stack=[(root,'')]
    di={}
    dic={}
    while stack:
        x,y=stack.pop()
        if x.left:
            stack.append((x.left,y+'0'))
        if x.right:
            stack.append((x.right,y+'1'))
        if not x.left and not x.right:
            di[x.char]=y
            dic[y]=x.char
    return di,dic
n=int(input())
d={}
for i in range(n):
    char,freq=input().split()
    freq=int(freq)
    d[char]=freq
root=build_huffman(d)
d_str,d_num=build_code(root)
while True:
    try:
        s=input()
        if s[0]=='0' or s[0]=='1':
            a=''
            for i in s:
                a+=i
                if a in d_num:
                    print(d_num[a],end='')
                    a=''
        else:
            for i in s:
                print(d_str[i],end='')
        print()
    except EOFError:
        break
```

## disjointset

```python
class disjointset:
    def __init__(self,n):
        self.father=[x for x in range(n)]
        self.dict={}
    def find(self,x):
        stack=[]
        while self.father[x]!=x:
            stack.append(x)
            x=self.father[x]
        for i in stack:
            self.father[i]=x
        return x
    def issameset(self,x,y):
        return self.find(x) == self.find(y)
    def union(self,x,y):
        fx=self.find(x)
        fy=self.find(y)
        if fx!=fy:
            self.father[fy]=fx
```

## heap

```python
class xiaoheap:
    def __init__(self):
        self.heaplist=[0]
        self.size=0
    def percup(self,i):
        while i//2>0:
            if self.heaplist[i]<self.heaplist[i//2]:
                self.heaplist[i],self.heaplist[i//2]=self.heaplist[i//2],self.heaplist[i]
            i//=2
    def insert(self,i):
        self.heaplist.append(i)
        self.size+=1
        self.percup(self.size)
    def percdown(self,i):
        while (i*2)<=self.size:
            mc=self.minchild(i)
            if self.heaplist[i]>self.heaplist[mc]:
                self.heaplist[i],self.heaplist[mc]=self.heaplist[mc],self.heaplist[i]
            i=mc
    def minchild(self,i):
        if (i*2+1)>self.size:
            return i*2
        else:
            if self.heaplist[i*2]<self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1
    def delmin(self):
        m=self.heaplist[1]
        self.heaplist[1]=self.heaplist[self.size]
        self.size-=1
        self.heaplist.pop()
        self.percdown(1)
        return m
    def buildheap(self,alist):
        i=len(alist)//2
        self.size=len(alist)
        self.heaplist=0+alist[:]
        while i>0:
            self.percdown(i)
            i-=1

n=int(input())
h=xiaoheap()
for _ in range(n):
    s=input()
    if s[0]=='1':
        s=s.split()
        a=int(s[1])
        h.insert(a)
    else:
        print(h.delmin())
```



# graph

## 最小生成树：

### kruskal（优先）：

greedy+disjointset

1.把所有的边按照权值sort，从权值小的开始考虑
2.如果当前边的两个节点不在一个集合：选择这个边
3.如果在一个集合：不选

### *prim

1.解锁的点的集合叫set，解锁的边的集合叫heap。set&heap为空。
2.从任意点开始，开始点加到set，开始点的所有边加入到heap
3.从heap弹出权值最小的边e，查看边e去往的点x：
	如果x in set，e舍弃
	如果不在，e属于最小生成树，x加入set

**优化**

1.小根堆放（到达节点的花费，节点）
2.弹出（花费y，节点u），y累加到总权重上，然后考察u的每一条边，去往v，权重w：
	v已经弹出过了，continue
	v不在heap里，heap里加入（w，v）
	v在heap里，记录为（x，v）
		如果w<x，记录更新成（w，v），然后调整堆
		w>=x ，continue

时间复杂度：O（（n+m）log n）



## DFS：

由于DFS的特性，path可以不参与变量的传递，这样只用一个全局变量path修改就行了，找到了可能的答案就copy到ans（字符串可以用两个变量，copy的时候就不会出事）。

给一个子集的模板吧

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        path=[]
        def s(nums,i,ans):
            nonlocal path
            if i==len(nums):
                ans.append(path[:])
                return
            path.append(nums[i])
            s(nums,i+1,ans)
            path.pop()
            s(nums,i+1,ans)
            return ans
        ans=s(nums,0,[])
        return ans
```

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        queens=[0]*n
        col=[False]*n
        diag1=[False]*(2*n-1)
        diag2=[False]*(2*n-1)
        def dfs(r:int):
            if r==n:
                ans.append(['.'*c+'Q'+'.'*(n-1-c) for c in queens])
                return
            for c, ok in enumerate(col):
                if not ok and not diag1[r+c] and not diag2[r-c]:
                    queens[r]=c
                    col[c]=diag1[r+c]=diag2[r-c]=True
                    dfs(r+1)
                    col[c]=diag1[r+c]=diag2[r-c]=False
        dfs(0)
        return ans
    
```



### *Warnsdorff：

接下来访问的点的能访问数是最少的（回忆骑士周游的degree优化）

```python
def degree(x,y,board):
    global n,di
    cnt=0
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny]==-1:
            cnt+=1
    return cnt
def dfs(x,y,cnt):
    global di,board,n
    if cnt==n*n:
        return True
    next_move=[]
    for dx,dy in di:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny]==-1:
            next_move.append((degree(nx,ny,board),nx,ny))
    next_move.sort()
    for _,nx,ny in next_move:
        board[nx][ny]=cnt
        if dfs(nx,ny,cnt+1):
            return True
        board[nx][ny]=-1
    return False
```



## BFS类

### BFS：

​	BFS通常用来处理最短路问题（连通分支、走迷宫等问题一般用DFS解决；对于最短路问题，由于用DFS可能需要遍历所有可能路径，BFS的时间复杂度常常会小得多）

#### 基本内容：

​	**特征**：任意两个节点之间的相互距离相同（无向图）

​	**形式**：可以是单点弹出或者整层弹出

​	进入队列的节点需要标记状态，防止同一个节点多次进入队列

​	**剪枝策略**

tip：

​	queue中的元素：不一定只是坐标对，有时间参量的时候要考虑加上时间的三元元组
​	BFS的劣势在于求路径问题时容易MLE，回忆词梯，可以先BFS求得有无路径（同时建图），再用DFS搜图	
​	小游戏：以拐弯此处作为BFS下一层的条件
​	变换的迷宫：重复一个周期啥也没干的就可以删了（需要额外的一个列表去判断上一个周期的状态）

visited类型：

​	1.set（）
​	2.[[0]*n for _ in range(m)]

一个有趣的directions：

```python
move=[-1,0,1,0,-1]
for i in range(4):
	dx,dy=move[i],move[i+1]
```

### 拓扑排序：（判断环）

degree表示入度，入度为0了再加入queue（或heap，一般用于字典序最小）

### 三色标记法（判断环）：

#### 核心思路

如果在递归过程中，发现下一个节点在递归栈中（正在访问中），则找到了环。

#### 具体思路

对于每个节点 *x*，都定义三种颜色值（状态值）：

0：节点 *x* 尚未被访问到。
1：节点 *x* 正在访问中，*dfs*(*x*) 尚未结束。
2：节点 *x* 已经完全访问完毕，*dfs*(*x*) 已返回。

⚠**误区**：不能只用两种状态表示节点「没有访问过」和「访问过」。例如上图，我们先 *dfs*(0)，再 *dfs*(1)，此时 1 的邻居 0 已经访问过，但这并不能表示此时就找到了环。

算法流程：

1. 建图：把每个 *prerequisites*[*i*]=[*a*,*b*] 看成一条有向边 *b*→*a*，构建一个有向图 *g*。

2. 创建长为 *numCourses* 的颜色数组 *colors*，所有元素值初始化成 0。

3. 遍历 *colors*，如果 *colors*[*i*]=0，则调用递归函数 *dfs*(*i*)。

4. 执行*dfs*(*x*)：

   1. 首先标记 *colors*[*x*]=1，表示节点 *x* 正在访问中。
   2. 然后遍历 *x* 的邻居 *y*。如果 *colors*[*y*]=1，则找到环，返回 true。如果 *colors*[*y*]=0（没有访问过）且 *dfs*(*y*) 返回了 true，那么 *dfs*(*x*) 也返回 true。
   3. 如果没有找到环，那么先标记 *colors*[*x*]=2，表示 *x* 已经完全访问完毕，然后返回 false。

5. 如果 *dfs*(*i*) 返回 true，那么找到了环，返回 false。

6. 如果遍历完所有节点也没有找到环，返回 true。

   ```python
   class Solution:
       def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
           g = [[] for _ in range(numCourses)]
           for a, b in prerequisites:
               g[b].append(a)
   
           colors = [0] * numCourses
           # 返回 True 表示找到了环
           def dfs(x: int) -> bool:
               colors[x] = 1  # x 正在访问中
               for y in g[x]:
                   if colors[y] == 1 or colors[y] == 0 and dfs(y):
                       return True  # 找到了环
               colors[x] = 2  # x 完全访问完毕
               return False  # 没有找到环
   
           for i, c in enumerate(colors):
               if c == 0 and dfs(i):
                   return False  # 有环
           return True  # 没有环
   ```



<mark>无向图的loop用dfs或者并查集（考察边）来判断</mark>

### *双向广搜

用途1：小优化
BFS的剪枝策略，分两侧展开分支，**哪侧数量少就从哪侧展开**

用途2：解决特征明显的一类问题
特征：**全量样本不允许递归完全展开，但是半量样本可以完全展开**
过程：把数据分成两部分，每部分**各自展开**计算结果，然后设计两部分结果的**整合逻辑**

### 01-BFS

其实就是用双端队列模拟Dijkstra的简单情况

过程：
1.distance[i]表示从源点到i点的最短距离，初始时所有点的distance设置为无穷大
2.源点进入双端队列，distance[源点]=0
3.双端队列 **头部弹出** x：
	A 如果x是目标点，返回distance[x]表示源点到目标点的最短距离
	B 考察从x出发的每一条边，假设某边去往y点，边权是w
		1）如果distance[y]>distance[x]+w，处理该边；否则忽略该边
		2）处理时，更新distance[y]=distance[x]+w
			如果w==0，y从头部进入双端队列。
			如果w==1，y从尾部进入双端队列

### **Dijkstra**

<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250514135516152.png" alt="image-20250514135516152" style="zoom:5%;" />

过程：
1.distance[i]表示从源点到i点的最短距离，visited[i]表示i节点是否从小根堆弹出过
2.准备好小根堆，小根堆存放记录：（源点到x的距离，x点），小根堆根据距离组织
3.令distance[源点]=0,（0，源点）放入小根堆
4.从小根堆弹出（源点到u的距离，u点）
	a.如果visited[u]==true，不做处理
	b.如果visited[u]==false. visited[u]=true
		然后考察u的每一条边，去往v，边权为w
		如果visited[v]==false and distance[u]+w<distance[v]，令distance[v]=distance[u]+w把（distance[u]+w,v)加入小根堆

```python
distance=[float('inf')]*n
distance[s]=0
visied=[False]*n
q=[]
heapq.heappush((0,s))
while q:
    u=heappop(q)
    if visited[u]:
        continue
    visited[u]=True
    for v,w in e[u]:
		if visited[v] and distance[u]+w<distance[v]:
            diatance[v]=distance[u]+w
            heapq.heappush(q,(distance[u]+w,v))
```

tips:

​	最后一次月考道路一题，最短路是一方面，能不能走是另一方面，所以不能只是单纯的Dijkstra，起码不能有visited的逻辑。（可以理解为钱数就充当了能否visited的条件了）	

​	剪枝，弹出来判断一下是不是终点，避免MLE

### 分层最短路（根据状态扩展点）

不把实际位置看作点，而是把 **实际位置及其状态的组合** 看作是点，然后搜索BFS或者Dijkstra的过程不变，只是扩了点而已、

原理简单，但是**如何扩点，如何到达，如何算距离**，每个题不一样

### *A星:

在Dijkstra的基础上增加了预估函数，并且让堆以**从源点出发到当前点的距离+当前点到终点的预估距离**进行排序

预估函数**要求**：当前点到终点的预估距离<=当前点到终点的真实最短距离

预估函数是一种吸引力
	1）合适的吸引力可以提升算法的速度
	2）吸引力过强会出现错误

预估函数常选：
	曼哈顿距离、欧式距离、对角线距离

**常数时间大大优化**！

## Floyd:（求任意两点之间的最短距离）

用**邻接矩阵**储存图

适用于任何图（不能有负环）

```python
for bridge in range(n):
    for i in range(n):
        for j in range(n):
            if distance[i][bridge]!=float('inf') and distance[bridge][j]!=float('inf') and distance[i][j] > distance[i][bridge]+distance[bridge][j]:
                distance[i][j]=distance[i][bridge]+distance[bridge][j]         
```



## Bellman-Ford：（有源点的最短路）

tips：

​	飞机k次中转呢个题，用了一个next拷贝cur，使得中转次数和松弛次数对应上了
​	货币兑换呢个题，不要纠结于d[x]是否比之前大了（因为可能要循环很多次才会大一点点），只要能判断出正环，就一定会大！

解决可以有负权但是不能有负环（保证最短路存在）的图，单源最短路

**松弛操作**：

​	假设源点为A，从A到任意点F的最短距离为distance[F]
​	假设从点P出发某条边，去往点S，边权为W
​	如果发现，distance[P] + W<distance[S]，也就是通过该边可以让distance[S]变小

那么就说P出发的这条边对点S进行了松弛操作

Bellman-Ford过程：

​	1.每一轮考察每条边，每条边都尝试进行松弛操作，那么诺干点的distance会变小
​	2.当某一轮发现不再有松弛操作出现时，停止

**时间复杂度**：

点N，边M，每一轮时间复杂度O（M）
最短路存在的情况下，因为1次松弛操作会使1个点的最短路的变数+1
而从源点出发到任何点的最短路最多走过全部的n个点，所以松弛的轮数必然<=n-1
所以Bellman-Ford算法时间复杂度O（MN）

**重要推广：判断从某个点出发能不能到达负环**
如果从A出发存在最短路（没有负环），那么松弛的论述必然<=n-1
而如果从A点出发到达一个负环，那么松弛操作显然会无休无止地进行下去
所以，如果发现从A点出发，在第n轮时松弛操作依然存在，说明从A点出发能够到达一个负环

### *SPFA优化：

每一轮考察所有的边看看能否做松弛操作时不必要的
因为只有上一次被某条边松弛过的节点所连接的边，才有可能引起下一次的松弛操作
所以用队列来维护”这一轮哪些节点的distance变小了“
下一轮只需要对这些点的所有边，考察有没有松弛操作即可

只优化了常数时间复杂度O（MN）只适用于小图，没有负权边优先Dijkstra

**用途**：
1.适用于小图
2.解决有负边（无负环）的图的单源最短路径问题
3.可以判断从某个点出发是否能遇到负环，**如果想判断整张图有向图有没有负环，需要设置虚拟源点**
4.并行计算时会有很大优势，因为每一轮多点判断松弛操作是相互独立的，可以交给多线程处理

虚拟源点：到图中所有点的距离都是0



<img src="C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20250517214902881.png" alt="image-20250517214902881" style="zoom: 5%;" />

## *Kosaraju（强连通）

这个也没有做题，感觉也不太会考，就直接把课件模板贴过来了。

Kosaraju算法是一种用于在有向图中寻找强连通分量（Strongly Connected Components，SCC）的算法。它基于深度优先搜索（DFS）和图的转置操作。

Kosaraju算法的核心思想就是两次深度优先搜索（DFS）。

1. **第一次DFS**：在第一次DFS中，我们对图进行标准的深度优先搜索，但是在此过程中，我们记录下顶点完成搜索的顺序。这一步的目的是为了找出每个顶点的完成时间（即结束时间）。

2. **反向图**：接下来，我们对原图取反，即将所有的边方向反转，得到反向图。

3. **第二次DFS**：在第二次DFS中，我们按照第一步中记录的顶点完成时间的逆序，对反向图进行DFS。这样，我们将找出反向图中的强连通分量。

Kosaraju算法的关键在于第二次DFS的顺序，它保证了在DFS的过程中，我们能够优先访问到整个图中的强连通分量。因此，Kosaraju算法的时间复杂度为O(V + E)，其中V是顶点数，E是边数。

以下是Kosaraju算法的Python实现，<mark>使用stack模拟按照结束时间的递减顺序访问顶点</mark>。

```python
def dfs1(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(graph, neighbor, visited, stack)
    stack.append(node)

def dfs2(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(graph, neighbor, visited, component)

def kosaraju(graph):
    # Step 1: Perform first DFS to get finishing times
    stack = []
    visited = [False] * len(graph)
    for node in range(len(graph)):
        if not visited[node]:
            dfs1(graph, node, visited, stack)
    
    # Step 2: Transpose the graph
    transposed_graph = [[] for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)
    
    # Step 3: Perform second DFS on the transposed graph to find SCCs
    visited = [False] * len(graph)
    sccs = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs2(transposed_graph, node, visited, scc)
            sccs.append(scc)
    return sccs

# Example
graph = [[1], [2, 4], [3, 5], [0, 6], [5], [4], [7], [5, 6]]
sccs = kosaraju(graph)
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
```



