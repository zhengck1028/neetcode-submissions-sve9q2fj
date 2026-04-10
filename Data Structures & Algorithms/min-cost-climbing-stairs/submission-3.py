
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prv2, prv1 = 0, 0
        for i in range(2, n+1):
            cur = min(prv1+cost[i-1], prv2+cost[i-2])
            prv2 = prv1
            prv1 = cur
        return prv1