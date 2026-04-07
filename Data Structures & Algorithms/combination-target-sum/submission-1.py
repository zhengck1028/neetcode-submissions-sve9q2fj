class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curSet, total, i):
            if total == target:
                res.append(curSet.copy())
                return
            if total > target or i == len(nums):
                return
            curSet.append(nums[i])
            dfs(curSet, total + nums[i], i)
            curSet.pop()
            dfs(curSet, total, i + 1)
        dfs([],0, 0)
        return res