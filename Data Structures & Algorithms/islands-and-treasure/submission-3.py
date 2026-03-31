class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647
        def bfs(r, c):
            q = deque([(r,c)])
            visit = set()
            visit.add((r,c))
            layer = 0
            while q:
                for i in range(len(q)):
                    x, y = q.popleft()
                    if grid[x][y] == 0:
                        return layer
                    for dx, dy in directions:
                        nx = x+dx
                        ny = y+dy
                        if 0<=nx<ROWS and 0<=ny<COLS and (nx, ny) not in visit and grid[nx][ny] != -1:
                            q.append((nx, ny))
                            visit.add((nx, ny))
                layer += 1
            return INF
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)
            