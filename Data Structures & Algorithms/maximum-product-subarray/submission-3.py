class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = curMin = 1
        for num in nums:
            tmp = curMax
            curMax = max(num, curMax*num, curMin*num)
            curMin = min(num, tmp*num, curMin*num)
            res = max(res, curMax)
        return res
