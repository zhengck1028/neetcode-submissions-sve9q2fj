class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L, R = 0, 0
        maxsum = float('-inf')
        cursum = float('-inf')
        for R in range(len(nums)):
            if cursum<0:
                cursum=0
                L=R
            
            cursum += nums[R]
            if cursum > maxsum:
                maxsum = cursum
                maxL, maxR = L, R
        return maxsum