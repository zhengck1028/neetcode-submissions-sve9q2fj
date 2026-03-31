class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()      # 记录被占据的列
        posDiag = set()   # 记录被占据的正对角线 (r + c)
        negDiag = set()   # 记录被占据的负对角线 (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)] # 正确初始化棋盘
        
        # 我们按行 (r) 往下推进，不需要在 DFS 里传一堆参数
        def dfs(r):
            # 1. 成功走完了 N 行，说明找到了一个合法解
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            # 2. 遍历当前行 r 的所有列 c
            for c in range(n):
                # 如果当前列，或者对角线已经被别的皇后占了，直接跳过
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # 做选择：在这里放下皇后，并宣告占领领地
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # 继续探索下一行
                dfs(r + 1)
                
                # 撤销选择 (回溯核心)：把刚才放的皇后拿走，让出领地
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        # 从第 0 行开始回溯
        dfs(0)
        return res