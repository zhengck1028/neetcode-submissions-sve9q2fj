class Solution:
    def minWindow(self, s: str, t: str) -> str:
        L = 0
        hmT = Counter(t)
        hm = {}
        min_size = float('inf')
        res = []
        have, need = 0, len(hmT)
        for R in range(len(s)):
            hm[s[R]] = hm.get(s[R], 0) + 1
            if s[R] in hmT and hmT[s[R]] == hm[s[R]]:
                have += 1
            while have == need and (s[L] not in hmT or hm[s[L]] > hmT[s[L]]):
                hm[s[L]] -= 1
                L += 1
            if have == need:
                size = R-L+1
                if size < min_size:
                    res = [L, R]
                    min_size = size
        return s[res[0] : res[1]+1] if min_size != float("inf") else ""