class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L= 0
        res = 0
        hm = {}
        max_S = 0
        for R in range(len(s)):
            hm[s[R]] = hm.get(s[R], 0) + 1
            max_S = max(hm.values())
            while R - L - max_S + 1 > k:
                hm[s[L]] = hm.get(s[L], 0) - 1
                max_S = max(hm.values())
                L += 1
            
            res = max(res, R-L+1)
        return res