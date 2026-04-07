class Solution:
    def jump(self, nums: List[int]) -> int:
        curMax = 0
        jump = farthest = 0
        for i in range(len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == curMax:
                jump += 1
                curMax = farthest
        return jump