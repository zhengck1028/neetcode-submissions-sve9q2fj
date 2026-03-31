class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        def dfs(r, c):
            if min(r,c)<0 or r >= rows or c >= cols or grid[r][c] ==0:
                return 0
            grid[r][c] = 0
            A = 1
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                A += dfs(row, col)
            return A

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(dfs(r, c), res)
        
        return res