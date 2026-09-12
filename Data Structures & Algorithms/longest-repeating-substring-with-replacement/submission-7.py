class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        hm = defaultdict(int)
        l = 0

        for r in range(len(s)):
            hm[s[r]] += 1
            longest = max(hm.values())
            while l < r and r - l + 1 - longest > k:
                hm[s[l]] -= 1

                l += 1
            res = max(res, r - l + 1)
        return res
