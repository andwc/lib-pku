# 599ms
# from bisect import bisect_left
# t=int(input())
# for _ in range(t):
#     m,n=map(int,input().split())
#     p = []
#     p= sorted(list(map(int, input().split())))
#     np=[]
#     for i in range(m-1):
#         shuru=sorted(list(map(int,input().split())))
#         for j in range(n):
#             np.append(shuru[0]+p[j])
#         judge=np[-1]
#         #print(np,p)
#         for j in range(1,n):
#             for k in range(n):
#                 cur=p[k]+shuru[j]
#                 if cur>=judge:
#                     break
#                 else:
#                     np.pop()
#                     np.insert(bisect_left(np,cur),cur)
#                     judge=np[-1]
#         p=np[:]
#         np=[]
#         #print(p,np)
#     print(' '.join(map(str,p)))
#
# np,p轮换着用会不会更快？
# 居然640ms
from bisect import bisect_left
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    p = [[],[]]
    p[0]= sorted(list(map(int, input().split())))
    for i in range(1,m):
        shuru=sorted(list(map(int,input().split())))
        a=i%2
        b=a^1
        for j in range(n):
            p[a].append(shuru[0]+p[b][j])
        judge=p[a][-1]
        for j in range(1,n):
            for k in range(n):
                cur=p[b][k]+shuru[j]
                if cur>=judge:
                    break
                else:
                    p[a].pop()
                    p[a].insert(bisect_left(p[a],cur),cur)
                    judge=p[a][-1]
        p[b]=[]
    print(' '.join(map(str,p[(m+1)%2])))

#用heap会不会快一点
#
# import heapq
# t=int(input())
# for _ in range(t):
#     m,n=map(int,input().split())
#     p = []
#     heapq.heapify(p)
#     np=[]
#     heapq.heapify(np)
#
#     shuru = list(map(int, input().split()))
#     for j in range(n):
#         heapq.heappush(np,-shuru[j])
#
#     for i in range(m-1):
#         shuru=sorted(list(map(int,input().split())))
#         for j in range(n):
#             heapq.heappush(np,-p[j]-shuru[0])
#         judge=-np[0]
#         for j in range(1,n):
#             for k in range(n):
#                 cur=p[k]+shuru[j]
#                 if cur>=judge:
#                     break
#                 else:
#                     p[i%2].pop()
#                     p[i%2].insert(bisect_left(p[i%2],cur),cur)
#                     judge=p[i%2][-1]
#         p[(i+1)%2].clear()
#     print(' '.join(map(str,p[(m+1)%2])))