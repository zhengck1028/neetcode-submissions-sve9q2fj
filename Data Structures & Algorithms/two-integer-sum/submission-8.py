class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in hm:
                return [hm[find], i]
            hm[num] = i
        