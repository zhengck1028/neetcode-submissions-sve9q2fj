class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        picked = [False] * len(nums)
        res = []
        def dfs(i, picked, curSet):
            if len(curSet) == len(nums):
                res.append(curSet.copy())
                return
            for i in range(len(nums)):
                if not picked[i]:
                    curSet.append(nums[i])
                    picked[i] = True
                    dfs(i+1, picked, curSet)
                    curSet.pop()
                    picked[i] = False
            return
        dfs(0, picked, [])
        return res