class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp[i] represents # of distinct combinations total up to amount i
        given X dollors coin, ways to get amount i equals the ways to get amount i - X
        so dp[i] = dp[i-x1] + dp[i-x2] + ...
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]
        return dp[amount]