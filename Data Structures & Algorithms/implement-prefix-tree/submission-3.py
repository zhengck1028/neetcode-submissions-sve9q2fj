class TrieNode:
    def __init__(self) -> None:
        self.neighboors={}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.dict_ = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.dict_
        for ch in word:
            if ch not in cur.neighboors:
                cur.neighboors[ch] = TrieNode()
            cur = cur.neighboors[ch]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.dict_
        for ch in word:
            if ch not in cur.neighboors:
                return False
            cur = cur.neighboors[ch]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.dict_
        for ch in prefix:
            if ch not in cur.neighboors:
                return False
            cur = cur.neighboors[ch]
        return True
        