class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        to_set = set(nums)
        if len(to_set) < len(nums):
            return True 
        else:
            return False