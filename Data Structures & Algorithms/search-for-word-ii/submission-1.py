class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 构建字典树
        tries = TrieNode()
        for w in words:
            cur = tries  # 🐛 修复 1：每个新单词必须从根节点重新开始插！
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True
            
        ress = set() # 🐛 修复：用 set 避免同一个单词被不同路径找到多次
        path = set()
        curSet = []
        
        # 简化一下参数，不需要每次传 curSet
        def dfs(r, c, cur):
            # 🐛 修复 2 & 3：正确的越界检查，以及提取当前棋盘字符
            if (r < 0 or c < 0 or 
                r >= len(board) or c >= len(board[0]) or 
                (r, c) in path or 
                board[r][c] not in cur.children):
                return
            
            # 当前格子合法，获取对应的字母并进入下一层 Trie 节点
            char = board[r][c]
            next_node = cur.children[char]
            
            # 做选择
            path.add((r, c))
            curSet.append(char)
            
            # 🐛 修复 4 & 5：在走入新节点后检查 isEnd，并且绝对不 return！
            if next_node.isEnd:
                ress.add("".join(curSet))
                
            # 四个方向继续探索
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            
            # 撤销选择 (回溯)
            curSet.pop()
            path.remove((r, c))

        # 遍历棋盘的每一个点作为起点
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, tries)
                
        return list(ress)