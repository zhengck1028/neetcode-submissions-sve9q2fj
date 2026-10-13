class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r == rows or c == cols or r < 0 or c < 0 or (r,c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r,c))
            for dr, dc in d:
                nr = r+ dr
                nc = c + dc
                if dfs(i + 1, nr, nc):
                    return True
            visited.remove((r,c))
            return False
        for r in range(rows):
            for c in range(cols):
                if dfs(0, r, c):
                     return True
        return False