class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(i, min(n, i + nums[i] + 1)):
                dp[j] = dp[i] or dp[j]
        return dp[n-1]