class Solution:
    def findMin(self, nums: List[int]) -> int:
        # start from hint 2
        l, r = 0, len(nums)-1
        while l<=r:
            m = l+(r-l)//2
            if nums[m-1]>nums[m]:
                return nums[m]
            else:
                if nums[m] >= nums[0]:
                    l = m + 1
                elif nums[m] < nums[0]:
                    r = m - 1
        return nums[0]