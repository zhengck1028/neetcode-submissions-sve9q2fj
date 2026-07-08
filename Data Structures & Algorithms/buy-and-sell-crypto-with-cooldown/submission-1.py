class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [1,3,4,0,4]
        hold = -prices[0]
        sell = 0
        cooldown = 0

        for i in range(1, len(prices)):
            p = prices[i]
            newHold = max(cooldown - p, hold)
            newCooldown = max(cooldown, sell)
            newSell = hold + p

            hold = newHold
            cooldown = newCooldown
            sell = newSell
        
        return max(cooldown, sell)