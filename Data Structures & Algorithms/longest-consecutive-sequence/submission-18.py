class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        for i, num in enumerate(nums):
            hm[num] = i
        longest = 0
        for num in nums:
            if num - 1 not in hm:
                l = 1
                while num + 1 in hm:
                    l += 1
                    num += 1
                longest = max(longest, l)
        return longest