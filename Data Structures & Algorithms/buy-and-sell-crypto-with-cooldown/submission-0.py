class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 3 type of state
        hold = float("-inf")
        sold = 0
        rest = 0
        for p in prices:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest 
            
            hold = max(prev_hold, prev_rest - p)
            sold = prev_hold + p
            rest = max(prev_rest, prev_sold)
        return max(sold, rest)