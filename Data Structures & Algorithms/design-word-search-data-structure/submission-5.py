class TrieNode:
    def __init__(self) -> None:
        self.neighboors={}
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.dict_ = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.dict_
        for ch in word:
            if ch not in cur.neighboors:
                cur.neighboors[ch] = TrieNode()
            cur = cur.neighboors[ch]
        cur.isWord = True

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            if i == len(word):
                return cur.isWord
            ch = word[i]
            if ch == '.':
                for nei in cur.neighboors:
                    if dfs(i+1, cur.neighboors[nei]):
                        return True
            else:
                if ch in cur.neighboors:
                    return dfs(i+1, cur.neighboors[ch])
            return False
        return dfs(0, self.dict_)