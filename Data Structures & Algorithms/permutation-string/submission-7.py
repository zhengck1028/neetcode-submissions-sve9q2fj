class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hm1 = Counter(s1)
        hm = defaultdict(int)
        for ch in s2[:len(s1)]:
            hm[ch] += 1
        if hm == hm1:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            ch = s2[r]
            hm[ch] += 1
            hm[s2[l]] -= 1
            if hm[s2[l]] == 0:
                del hm[s2[l]]
            if hm == hm1:
                return True
            l += 1
        return False