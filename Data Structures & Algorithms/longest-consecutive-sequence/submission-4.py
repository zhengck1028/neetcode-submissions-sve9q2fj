class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        if len(nums) in [0,1] : return len(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                cnt = 1
                while nums[i] + cnt in nums_set:
                    cnt += 1
                longest = max(longest, cnt)
        
        return longest

