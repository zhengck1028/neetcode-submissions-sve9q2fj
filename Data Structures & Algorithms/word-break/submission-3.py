class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                l = len(word)
                if i - l >= 0 and s[i-l:i] == word:
                    dp[i] = dp[i-l] or dp[i]
        return dp[n]