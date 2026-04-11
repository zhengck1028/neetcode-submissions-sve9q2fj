class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        prv2, prv1 = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(prv2 + nums[i], prv1)
            prv2 = prv1
            prv1 = cur
        return prv1