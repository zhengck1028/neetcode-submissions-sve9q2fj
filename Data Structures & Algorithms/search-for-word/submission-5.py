class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r,c))
            res = False
            for dr, dc in d:
                row = r + dr
                col = c + dc
                res = res or dfs(row, col, i+1)
            visited.remove((r, c))
            return res
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
            