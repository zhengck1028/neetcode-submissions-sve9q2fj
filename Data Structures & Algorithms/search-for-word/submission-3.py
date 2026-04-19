class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = set()
        d = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(r,c,i):
            if i == len(word):
                return True
            if min(r,c)<0 or r == rows or c == cols or (r,c) in visit or board[r][c] != word[i]:
                return False
            visit.add((r,c))
            for dr, dc in d:
                newR, newC = r + dr, c + dc
                if dfs(newR, newC, i + 1):
                    return True
            visit.remove((r,c))
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False