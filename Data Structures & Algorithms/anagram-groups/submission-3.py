class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMaps = {}
        for word in strs:
            counter = [0]*26
            for c in word:
                counter[ord(c)-ord('a')] += 1
            counter = tuple(counter)
            if counter not in hashMaps:
                hashMaps[counter] = []
            hashMaps[counter].append(word)

        return list(hashMaps.values())
            