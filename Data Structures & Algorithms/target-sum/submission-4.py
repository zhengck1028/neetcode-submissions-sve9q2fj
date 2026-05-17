class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        total = sum(nums)
        dp[0] = 1
        for num in nums:
            cur = defaultdict(int)
            for i in dp.keys():
                cur[i-num] += dp[i] 
                cur[i+num] += dp[i]
            dp = cur
        return dp[target]