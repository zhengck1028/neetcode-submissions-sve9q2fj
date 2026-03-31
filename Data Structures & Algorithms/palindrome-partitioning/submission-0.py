class Solution:
    def partition(self, s: str) -> List[List[str]]:
        curSet = []
        res = []
        def dfs(curSet, i):
            if i >= len(s):
                res.append(curSet.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s[i:j+1]):
                    curSet.append(s[i:j+1])
                    dfs(curSet, j+1)
                    curSet.pop()
        dfs(curSet, 0)
        return res

    def isPali(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return  True