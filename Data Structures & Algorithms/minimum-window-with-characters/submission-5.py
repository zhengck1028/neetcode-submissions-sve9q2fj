class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hmT = Counter(t)
        hmRes = defaultdict(int)
        left = 0
        have = 0
        need = len(hmT)
        resL = float("inf")
        res = ""
        for right in range(len(s)):
            hmRes[s[right]] += 1
            if hmT[s[right]] == hmRes[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < resL:
                    resL = right - left + 1
                    res = s[left:right+1]
                hmRes[s[left]] -= 1
                if hmRes[s[left]] < hmT[s[left]]:
                    have -= 1
                if hmRes[s[left]] == 0:
                    del hmRes[s[left]]
                left += 1
        return res
