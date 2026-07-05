class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        d = [(1,0),(0,1),(-1,0),(0,-1)]
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        # BFS
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r,c))

        distance = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols and \
                    grid[nr][nc] not in (-1, 0) and (nr, nc) not in visit:
                        grid[nr][nc] = distance
                        q.append((nr, nc))
                        visit.add((nr, nc))
            distance += 1

        
        