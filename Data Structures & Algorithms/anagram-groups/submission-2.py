class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 2.4
        hm = defaultdict(list)
        
        for word in strs:
            hashtable = [0]*26
            for c in word:
                hashtable[ord(c)-ord('a')] += 1
            hm[tuple(hashtable)].append(word)
        
        return list(hm.values())