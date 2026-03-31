class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)
        for n in nums:
            if n-1 not in numSet:
                rs = 1
                while True:
                    if n + 1 in numSet:
                        rs += 1
                    else:
                        break
                    n += 1
                res = max(rs, res)
        return res