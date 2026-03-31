class Solution:
    def canJump(self, nums: List[int]) -> bool:
        L, R = len(nums) -2, len(nums) -1
        while L >= 0:
            if nums[L] >= R-L:
                R = L
            L -= 1
        
        return R == 0