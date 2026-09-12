class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        hs = set()
        for r in range(len(s)):
            while l < r and s[r] in hs:
                hs.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            hs.add(s[r])
        return res