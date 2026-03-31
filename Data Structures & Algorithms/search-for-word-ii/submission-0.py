class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tries = TrieNode()
        for w in words:
            cur = tries
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True
        ress = set()
        curSet = []
        path = set()
        cur = tries
        def dfs(r, c, cur):
            if (r < 0 or c < 0 or
                r >= len(board) or
                c >= len(board[0]) or
                (r, c) in path or
                board[r][c] not in cur.children):
                return
            
            path.add((r,c))
            curSet.append(board[r][c])
            next_node = cur.children[board[r][c]]
            if next_node.isEnd:
                ress.add("".join(curSet))
            dfs(r, c+1, next_node)
            dfs(r, c-1, next_node)
            dfs(r+1, c, next_node)
            dfs(r-1, c, next_node)

            curSet.pop()
            path.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, tries)
        return list(ress)

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False