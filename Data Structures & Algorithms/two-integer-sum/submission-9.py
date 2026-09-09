class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            n = nums[i]
            if target - n in hm:
                return[hm[target - n], i]
            hm[n] = i