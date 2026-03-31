class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        N = m*n
        L, R = 0, N-1
        while L <= R:
            M = (L+R)//2
            if matrix[M // n][M % n] < target:
                L = M + 1
            elif matrix[M // n][M % n] > target:
                R = M - 1
            else:
                return True
        return False