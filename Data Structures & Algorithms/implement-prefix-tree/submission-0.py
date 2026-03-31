class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.isword = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.child:
                cur.child[i] = TrieNode()
            cur = cur.child[i]
        cur.isword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        return cur.isword

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        return True
        