class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        if len(hashset) < len(nums):
            return True
        return False