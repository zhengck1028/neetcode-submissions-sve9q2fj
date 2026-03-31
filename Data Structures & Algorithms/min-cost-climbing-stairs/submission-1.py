
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prv1 = 0 # dp[0]
        prv2 = 0 # # dp[1]
        for i in range(2, len(cost)+1):
            cur = min(prv1 + cost[i-2], prv2+cost[i-1])
            prv1 = prv2
            prv2 = cur
        return prv2