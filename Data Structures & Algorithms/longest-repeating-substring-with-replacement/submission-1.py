class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hm = {}
        max_l = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            max_l = max(max_l, hm[s[r]])
            while r - l + 1 -max_l > k:
                hm[s[l]] -= 1
                l += 1
            res = max (res, r - l + 1)
        return res