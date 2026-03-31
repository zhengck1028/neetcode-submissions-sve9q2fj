class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1
        while L<=R:
            M = (L + R) // 2
            if M == len(nums)-1:
                return nums[0]
            if nums[M+1]<nums[M]:
                return nums[M+1]
            elif nums[M+1]>nums[M]>=nums[0]:
                L = M + 1
            elif nums[0]>=nums[M+1]>nums[M]:
                R = M - 1