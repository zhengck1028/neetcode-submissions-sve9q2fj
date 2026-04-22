class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            hm[n] = i
        for i, n in enumerate(nums):
            new_target = target - n
            if new_target in hm:
                j = hm[new_target]
                if i != j:
                 return [i, j]