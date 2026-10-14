class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        prv2 = nums[0]
        prv1 = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            cur = max(nums[i] + prv2, prv1)
            prv2 = prv1
            prv1 = cur
        return prv1