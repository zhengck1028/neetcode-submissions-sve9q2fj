class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        res = 0
        rows, cols = len(grid),len(grid[0])

        def dfs(r,c):
            if r == rows or c == cols or r <0 or c <0 or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            a = 1
            for dr, dc in d:
                a += dfs(r+dr, c+dc)
            return a

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    a = dfs(r,c)
                    res = max(res, a)
        return res