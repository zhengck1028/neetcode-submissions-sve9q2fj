class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(1, (len(s)+1)):
            for w in wordDict:
                if i >= len(w):
                    if s[i-len(w):i] == w:
                        dp[i] = dp[i-len(w)] or dp[i]
        return dp[len(s)]