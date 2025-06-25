from bisect import bisect_left
a, b, now = [], [], 0
for _ in range(int(input())):
    opt = input().split()
    if opt[0] == 'query':
        l = len(a)
        if l & 1: print(a[l >> 1])
        else:
            ans = (a[l >> 1] + a[l - 1 >> 1]) / 2
            print(ans if int(ans) != ans else int(ans))
    if opt[0] == 'add':
        v = int(opt[1])
        a.insert(bisect_left(a, v), v)
        b.append(v)
    if opt[0] == 'del':
        v = b[now]
        now += 1
        a.pop(bisect_left(a, v))
#------------------------------------------------------------------------
# import collections
# import heapq
#
#
# class DualHeap:
#     def __init__(self):
#         # 大根堆，维护较小的一半元素，注意 python 没有大根堆，需要将所有元素取相反数并使用小根堆
#         self.small = list()
#         # 小根堆，维护较大的一半元素
#         self.large = list()
#         # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
#         self.delayed = collections.Counter()
#
#         # small 和 large 当前包含的元素个数，需要扣除被「延迟删除」的元素
#         self.smallSize = 0
#         self.largeSize = 0
#
#     # 不断地弹出 heap 的堆顶元素，并且更新哈希表
#     def prune(self, heap):
#         while heap:
#             num = heap[0]
#             if heap is self.small:
#                 num = -num
#             if num in self.delayed:
#                 self.delayed[num] -= 1
#                 if self.delayed[num] == 0:
#                     self.delayed.pop(num)
#                 heapq.heappop(heap)
#             else:
#                 break
#
#     # 调整 small 和 large 中的元素个数，使得二者的元素个数满足要求
#     def make_balance(self):
#         if self.smallSize > self.largeSize + 1:
#             # small 比 large 元素多 2 个
#             heapq.heappush(self.large, -self.small[0])
#             heapq.heappop(self.small)
#             self.smallSize -= 1
#             self.largeSize += 1
#             # small 堆顶元素被移除，需要进行 prune
#             self.prune(self.small)
#         elif self.smallSize < self.largeSize:
#             # large 比 small 元素多 1 个
#             heapq.heappush(self.small, -self.large[0])
#             heapq.heappop(self.large)
#             self.smallSize += 1
#             self.largeSize -= 1
#             # large 堆顶元素被移除，需要进行 prune
#             self.prune(self.large)
#
#     def insert(self, num):
#         if not self.small or num <= -self.small[0]:
#             heapq.heappush(self.small, -num)
#             self.smallSize += 1
#         else:
#             heapq.heappush(self.large, num)
#             self.largeSize += 1
#         self.make_balance()
#
#     def erase(self, num):
#         self.delayed[num] += 1
#         if num <= -self.small[0]:
#             self.smallSize -= 1
#             if num == -self.small[0]:
#                 self.prune(self.small)
#         else:
#             self.largeSize -= 1
#             if num == self.large[0]:
#                 self.prune(self.large)
#         self.make_balance()
#
#     def get_median(self):
#         return -self.small[0] if self.smallSize != self.largeSize else (-self.small[0] + self.large[0]) / 2
#
#
# n = int(input())
# q = DualHeap()
# l = []
# start_idx = 0
# for _ in range(n):
#     operation = input()
#     if operation == 'query':
#         ans = q.get_median()
#         if round(ans) == ans:
#             print(int(ans))
#         else:
#             print(ans)
#     elif operation == 'del':
#         q.erase(l[start_idx])
#         start_idx += 1
#     else:
#         t = int(operation.split()[1])
#         q.insert(t)
#         l.append(t)
#--------------------------------------------------------------
# import heapq
# from collections import deque
# class quickmid:
#     def __init__(self):
#         self.xiao=[]
#         self.da=[]
#         self.lxiao=0
#         self.lda=0
#         self.mid=None
#         self.p=deque()
#     def add(self,num):
#         self.p.append(num)
#         if self.lxiao==0:
#             self.mid=num
#             heapq.heappush(self.xiao,-num)
#             self.lxiao+=1
#             return
#         if num>=self.mid:
#             heapq.heappush(self.da,num)
#             self.lda+=1
#         else:
#             heapq.heappush(self.xiao,-num)
#             self.lxiao+=1
#         #tiao zheng
#         if self.lxiao>self.lda+1:
#             heapq.heappush(self.da,-heapq.heappop(self.xiao))
#             self.lda+=1
#             self.lxiao-=1
#             self.mid=(self.da[0]-self.xiao[0])/2 if (self.da[0]-self.xiao[0])%2==1 else (self.da[0]-self.xiao[0])//2
#         elif self.lda==self.lxiao+1:
#             heapq.heappush(self.xiao,-heapq.heappop(self.da))
#             self.lda-=1
#             self.lxiao+=1
#             self.mid=-self.xiao[0]
#         elif self.lxiao==self.lda:
#             self.mid=(self.da[0]-self.xiao[0])/2 if (self.da[0]-self.xiao[0])%2==1 else (self.da[0]-self.xiao[0])//2
#         elif self.lxiao==self.lda+1:
#             self.mid=-self.xiao[0]
#         #print('addd',self.mid,self.xiao[0],self.da[0])
#     def delete(self):
#         target=self.p.popleft()
#         if target==self.mid:
#             heapq.heappop(self.xiao)
#             self.lxiao-=1
#         elif target>self.mid:
#             self.da.remove(target)
#             heapq.heapify(self.da)
#             if self.lxiao==self.lda+1:
#                 heapq.heappush(self.da,-heapq.heappop(self.xiao))
#                 self.lxiao-=1
#                 self.mid=(self.da[0]-self.xiao[0])/2 if (self.da[0]-self.xiao[0])%2==1 else (self.da[0]-self.xiao[0])//2
#             else:
#                 self.lda-=1
#                 self.mid=-self.xiao[0]
#         else:
#             self.xiao.remove(-target)
#             heapq.heapify(self.xiao)
#             self.lxiao-=1
#             if self.lxiao<self.lda:
#                 heapq.heappush(self.xiao,-heapq.heappop(self.da))
#                 self.lxiao+=1
#                 self.lda-=1
#                 self.mid=-self.xiao[0]
#             else:
#                 self.mid=(self.da[0]-self.xiao[0])/2 if (self.da[0]-self.xiao[0])%2==1 else (self.da[0]-self.xiao[0])//2
#         #print('del',self.mid)
#     def query(self):
#         return self.mid
# q=quickmid()
# n=int(input())
# for i in range(n):
#     s=input().split()
#     if s[0]=='add':
#         q.add(int(s[1]))
#     elif s[0]=='del':
#         q.delete()
#     else:
#         print(q.query())
#-----------------------------------------------
# qu=[]
# n=int(input())
# for i in range(n):
#     s=input().split()
#     if s[0]=='add':
#         qu.append(int(s[1]))
#     elif s[0]=='del':
#         qu.pop(0)
#     else:
#         q=sorted(qu)
#         l=len(q)
#         if l%2==1:
#             print(q[l//2])
#         else:
#             a=(q[l//2-1]+q[l//2])
#             if a%2==1:
#                 print(a/2)
#             else:
#                 print(a//2)