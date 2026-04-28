class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curSet, i):
            if i == len(nums):
                res.append(curSet.copy())
                return
            curSet.append(nums[i])
            dfs(curSet, i + 1)
            curSet.pop()
            dfs(curSet, i + 1)
            return
        dfs([], 0)
        return res