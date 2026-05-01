class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False] * len(nums)
        def dfs(curSet, picked):
            if len(curSet) == len(nums):
                res.append(curSet.copy())
                return
            for i, num in enumerate(nums):
                if not picked[i]:
                    picked[i] = True
                    curSet.append(num)
                    dfs(curSet, picked)
                    picked[i] = False
                    curSet.pop()
        dfs([], picked)
        return res