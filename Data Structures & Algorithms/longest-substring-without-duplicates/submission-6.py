class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        L, R = 0, 1
        res = 0
        hs = set(s[L])
        while R <= len(s) - 1:
            while s[R] in hs:
                hs.remove(s[L])
                L += 1
            hs.add(s[R])
            res = max(res, R-L+1)
            R += 1
        return res