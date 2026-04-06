class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for n in nums:
            if n-1 not in hashSet:
                len = 0
                while n+len in hashSet:
                    len += 1
                res = max(res, len)
        return res