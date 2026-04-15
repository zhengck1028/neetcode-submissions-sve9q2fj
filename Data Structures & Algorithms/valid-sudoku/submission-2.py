class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmCol = defaultdict(list)
        hmRow = defaultdict(list)
        hmBlk = defaultdict(list)
        n = len(board)
        for i in range(n):
            for j in range(n):
                num = board[i][j]
                if num == ".":
                    continue
                if num in hmRow[i] or num in hmCol[j] or num in hmBlk[(i // 3, j // 3)]:
                    return False
                hmRow[i].append(num)
                hmCol[j].append(num)
                hmBlk[(i // 3, j // 3)].append(num)
        return True