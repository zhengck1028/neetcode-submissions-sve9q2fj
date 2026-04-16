class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashMap1 = Counter(s1)
        hashMap2 = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            hashMap2[s2[r]] += 1
            if r - l + 1 > len(s1):
                hashMap2[s2[l]] -= 1
                if hashMap2[s2[l]] == 0:
                    del hashMap2[s2[l]]
                l += 1
            if hashMap1 == hashMap2:
                return True
        return False