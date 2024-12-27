## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/（十分钟以内）

思路：

先转换成ascii码，然后往前减，如果超范围了就+26

代码

```python
#print(ord('a'))
num=int(input())
s=str(input())
num%=26
for i in range(len(s)):
    s1=chr(ord(s[i])-num)
    if ord(s[i])<=90 and ord(s1)<65:
        s1=chr(ord(s1)+26)
    if ord(s[i]) >=97 and ord(s1) < 97:
        s1 = chr(ord(s1) +26)
    print(s1,end='')
```



代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012094008553](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241012094008553.png)

### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/（小于10分钟）

思路：

只读取每段的前两位数，用eval读取并相加

代码

```python
s=input().split()
a=eval(s[0][0]+s[0][1])
b=eval(s[1][0]+s[1][1])
print(a+b)
```

代码运行截图 ==（至少包含有"Accepted"）==

![image-20241012094328925](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241012094328925.png)

### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/（10min左右）

思路：

拉一个表（X感觉比较特殊，就随便赋值555），现在看来其实可以用字典的

代码

```python
num=int(input())
b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
a=[1,0,555,9,8,7,6,5,4,3,2]
for i in range(num):
    s=input()
    check=0
    for j in range(17):
        check+=b[j]*eval(s[j])
    check%=11
    answer=a[check]
    #print(type(answer))
    if answer==555:
        if s[17]=='X':
            print('YES')
        else:
            print('NO')
        continue
    if answer==eval(s[17]):
        print('YES')
    else:
        print('NO')	
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012094456237](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241012094456237.png)

### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/（10分钟左右）

思路：

不断迭代

代码

```python
def ha(a):
    if a%2==0:
        print(a,'/2=',int(a/2),sep='')
        a=int(a/2)
    else:
        print(a,'*3+1=',a*3+1,sep='')
        a=a*3+1
    return(a)
num=int(input())
while num!=1:
    num=ha(num)
print('End')
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012094606929](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241012094606929.png)

### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/（50min）

思路：数字转字母好转，但是字母转数字我不太会，于是我只写了数字转字母，对于字母转数字的情况，我用一个函数从一开始转成字母，如果字母不相等就+1，直到相等为止，最后输出这个数字。

##### 代码

```python
# 
s=input()
d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
def o(s):
    an=''
    if s // 1000 >= 1:
        for i in range(s // 1000):
            an+='M'
    if s // 100 >= 1:
        bai = (s % 1000) // 100
        if bai == 1:
            an+='C'
        elif bai == 2:
            an+='CC'
        elif bai == 3:
            an+='CCC'
        elif bai == 4:
            an+='CD'
        elif bai == 5:
            an+='D'
        elif bai == 6:
            an+='DC'
        elif bai == 7:
            an+='DCC'
        elif bai == 8:
            an+='DCCC'
        elif bai == 9:
            an+='CM'
    if s // 10 >= 1:
        shi = (s % 100) // 10
        if shi == 1:
            an+='X'
        elif shi == 2:
            an+='XX'
        elif shi == 3:
            an+='XXX'
        elif shi == 4:
            an+='XL'
        elif shi == 5:
            an+='L'
        elif shi == 6:
            an+='LX'
        elif shi == 7:
            an+='LXX'
        elif shi == 8:
            an+='LXXX'
        elif shi == 9:
            an+='XC'
    if s // 1 >= 0:
        ge = s % 10
        if ge == 1:
            an+='I'
        elif ge == 2:
            an+='II'
        elif ge == 3:
            an+='III'
        elif ge == 4:
            an+='IV'
        elif ge == 5:
            an+='V'
        elif ge == 6:
            an+='VI'
        elif ge == 7:
            an+='VII'
        elif ge == 8:
            an+='VIII'
        elif ge == 9:
            an+='IX'
    return(an)
if '0'<=s[0]<='9':
    s=int(s)
    if s//1000>=1:
        for i in range(s//1000):
            print('M',end='')
    if s//100>=1:
        bai=(s%1000)//100
        if bai==1:
            print('C',end='')
        elif bai==2:
            print('CC',end='')
        elif bai==3:
            print('CCC',end='')
        elif bai==4:
            print('CD',end='')
        elif bai==5:
            print('D',end='')
        elif bai==6:
            print('DC',end='')
        elif bai==7:
            print('DCC',end='')
        elif bai==8:
            print('DCCC',end='')
        elif bai==9:
            print('CM',end='')
    if s//10>=1:
        shi =(s%100)// 10
        if shi == 1:
            print('X', end='')
        elif shi == 2:
            print('XX', end='')
        elif shi == 3:
            print('XXX', end='')
        elif shi == 4:
            print('XL', end='')
        elif shi == 5:
            print('L', end='')
        elif shi == 6:
            print('LX', end='')
        elif shi == 7:
            print('LXX', end='')
        elif shi == 8:
            print('LXXX', end='')
        elif shi == 9:
            print('XC', end='')
    if s//1>=0:
        ge =s%10
        if ge == 1:
            print('I', end='')
        elif ge == 2:
            print('II', end='')
        elif ge == 3:
            print('III', end='')
        elif ge == 4:
            print('IV', end='')
        elif ge == 5:
            print('V', end='')
        elif ge == 6:
            print('VI', end='')
        elif ge == 7:
            print('VII', end='')
        elif ge == 8:
            print('VIII', end='')
        elif ge == 9:
            print('IX', end='')
else:
    j=1
    while o(j)!=s:
        j+=1
    print(j)
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![image-20241012095306570](C:\Users\31983\AppData\Roaming\Typora\typora-user-images\image-20241012095306570.png)

### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/

很想做出来这个题，但下来试了快三个小时，真不是很会做这个题

## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

第一题：对ascii码还不是很熟悉，不过考试的时候先让程序print了一下azAZ的值。

前四道题一共花了不到40min，感觉对于新手来说是比较满意的，然后开始卡在第五题，第五题有个重大失误，就是当时比较心急，没有完全想懂就开始写，导致前三次写的代码逻辑上就不通顺，但好在花了40多min后我发现了，并想了一会还是没思路后，开始人工枚举（我知道这不是一个好方法，但在考试的时候确实是很管用的），最后10min左右就把枚举代码写完了（并很后悔之前的轻举妄动）。

至于最后一题，感觉起飞了，我还没思路，试过几次没啥思路，主要可能是因为还没学过算法，希望老师上课能讲讲这个题思路。

每日选做也在尽量跟进，前几天做出了几道1300的题，很有成就感，感觉这样下去下个月可以顺利做出medium的题，下一个目标是向tough进军
