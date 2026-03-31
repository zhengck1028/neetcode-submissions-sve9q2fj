class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curSet,i,total):
            if total == target:
                res.append(curSet.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            curSet.append(nums[i])
            dfs(curSet, i, total + nums[i])
            curSet.pop()
            dfs(curSet, i + 1, total)
        dfs([], 0, 0)
        return res