class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, curSet, total):
            if total == target:
                res.append(curSet.copy())
                return
            if total > target or i == len(candidates):
                return
            curSet.append(candidates[i])
            dfs(i + 1, curSet, total + candidates[i])
            curSet.pop()
            while i + 1 < len(candidates) and candidates[i+1] == candidates[i]:
                i += 1
            dfs(i + 1, curSet, total)
        dfs(0, [], 0)
        return res