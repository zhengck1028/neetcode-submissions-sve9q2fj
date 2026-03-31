class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(curSet, i):
            if i == len(nums):
                res.append(curSet.copy())
                return
            curSet.append(nums[i])
            dfs(curSet, i+1) 
            curSet.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(curSet, i+1) 
        dfs([], 0)
        return res