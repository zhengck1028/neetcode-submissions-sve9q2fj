class TrieNode:
    def __init__(self) -> None:
        self.child={}
        self.isword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isword = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c == '.':
                res = False
                for a in cur.child:
                    newword = word.replace('.', a, 1)
                    res = res or self.search(newword)
                return res
            if c not in cur.child:
                return False
            cur = cur.child[c]
        return cur.isword
