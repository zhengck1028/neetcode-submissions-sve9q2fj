class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b=prices[0]
        for s in prices:
            profit = max(profit, s - b)
            b = min(b, s)
        return profit