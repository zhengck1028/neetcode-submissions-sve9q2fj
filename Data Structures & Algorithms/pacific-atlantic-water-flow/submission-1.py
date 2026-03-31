class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        res = []
        pac = set()
        alt = set()
        def dfs(r,c,visit,prvHeight):
            if min(r,c)<0 or r >= rows or c >= cols or (r,c) in visit or heights[r][c]<prvHeight:
                return
            visit.add((r,c))
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                dfs(row, col, visit, heights[r][c])


        for r in range(rows):
            dfs(r,0,pac,0)
            dfs(r,cols-1,alt, 0)

        for c in range(cols):
            dfs(0,c,pac,0)
            dfs(rows-1,c,alt,0)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in alt:
                    res.append([r,c])
        return res