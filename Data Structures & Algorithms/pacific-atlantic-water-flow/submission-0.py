class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfsPac(r,c,h,visited):
            if min(r, c) < 0:
                return True
            if r >= rows or c >= cols or heights[r][c] > h or (r,c) in visited:
                return False
            visited.append((r,c))
            height = heights[r][c]
            res = (
                dfsPac(r+1, c, height, visited) or
                dfsPac(r-1, c, height, visited) or
                dfsPac(r, c+1, height, visited) or
                dfsPac(r, c-1, height, visited)
            )
            return res

        def dfsAlt(r,c,h,visited):
            if r >= rows or c >= cols:
                return True
            if min(r, c) < 0 or heights[r][c] > h or (r,c) in visited:
                return False
            height = heights[r][c]
            visited.append((r,c))
            res = (
                dfsAlt(r+1, c, height, visited) or
                dfsAlt(r-1, c, height, visited) or
                dfsAlt(r, c+1, height, visited) or
                dfsAlt(r, c-1, height, visited)
            )
            return res
        
        res = []
        for r in range(rows):
            for c in range(cols):
                h = heights[r][c]
                if dfsPac(r, c, float('inf'), []) and dfsAlt(r, c, float('inf'), []):
                    res.append([r, c])
        return res