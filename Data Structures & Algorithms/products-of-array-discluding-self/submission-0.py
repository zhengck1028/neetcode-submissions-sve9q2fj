class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix_ = [1]*l
        suffix_ = [1]*l
        
        for i in range(1, l):
            prefix_[i] = prefix_[i-1] * nums[i-1] 
            suffix_[l-i-1] = suffix_[l-i] * nums[l-i]

        res = [0]*l
        for i in range(l):
            res[i] = prefix_[i] * suffix_[i]
        
        return res
