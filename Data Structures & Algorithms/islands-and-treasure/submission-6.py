class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        directions = [[-1,0], [0,-1],[1,0],[0,1]]
        visit = set()
        from collections import deque
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        level = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row >= 0 and col >=0 and row < rows and col < cols and (row,col) not in visit and grid[row][col] !=-1:
                        q.append((row, col))
                        visit.add((row, col))
            level += 1

