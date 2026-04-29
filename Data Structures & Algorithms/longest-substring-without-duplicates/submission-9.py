class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while hs and s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            res = max(res, r - l + 1)
        return res