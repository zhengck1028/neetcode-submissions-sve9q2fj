class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L ,R = 0, 0
        res = 0
        while R < len(prices)-1:
            R += 1
            if prices[R]<prices[L]:
                L = R
            res = max(res, prices[R] - prices[L])
        return max(res, 0)