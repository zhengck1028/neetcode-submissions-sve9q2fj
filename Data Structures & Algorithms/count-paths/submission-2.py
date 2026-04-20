class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for r in range(1, m):
            cur_dp = [1] * n
            for c in range(1, n):
                cur_dp[c]=cur_dp[c-1]+dp[c]
            dp = cur_dp
        return dp[n-1]