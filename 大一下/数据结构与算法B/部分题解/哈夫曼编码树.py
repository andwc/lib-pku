import heapq
class node:
    def __init__(self, char,freq):
        self.char = char
        self.left=None
        self.right=None
        self.freq=freq
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