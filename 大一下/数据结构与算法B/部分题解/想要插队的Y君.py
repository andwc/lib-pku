class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next
class LinkList:
    def __init__(self):
        self.head = None
    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def insertCat(self):
        m=Node(6)
        h=self.head
        n=0
        while h:
            n+=1
            h=h.next
        n=(n-1)//2
        h=self.head
        for i in range(n):
            h=h.next
        m.next=h.next
        h.next=m
    def printLk(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
        print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()