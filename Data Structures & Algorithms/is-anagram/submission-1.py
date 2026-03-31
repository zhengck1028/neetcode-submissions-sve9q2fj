class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}
        for ss in s:
            hm1[ss] = hm1.get(ss,0) + 1
        for tt in t:
            hm2[tt] = hm2.get(tt,0) + 1
        return hm1 == hm2
        