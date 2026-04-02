class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ## DP
        res = nums[0]
        curMin = curMax = 1

        for n in nums:
            tmp = n*curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(n*curMin, tmp, n)
            res = max(curMax, res)

        return res