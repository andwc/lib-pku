class Trie:
    class TrieNode:
        def __init__(self):
            self.p=0
            self.e=0
            self.next=[None]*26

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