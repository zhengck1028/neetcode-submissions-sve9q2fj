class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l, r = 0, 0
        while l <= r and l < len(nums):
            if l + nums[l] > r:
                r = l + nums[l]
            l += 1
        if r >= len(nums) - 1:
            return True
        else:
            return False