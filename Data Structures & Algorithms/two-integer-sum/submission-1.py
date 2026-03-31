class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [3,4,5,6], target = 7
        for i, n in enumerate(nums):
            s = target - n
            for j in range(len(nums)-i-1):
                if nums[j+i+1] == s:
                    return [i, j+i+1]
