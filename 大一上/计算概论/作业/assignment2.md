# 1.题目

## 263A.Beautiful Matrix（16分钟）

### 思路：记录1的行数和列数，并与3减取绝对值再相加

### 代码：![image-20240928154149531](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928154149531.png)

![image-20240928171159153](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928171159153.png)

## 1328A.Divisibility Problem（10分钟）

### 思路：用数学b-a%b，并注意整除的情况

### 代码：

```
num=int(input())
shuchu=[]
for i in range(0,num):
    shuru=input().split()
    a=int(shuru[0])
    b=int(shuru[1])
    answer=(b-(a%b))
    if answer==b:
        answer=0
    shuchu.append(answer)
for i in range(0,num):
    print(shuchu[i])
```

![image-20240928171205281](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928171205281.png)

## 427A.Police Recruits(13分钟)

### 思路：保存剩余警察的数量并与逐个犯罪数量相比较

### 代码：

```
num=int(input())
shuru=input().split()
shu=answer=0
for i in range(num):
    if int(shuru[i])<0:
        if shu<(-int(shuru[i])):
            answer+=1
        else:
            shu-=1
    else:
        shu+=int(shuru[i])
print(answer)
```

## ![image-20240928171210570](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928171210570.png)02808.校门外的树（很长时间)

### 思路：用一个列表，有树为1，没树为0，最后求1的个数

### 代码：![image-20240928180932619](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928180932619.png)

## sy60：水仙花数II（15分钟）

### 思路：循环判断

### 代码：

```
def shuixianhua(a):
    bai=a//100
    ge=a%10
    shi=(a%100)//10
    if a==ge**3+shi**3+bai**3:
        return True
    else:
        return False
shuru=input().split()
a=int(shuru[0])
b=int(shuru[1])
answer=[]
for i in range(a,b+1):
    if shuixianhua(i):
        answer.append(i)
if len(answer)!=0:
    for i in range(len(answer)):
        print(answer[i],end='')
        if i!=len(answer)-1:
            print(' ',end='')
else:
    print('NO')
```

![image-20240928171041472](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928171041472.png)

## 01922:Ride to School（很长时间）

### 思路：先删除出发时间为负数。在进行到达时间的逐一比较

### 代码：![image-20240928212927134](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240928212927134.png)

# 2.学习总结与收获

通过本次作业的六道题（尤其是标注很长时间的两道题）我的收获很多，譬如：我理解了runtime error是程序结构有问题（我一直以为是超时，所以一直在优化算法，浪费时间）以及审题的重要（校门外的树呢一道题，列表的长度应该是l+1而不是l，虽然题目中明确说了，但我这次做题的时候还是先入为主了，导致一直re）以及清空列表的重要性（最后一道题没有清空列表花了好长时间），最近（截至今日9月28日）刚学完一点基本的语法，一直在慢慢刷每日选做，已经完成了6道，后续十一我会多花点时间慢慢赶上来的。