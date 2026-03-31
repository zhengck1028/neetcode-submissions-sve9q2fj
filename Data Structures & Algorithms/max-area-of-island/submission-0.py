class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
                return 0
            A = 1
            grid[r][c] = 0
            for dr, dc in directions:
                A += dfs(r+dr, c+dc)
            return A

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    A = dfs(r, c)
                    res = max(res, A)
        return res
        