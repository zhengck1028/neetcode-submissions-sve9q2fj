class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        hm = {}
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            longest = max(hm.values())
            while r - l + 1 - longest > k:
                hm[s[l]] -= 1
                longest = max(hm.values())
                l += 1
            res = max(res, r-l+1)
        return res