class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        def dfs(curSet, i):
            nonlocal res
            if i == len(nums):
                res.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            dfs(curSet, i + 1)
            curSet.pop()
            dfs(curSet, i + 1)
        dfs(cur,0)

        return res