class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        n                 top
        n-1
        ...
        i+2
        i+1 cost[i+1]
        i cost[i]
        ...
        2
        1
        0

        dp[i] # min cost to reach ith stair
        return dp[n] at last
        """
        if not cost or len(cost) == 1:
            return 0
        n = len(cost) # 3
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0 # [0, 0, 0, 0]
        for i in range(2, n+1):
            dp[i] = min(cost[i-2] + dp[i-2], cost[i-1] + dp[i-1]) # dp[2] = min(1+0,2+0) = 1
        return dp[n] # dp[3] = min(2+0,1+3) = 2