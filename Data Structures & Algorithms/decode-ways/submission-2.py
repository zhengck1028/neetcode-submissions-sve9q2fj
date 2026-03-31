class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        prv1, prv2 = 1, 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += prv2
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                cur += prv1
            prv1 = prv2
            prv2 = cur
        return prv2