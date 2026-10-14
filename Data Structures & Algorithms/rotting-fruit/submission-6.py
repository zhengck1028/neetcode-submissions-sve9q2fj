class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        rows, cols = len(grid), len(grid[0])

        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))
        miniutes = 0
        while q and fresh > 0:
            miniutes += 1
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r + dr, c+dc
                    if 0 <= nr < rows and 0<= nc < cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr,nc))
        return miniutes if fresh == 0 else -1