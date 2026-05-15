class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        d = [[0,1], [1,0],[0,-1],[-1,0]]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        time = 0
        while fresh >0 and q:
            
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in d:
                    nr, nc = r +dr, c+dc
                    if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue
                    elif grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            time += 1
        return time if fresh == 0 else -1