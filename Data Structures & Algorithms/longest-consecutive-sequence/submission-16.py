class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in hashSet:
                k = 1
                while n in hashSet:
                    res = max(res, k)
                    k += 1
                    n += 1
        return res