class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        dp[0] = 0
        minBuy = prices[0]
        for i in range(1, len(prices)):
            minBuy = min(minBuy, prices[i])
            dp[i] = max(dp[i-1], prices[i] - minBuy)
        return dp[len(prices)-1]