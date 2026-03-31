class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        # if n <= 2:
        #     return n
        k = n
        while k > 0:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            k -= 1
        return dp[1]