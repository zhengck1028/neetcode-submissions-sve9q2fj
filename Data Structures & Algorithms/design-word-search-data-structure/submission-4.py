class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.dic = Node()

    def addWord(self, word: str) -> None:
        cur = self.dic
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            cur = node
            for j in range(i, len(word)):
                if word[j] == ".":
                    for k in cur.children.values():
                        if dfs(k, j+1):
                            return True
                    return False
                elif word[j] not in cur.children:
                    return False
                else:
                    cur = cur.children[word[j]]
            return cur.is_word
        return dfs(self.dic, 0)
        

