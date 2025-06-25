from collections import defaultdict
class node:
    def __init__(self,key):
        self.key=key
        self.neighbor={}
class graph:
    def __init__(self):
        self.vertex={}
    def build(self,words):
        for word in words:
            self.vertex[word]=node(word)
        d=defaultdict(list)
        for word in words:
            for i in range(4):
                w=word[:i]+' '+word[i+1:]
                d[w].append(word)
        for i in d:
            n=len(d[i])
            for j in range(n-1):
                word1=d[i][j]
                for k in range(j+1,n):
                    word2=d[i][k]
                    self.vertex[word1].neighbor[word2]=self.vertex[word2]
                    self.vertex[word2].neighbor[word1]=self.vertex[word1]
        return
n=int(input())
words=[]
for i in range(n):
    words.append(input())
start,end=map(str,input().split())
g=graph()
g.build(words)
visited=set()
from collections import deque, defaultdict

q=deque()
q.append([g.vertex[start],[start]])
visited.add(start)
while q:
    for _ in range(len(q)):
        node,path=q.popleft()
        if node.key==end:
            print(' '.join(path))
            exit()
        for i in node.neighbor:
            if i not in visited:
                visited.add(i)
                q.append([node.neighbor[i],path+[i]])
print('NO')