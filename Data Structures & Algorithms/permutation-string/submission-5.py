class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = [0] *26
        hm = [0] *26
        for c in s1:
            hm1[ord(c) - ord('a')] += 1
        l = 0
        for r in range(len(s2)):
            hm[ord(s2[r]) - ord('a')] += 1
            while hm[ord(s2[r]) - ord('a')] > hm1[ord(s2[r]) - ord('a')]:
                hm[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if hm1 == hm:
                return True
        return False