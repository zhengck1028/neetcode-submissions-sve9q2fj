class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = Counter(s1)
        hm = Counter(s2[:len(s1)-1])
        for R in range(len(s1)-1, len(s2)):
            hm[s2[R]] += 1
            if hm == set1:
                return True
            else:
                hm[s2[R-len(s1)+1]] -= 1
        return False