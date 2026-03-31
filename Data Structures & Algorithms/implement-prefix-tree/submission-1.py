class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.dic = Node()

    def insert(self, word: str) -> None:
        cur = self.dic
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = Node()
            cur = cur.children[word[i]]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.dic
        for i in range(len(word)):
            if word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.dic
        for i in range(len(prefix)):
            if prefix[i] not in cur.children:
                return False
            cur = cur.children[prefix[i]]
        return True
        
        