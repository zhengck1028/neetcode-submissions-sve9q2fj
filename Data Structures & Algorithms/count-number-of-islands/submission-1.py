class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # return when out of bounds or reach "0" 
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == "0": 
                return
            grid[r][c] = "0"
            for dr, dc, in d:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    res += 1
        return res