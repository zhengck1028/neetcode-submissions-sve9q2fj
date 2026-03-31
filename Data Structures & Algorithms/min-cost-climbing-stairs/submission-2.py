from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache  # 🪄 加上这一行，Python 自动帮你缓存函数返回值！
        def dfs(i):
            if i < 2:
                return 0
            
            c1 = dfs(i-1) + cost[i-1]
            c2 = dfs(i-2) + cost[i-2]
            
            return min(c1, c2)
            
        return dfs(len(cost))