class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hashMap = defaultdict(int)
        for r in range(len(s)):
            hashMap[s[r]] += 1
            longest = max(hashMap.values())
            while r-l+1 > longest + k:
                hashMap[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res