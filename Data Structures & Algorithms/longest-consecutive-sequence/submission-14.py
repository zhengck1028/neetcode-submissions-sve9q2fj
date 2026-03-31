class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  2.4
        res=0
        numSet = set(nums)
        for n in numSet:
            if n-1 not in numSet:
                x = 1
                while n+x in numSet:
                    x +=1
                res= max(res, x)
        
        return res