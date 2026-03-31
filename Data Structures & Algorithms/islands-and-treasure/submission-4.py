class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        q=deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        def addDist(r,c):
            if min(r,c)<0 or r>=rows or c>=cols or (r,c) in visit or grid[r][c]==-1:
                return
            q.append((r,c))
            visit.add((r,c))
        
        layer = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = layer
                addDist(r+1,c)
                addDist(r-1,c)
                addDist(r,c+1)
                addDist(r,c-1)
            layer += 1
