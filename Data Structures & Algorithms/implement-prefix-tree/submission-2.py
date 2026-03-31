class Node:
    def __init__(self) -> None:
        self.child = {}
        self.isWord = False
class PrefixTree:

    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        cur = self.node
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.node
        for w in word:
            if w not in cur.child:
                cur.child[w] = Node()
            cur = cur.child[w]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for w in prefix:
            if w not in cur.child:
                return False
            cur = cur.child[w]
        return True
        