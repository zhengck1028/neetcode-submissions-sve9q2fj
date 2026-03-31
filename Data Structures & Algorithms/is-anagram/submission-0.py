class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "racecar", t = "carrace"
        s_hashmap = dict()
        t_hashmap = dict()
        for c in s:
            s_hashmap[c] = s_hashmap.get(c, 0) + 1
        for c in t:
            t_hashmap[c] = t_hashmap.get(c, 0) + 1
        
        return s_hashmap == t_hashmap