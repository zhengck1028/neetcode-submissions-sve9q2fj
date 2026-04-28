class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmT = Counter(t)
        hmS = defaultdict(int)
        l = 0
        res = ""
        resLen = float("inf")
        need = len(hmT)
        have = 0
        for r in range(len(s)):
            hmS[s[r]] += 1
            if hmS[s[r]] == hmT[s[r]]:
                have += 1
            while have == need:
                if (r - l +1) < resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                hmS[s[l]] -= 1
                if s[l] in hmT and hmS[s[l]] < hmT[s[l]]:
                    have -= 1
                l += 1
        return res