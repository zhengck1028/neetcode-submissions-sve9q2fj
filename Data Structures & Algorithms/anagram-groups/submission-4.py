class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            counter = tuple(counter)
            if counter not in hm:
                hm[counter] = []
            hm[counter].append(s)
        return list(hm.values())