class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curSet, total):
            if total == target:
                res.append(curSet.copy())
                return
            if total > target or i == len(nums):
                return
            curSet.append(nums[i])
            dfs(i, curSet, total + nums[i])
            curSet.pop()
            dfs(i + 1, curSet, total)
            # return
        dfs(0, [], 0)
        return res