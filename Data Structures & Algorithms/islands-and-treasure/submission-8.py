class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])

        # BFS
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        level = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in visited
                        and grid[nr][nc] == INF
                    ):
                        grid[nr][nc] = level
                        q.append((nr, nc))
                        visited.add((nr, nc))
            level += 1

