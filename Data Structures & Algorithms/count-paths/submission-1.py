class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*(n)
        for i in range(1,m):
            cur = [1]*n
            for j in range(1,n):
                cur[j] = dp[j]+cur[j-1]
            dp = cur
        return dp[n-1]
