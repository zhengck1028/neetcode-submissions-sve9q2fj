class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = [False]*len(nums)
        def dfs(curSet,picked):
            if len(curSet) == len(nums):
                res.append(curSet.copy())
                return
            for i in range(len(nums)):
                if picked[i]:
                    continue
                curSet.append(nums[i])
                picked[i] = True
                dfs(curSet, picked)
                curSet.pop()
                picked[i] = False
                # dfs(curSet, picked)
        
        dfs([],picked)
        return res