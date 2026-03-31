class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curSet = []
        total = 0
        candidates.sort()
        def dfs(curSet, i, total):
            if total == target:
                res.append(curSet.copy())
                return
            if i > len(candidates) - 1 or total > target:
                return

            curSet.append(candidates[i])
            
            dfs(curSet, i + 1, total + candidates[i])
            curSet.pop()
            while i+1<len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(curSet, i + 1, total)
        dfs(curSet, 0, 0)
        return res