class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxL = 0
        idx = 0
        for i in range(n):
            l = 0
            while i-l>=0 and i+l<n and s[i-l] == s[i+l]:
                if l * 2 > maxL:
                    maxL = 2 * l
                    idx = i - l
                l += 1
            l = 0
            while i-l>=0 and i+1+l<n and s[i-l] == s[i+1+l]:
                if 2 * l + 1 > maxL:
                    maxL = 2 * l + 1
                    idx = i - l
                l += 1


        return s[idx:(idx+maxL+1)]