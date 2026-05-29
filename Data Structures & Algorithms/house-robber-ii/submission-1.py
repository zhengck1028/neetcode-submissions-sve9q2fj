class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums: List[int]) -> int:
        prv2, prv1 = 0, 0
        for i in range(len(nums)):
            cur = max(prv2 + nums[i], prv1)
            prv2 = prv1
            prv1 = cur
        return prv1