class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        d = [(0,1),(1,0),(-1,0),(0,-1)]
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()
        visit.add((0,0))
        while minHeap:
            h, r, c = heapq.heappop(minHeap)
            if r == n-1 and c == n -1:
                return h
            for dr, dc in d:
                row = r + dr
                col = c + dc
                if min(row,col)<0 or row == n or col == n or (row, col) in visit:
                    continue
                visit.add((row, col))
                heapq.heappush(minHeap, [max(grid[row][col], h), row, col])
