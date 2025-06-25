class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next
class LinkList:  #循环链表
    def __init__(self):
        self.tail = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def pushFront(self,data):
        nd = Node(data)
        if self.tail == None:
            self.tail = nd
            nd.next = self.tail
        else:
            nd.next = self.tail.next
            self.tail.next = nd
        self.size += 1
    def pushBack(self,data):
        self.pushFront(data)
        self.tail = self.tail.next
    def popFront(self):
        if self.size == 0:
            return None
        else:
            nd = self.tail.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            else:
                self.tail.next = nd.next
        return nd.data
    def printList(self):
        if self.size > 0:
            ptr = self.tail.next
            while True:
                print(ptr.data,end = " ")
                if ptr == self.tail:
                    break
                ptr = ptr.next
            print("")

    def remove(self,data):
        n=self.size
        if n==0:
            return '0'
        t=self.tail
        for i in range(n):
            if t.next.data==data:
                if i!=n-1:
                    t.next=t.next.next
                else:
                    t.next=self.tail.next
                    self.tail=t
                self.size -= 1
                return True
            t=t.next
        return False
t = int(input())
for i in range(t):
    lst = list(map(int,input().split()))
    lkList = LinkList()
    for x in lst:
        lkList.pushBack(x)
    lst = list(map(int,input().split()))
    for a in lst:
        result = lkList.remove(a)
        if result == True:
            lkList.printList()
        elif result == False:
            print("NOT FOUND")
        else:
            print("EMPTY")
    print("----------------")