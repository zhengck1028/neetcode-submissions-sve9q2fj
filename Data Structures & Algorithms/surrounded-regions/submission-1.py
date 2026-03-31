class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        visit = set()
        def dfs(r, c):
            if min(r,c)<0 or r >= rows or c >= cols or board[r][c] =="X" or (r,c) in visit:
                return
            visit.add((r,c))
            board[r][c] = "S"
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                dfs(row, col)

        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == "O":
                    dfs(r, c)
        for c in range(cols):
            for r in [0, rows-1]:
                if board[r][c] == "O":
                    dfs(r, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O" 