class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
            
        rows, cols = len(board), len(board[0])
        
        # 辅函数：用来把安全的 "O" 感染成 "T"
        def dfs(r, c):
            # 拦截条件：越界，或者不是 "O"（如果是 "X" 或者是已经访问过的 "T"，都退回）
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            
            # 把当前安全节点标记为 "T"
            board[r][c] = "T"
            
            # 继续向四周渗透
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. 边缘渗透：让四条边上的 "O" 向内扩散，打上安全标记 "T"
        for r in range(rows):
            dfs(r, 0)           # 第一列
            dfs(r, cols - 1)    # 最后一列
            
        for c in range(cols):
            dfs(0, c)           # 第一行
            dfs(rows - 1, c)    # 最后一行

        # 2. 秋后算账：遍历全图，进行清洗和恢复
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    # 没被标记为 "T" 的 "O"，说明是死棋，吃掉！
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    # 安全区，恢复原状
                    board[r][c] = "O"