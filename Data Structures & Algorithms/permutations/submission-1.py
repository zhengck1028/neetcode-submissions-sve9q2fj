class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picks = [False] * len(nums)
        def dfs(cur, picks):
            if len(cur) == len(nums):
                res.append(cur.copy())
            for i in range(len(nums)):
                if not picks[i]:
                    cur.append(nums[i])
                    picks[i] = True
                    dfs(cur, picks)
                    cur.pop()
                    picks[i] = False
        dfs([], picks)
        return res