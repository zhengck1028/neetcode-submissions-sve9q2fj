class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        fresh = 0
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        miniute = 0
        while fresh >0 and q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if 0<=r+dr<rows and 0<=c+dc<cols and grid[r+dr][c+dc]==1 and (r+dr,c+dc) not in visit:
                        grid[r+dr][c+dc] = 2
                        fresh -= 1
                        q.append((r+dr, c+dc))
                        visit.add((r+dr, c+dc))
            miniute += 1
        return miniute if fresh ==0 else -1
        