class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = Counter(s1)
        hm = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            if s2[r] not in hm1:
                l = r
                hm = defaultdict(int)
                continue
            hm[s2[r]] += 1
            while hm[s2[r]] > hm1[s2[r]]:
                hm[s2[l]] -= 1
                l += 1
            if hm1 == hm:
                return True
        
        return False