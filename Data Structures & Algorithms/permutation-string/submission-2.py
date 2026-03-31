class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        mapS1= {}
        for s in s1:
            mapS1[s] = mapS1.get(s, 0) + 1
        
        mapS2 = {}
        for r in range(len(s2)):
            if s2[l] not in mapS1:
                l = r
            while s2[r] in mapS2 and mapS2[s2[r]] >= mapS1[s2[r]]:
                mapS2[s2[l]] = mapS2.get(s2[l], 0) - 1
                l += 1
            if s2[r] in mapS1:
                mapS2[s2[r]] = mapS2.get(s2[r], 0) + 1
                if mapS1 == mapS2:
                    return True
            else:
                mapS2 = {}
                l=r
            
        return False